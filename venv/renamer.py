import os
import shutil


x=input('number: ')
path='C:\\Users\\Drastis\\Desktop\\Bleach 1-686(Complete)\\Bleach v'+x
newpath='C:\\Users\\Drastis\\Desktop\\Bleach 1-686(Complete)\\v'+x


arr = os.listdir(path)


# print(arr)
cnt=0
cnt2=1
for j,i in enumerate(arr):
    link = path+"\\"+i
    arr2 = os.listdir(link)
    if len(arr2)==1:
        link = path+"\\"+i+'\\'+arr2[0]
        arr3 = os.listdir(link)
        arr2 = arr3
    print(i)
    print(arr2)
    # input('')
    for numberer,img in enumerate(arr2):
        if img[-4:] != '.png' and img[-4:] != '.jpg':
            print(img)
            input('@@')
            continue
        cnt2+=2
        old_name=link+'\\'+img
        new_name=newpath+'\\'+str(cnt2)+'.png'
        shutil.move(old_name, new_name)
        print(new_name)

    print(cnt)
    cnt+=1

# os.rename(r'file path\OLD file name.file type',r'file path\NEW file name.file type')


#v66
#v70,1,2,47