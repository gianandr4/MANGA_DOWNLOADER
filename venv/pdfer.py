import os ,shutil
working_dir=r'C:\Users\Drastis\PycharmProjects\MANGA_DOWNLOADER\venv'
import img2pdf

from PIL import Image



manga_folder=r'C:\Users\Drastis\PycharmProjects\MANGA_DOWNLOADER\venv\Downloads\All_You_Need_Is_Kill'
chapters=os.listdir(manga_folder)

for chapter in chapters:
    images_path=manga_folder+'\\'+chapter
    images_folder = os.listdir(images_path)

    longest_string = len(max(images_folder, key=len))
    shortest_string = len(min(images_folder, key=len))

    # renaming
    for image in images_folder:
        if len(image)<longest_string:
            new_name=images_path+'\\'
            new_name+=image.replace('Page_','Page_'+'0'*(longest_string-shortest_string))
            old_name=images_path+'\\'+image

            shutil.move(old_name,new_name)
            print(new_name)




    im_list=[]
    for i,image in enumerate(images_folder):

        path = images_path + '\\' + image

        img = Image.open(path)
        if img.size[0]> img.size[1]:
            img.rotate(00, expand=True).save(path)
            img.close()




        im_list.append(path)

    name = manga_folder + '\\' + chapter + '.pdf'

    ## a4 shit
    a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
    layout_fun = img2pdf.get_layout_fun(a4inpt)

    with open(name,"wb") as f:
        f.write(img2pdf.convert(im_list,layout_fun=layout_fun))


#
# # for i in im_list:
#     image_path='C:\\Users\\Drastis\\PycharmProjects\\MANGA_DOWNLOADER\\venv\\Downloads\\All_You_Need_Is_Kill\\chapter_1.2\\1.2_Page_00.png'
#     fold_path = 'C:\\Users\\Drastis\\PycharmProjects\\MANGA_DOWNLOADER\\venv\\Downloads\\All_You_Need_Is_Kill\\asda\\2.png'
#
#
#
#     img = Image.open(image_path)
#     img.show()
#     img.rotate(90,expand=True).save(image_path)#.save(image_path)
#
#     img.close()
#     input()
#
#
#
#
#
#
#


