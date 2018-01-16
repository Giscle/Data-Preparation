from lxml import etree
import os, sys
image_directory = os.getcwd()
arr = os.listdir(os.path.join(image_directory,'combine'))
count=0

for file in arr:
    if file.endswith(".jpg"):
        count=count+1

print(count)
count_n=1
for file in arr:
    if file.endswith(".jpg"):
        #print(file)
        string=file.split('.jpg' , 0)[0]
        org=string.split('.')[0]
        im=str(org)+'.xml'
        im1=str(org)+'.jpg'
        #print(im)
        new_xml='image_'+str(count_n)+'.xml'
        #print(im1)
        new_jpg='image_'+str(count_n)+'.jpg'
        count_n=count_n+1
        print(count_n)
        if os.path.isfile(os.path.join(os.path.join(image_directory,'combine'),im)) :
            try :
                print(im)
                print(new_xml)
                os.rename(os.path.join(os.path.join(image_directory,'combine'),im),os.path.join(os.path.join(image_directory,'combine'),new_xml))
                os.rename(os.path.join(os.path.join(image_directory,'combine'),im1),os.path.join(os.path.join(image_directory,'combine'),new_jpg))
                
            except WindowsError:
                print ( 'File already Renamed' )
           
print (str(count_n-1) +' '+  'File Names Changed')
