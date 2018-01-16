from lxml import etree
import os, sys
arr = os.listdir('C:\Users\SAURADIP\Desktop\GISCLE\windows_v1.5.2\dataset\Night Part 2\Sandeep\Annotated')
# converts any mistyped label names using LabelImg Software
for files in arr:
    if str(files) != 'rename.py':
        tree = etree.parse(str(files))
        root = tree.getroot()
        #print str(files)
        for child in root.findall('object'):
                   ob=child.find('name')
                   ob.text=str(ob.text.lower())
                   #print ob.text
                   tree.write(str(files))         
print ('Renaming Complete')
