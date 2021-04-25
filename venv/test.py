import os ,shutil
import img2pdf
from PIL import Image


root=r'C:\Users\Drastis\Desktop\manganator\Downloads'
os.chdir(root)

manga_list=os.listdir()

for manga in manga_list:


    chapters_list=os.listdir(manga)

    chapter_path=manga


    for chapter in chapters_list:
        # input()

        images_path=chapter_path+'\\'+chapter

        images_list= os.listdir(images_path)

        longest_string = len(max(images_list, key=len))
        shortest_string = len(min(images_list, key=len))
        if longest_string - shortest_string <3:
            longest_string+=1

        # renaming
        for image in images_list:



            if len(image)<longest_string:
                namer=[]
                for i in range(999):
                   x= (3 - len(str(i)))*'0'+str(i)
                   namer.append(x+'.png')

                for i in namer:
                    t=False
                    if i in image:
                        retur=i
                        t=True
                        break



                old_name=images_path+'\\'+image

                if 'Page_' in old_name:
                    a, b = old_name.split('_Page_')
                else:
                    a, b = image.split('_')
                    a=images_path+'\\'+a


                if t:
                    new_name=a+'_Page_'+retur

                print(old_name,'  ',new_name)

                shutil.move(old_name,new_name)

        # print(manga,'---',chapter,'--','COMPLETE')




        # im_list=[]
        # for i,image in enumerate(images_folder):
        #
        #     path = images_path + '\\' + image
        #
        #     img = Image.open(path)
        #     if img.size[0]> img.size[1]:
        #         img.rotate(00, expand=True).save(path)
        #         img.close()
        #
        #
        #
        #
        #     im_list.append(path)
        #
        # name = manga_folder + '\\' + chapter + '.pdf'
        #
        # ## a4 shit
        # a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        # layout_fun = img2pdf.get_layout_fun(a4inpt)
        #
        # with open(name,"wb") as f:
        #     f.write(img2pdf.convert(im_list,layout_fun=layout_fun))










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
input('done')

