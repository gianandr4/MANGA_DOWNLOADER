import requests,bs4, os

name='Berserk'
url='https://kissmanga.org/chapter/ilsi12001567132882/chapter_' ## ROOT FOLDER
start=330
end=361



path='C:\\Users\\Drastis\\Desktop\\MANGA_DOWNLOAD\\' + name  ####  MANGA FOLDER
os.makedirs(path,exist_ok=True)


## CHAPTERS
while start>0 and start<end+1:


    chapter=path+'\\Chapter_'+str(start)            ##############CHAPTER FOLDER
    os.makedirs(chapter,exist_ok=True)
    c_url = url+str(start)
    res = requests.get(c_url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'html.parser')

    img_list = soup.select('#centerDivVideo img')

    if img_list ==[]:
        print('images not found')
    else:
        ## PAGES
        for j,i in enumerate(img_list):
            page_name='page_'+str(j+1)
            manga_url = i.get('src')
            response = requests.get(manga_url)

            ################################################# IMAGE/PAGE NAME
            img_name=chapter+'\\'+str(start)+'_Page_'+str(j+1)+'.png'


            with open(img_name,'wb') as f:
                f.write(response.content)




    print('Complete: ',chapter)
    start +=1

print('done')


url='https://kissmanga.org/manga/read_hunter_x_hunter_manga_online_free2'
test=requests.get(url)
test.raise_for_status()

soup = bs4.BeautifulSoup(test.text, 'html.parser')

arser = soup.find("strong",{'class':'bigChar'})
arser.text




arse=soup.find("div", {"class": "barContent episodeList full"}).select('a')
arse[0].get('title')
print(repr(arse[0].text))

bigChar



