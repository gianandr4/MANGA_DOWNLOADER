import requests, bs4, os, time, pathlib
import img2pdf
from PIL import Image

##########################################
clear = lambda: os.system('cls')  # clear screen


def welcome():
    w_inputs = ['UPDATE', 'EXIT', '', 'HELP', 'CHECK','CONFIG']
    print('''WELCOME TO MANGANATOR''')
    ######################################  HELP MENU
    while True:

        print(
            '''
        [Paste link] - to Download and check files
        [Enter] - to view config.txt
        Update - to Update
        Help - to show help
        Exit- to exit
        '''
        )
        w_input = input('>> ').upper()
        ###################################  WRONG INPUT
        if not w_input.upper() in w_inputs and not w_input.lower().startswith('https://'):
            print('WRONG INPUT')
            clear()
            continue
        ################################## EXIT
        if w_input == 'EXIT':
            exit()
        ################################## HELP
        if w_input == 'HELP':
            clear()
            print('''WELCOME TO MANGANATOR

            UPDATE - Starts downloading manga from newest to oldest
                    If a folder containing a chapter is found the
                    program stops. Essentially you should always keep
                    the last chapter that you read for this to work

            DOWNLOAD - Starts downloading manga from oldest to newest
                    If a chapter is downloaded completely it skips it
                    It can be interrupted without losing considerable 
                    progress on your download

            EXIT - ^_^


            ''')

        ################################# UPDATE
        # Starts downloading manga from latest to oldest
        # If a folder containing a chapter is found the
        # program stops. Essentially you should always leave a

        if w_input == 'UPDATE':
            with open('config.txt', 'r') as f:
                w_list = f.readlines()
                # print(w_list)

            return w_list, 'UPDATE'

        ################################ FULL CHECK

        if w_input == '':
            with open('config.txt', 'r') as f:
                w_list = f.read()
                # print(w_list)
                w_list=w_list.split('\n\n')


            while True:
                print('''_________________________________________
                 Config.txt
                 /exit to close
                ''')

                for i,item in enumerate(w_list):
                    if '\n' in item:

                        x=item.split('\n')[0]
                        y=item.split('\n')[1]
                        differential_item = len(max(w_list, key=len)) -len(item) + 3

                        print(i,' ',x,differential_item*' ',y)

                print('''0.UPDATE, CHECK, DELETE''')
                x_list=['UPDATE', 'CHECK', 'DELETE']
                x=input('(select item )>>')
                clear()
                print(w_list[int(x)])







            # return w_list, 'CHECK'



        if w_input == 'CHECK':
            with open('config.txt', 'r') as f:
                w_list = f.readlines()

            return w_list, 'CHECK'

        if w_input.lower().startswith('https://'):
            print('edw')
            while True:
                if not w_input.lower().startswith('https://kissmanga.org/'):

                    print('Incorrect url\n', w_url)
                    print('Find your manga from: https://kissmanga.org/')
                    input('')
                    w_url = input('Paste link to download: ')
                    clear()
                else:
                    break
            w_url = w_input.lower()

            w_request = requests.get(w_url)
            w_request.raise_for_status()
            print(w_request)

            w_soup = bs4.BeautifulSoup(w_request.text, 'html.parser')

            w_soup = w_soup.find("strong", {'class': 'bigChar'})
            w_name = w_soup.text

            print('\nPress [Enter] to add', w_name, 'to the config: ')
            w_choice = input('>>')
            if w_choice == '':
                with open('config.txt', 'r') as f:
                    w_check_list = f.readlines()
                if not w_url in w_check_list and not w_url + '\n' in w_check_list:
                    print('Added to config')
                    with open('config.txt', 'a+') as f:
                        f.write(w_name + '\n')
                        f.write(w_url + '\n\n')
                print("Item already in config, proceeding to check it's files")
            return [w_url], 'DOWNLOAD'


def link_request(lr_url):
    lr_res = requests.get(lr_url)
    lr_res.raise_for_status()
    return lr_res


def soup_parsing(sp_res):
    sp_soup = bs4.BeautifulSoup(sp_res.text, 'html.parser')
    sp_chapter_links_parser = sp_soup.find("div", {"class": "barContent episodeList full"}).select('a')
    sp_name = sp_chapter_links_parser[0].get('title').replace('Read ', '').replace(' Manga online ',
                                                                                   '')  # Read Berserk Manga online
    return sp_name, sp_chapter_links_parser


def list_of_links(lol_list, lol_repo):
    ('Listing available urls')
    lol_chapter_links = []
    for i in lol_list:
        lol_chapter_links.append(repo + i.get('href'))
    lol_chapter_links
    return lol_chapter_links


def list_of_images(mfl_url):
    mfl_res = requests.get(mfl_url)
    mfl_soup = bs4.BeautifulSoup(mfl_res.text, 'html.parser')
    mfl_img_list = mfl_soup.select('#centerDivVideo img')
    mfl_img_list_clean = []
    for mfl_image in mfl_img_list:
        mfl_img_list_clean.append(mfl_image.get('src'))

    return mfl_img_list_clean


def image_download(id_image_url, id_path):
    id_response = requests.get(id_image_url)
    with open(id_path + '.png', 'wb') as f:
        f.write(id_response.content)


################################# MAIN
urls, choice = welcome()
clear()

# url= input('Enter manga Url: ')##### input anime

repo = 'https://kissmanga.org'

########################################## DIR
root = 'Downloads'
os.makedirs(root, exist_ok=True)
os.chdir(root)
############################################################# convert to pdf
# while True:
#     convert_to_pdf=input('Convert to pdf? Yes/No: ')
#     if not convert_to_pdf.upper() in ['YES','NO','']
# if convert_to_pdf.upper() in ['YES','']:
#     convert_to_pdf=True
# else:
#     convert_to_pdf = False

for url in urls:
    if not url.startswith('https://kissmanga.org/'):
        # print('INCORRECT URL\n',url)
        continue

    url = url.replace('\n', '')

    # download page from url
    request = link_request(url)

    # parse the downloaded page
    # get manga name and list of chapter links
    name, chapter_list = soup_parsing(request)

    ###################################### DIR NAME
    name = name.replace(':', '-').replace(' ', '_')
    os.makedirs(name, exist_ok=True)
    print(name.upper())

    chapters = list_of_links(lol_list=chapter_list, lol_repo=repo)

    # run check to edit the list of links
    if choice == 'DOWNLOAD' or choice == 'CHECK': chapters.reverse()

    for chapter in chapters:
        # print(chapter)
        chapter_name_replace = chapter.replace(repo, '').replace('/chapter/', '')
        manga_code, chapter_name = chapter_name_replace.split('/')  # CHAPTER NAME

        # new folder with chapter name
        chapter_dir = name + '\\' + chapter_name
        os.makedirs(chapter_dir, exist_ok=True)

        ##########################################################################  MAKE DIR WITH CHAPTER NAME

        images = list_of_images(chapter)
        # Checks if there are images in the chapter link
        if images == []:
            print('Link Broken->', chapter)
            continue
        # checks if the images in folder are the same number with those in the chapter link
        if len(images) == len(os.listdir(chapter_dir)):
            print('Skipping ->',chapter_dir)

            if choice == 'UPDATE':  ########################### IF UPDATE FLAG IS ON CHECKS ONLY LAST CHAPTER
                print(name,'updated, moving to net item\n')
                break
            continue

        for i, image in enumerate(images):
            print('.' * i, end='\r')

            if len(str(i)) < 3:

                page_num = (3 - len(str(i))) * '0' + str(i)

            else:
                page_num = str(i)

            image_name = chapter_name[8:] + '_Page_' + page_num
            image_path = chapter_dir + '\\'

            image_download(id_image_url=image, id_path=image_path + image_name)

        # if convert_to_pdf:
        #     print('not ready yet')

        print('Download Complete ->', '(' + str(len(images)) + ')', chapter_dir)

print('SUCESS!!', choice, 'COMPLETE.')
input('')
#
# 'https://kissmanga.org/manga/ao_no_orchestra'+'\n' in x



