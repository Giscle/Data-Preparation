from lxml import etree
import os, sys
#direc=os.listdir('C:\Users\SAURADIP\Desktop\GISCLE\windows_v1.5.2\dataset\Night Part 2\Sandeep\combine\testing')
image_directory = os.getcwd()
arr = os.listdir(os.path.join(image_directory,'combine'))
count=0
# Removes any Unannotated Image 

for file in arr:
    if file.endswith(".jpg"):
        string=file.split('.jpg' , 0)[0]
        org=string.split('.')[0]
        im=str(org)+'.xml'
        im1=str(org)+'.jpg'
        #if not os.path.isfile(os.path.join('C:\Users\SAURADIP\Desktop\GISCLE\windows_v1.5.2\dataset\Night Part 2\Sandeep\combine\\testing',im)):
        if not os.path.isfile(os.path.join(os.path.join(image_directory,'combine'),im)):
            os.remove(os.path.join(os.path.join(image_directory,'combine'),im1))
            count=count+1
print (str(count) +' '+  'Duplicates Images Removed')
count1=0
for file in arr:
    if file.endswith(".xml"):
        string=file.split('.xml' , 0)[0]
        org=string.split('.')[0]
        im=str(org)+'.xml'
        im1=str(org)+'.jpg'
        #if not os.path.isfile(os.path.join('C:\Users\SAURADIP\Desktop\GISCLE\windows_v1.5.2\dataset\Night Part 2\Sandeep\combine\\testing',im1)):
        if not os.path.isfile(os.path.join(os.path.join(image_directory,'combine'),im1)):
            os.remove(os.path.join(os.path.join(image_directory,'combine'),im))
            count1=count1+1
print (str(count1) +' '+  'Duplicates XML Removed')

