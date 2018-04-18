"""
// paste this script into the chrome console, and then download the urls using the python script below
var cont=document.getElementsByTagName("body")[0];
var imgs=document.getElementsByTagName("a");
var i=0;var divv= document.createElement("div");
var aray=new Array();var j=-1;
while(++i<imgs.length){
    if(imgs[i].href.indexOf("/imgres?imgurl=http")>0){
      divv.appendChild(document.createElement("br"));
      aray[++j]=decodeURIComponent(imgs[i].href).split(/=|%|&/)[1].split("?imgref")[0];
      divv.appendChild(document.createTextNode(aray[j]));
    }
 }
cont.insertBefore(divv,cont.childNodes[0]);
"""


import requests

f = open("images_urls")
content = f.read()
urls = content.split("<br>")


def write_to_file(url, path):
    with open(path, 'wb') as f:
        f.write(requests.get(url).content)

i = 1
for url in urls:
	if len(url) == 0:
		continue
	print(url)
	write_to_file(url, "downloads/" + str(i) + ".jpg")
	i += 1
