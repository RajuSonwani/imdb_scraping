import os,json,requests,time,random
from bs4 import BeautifulSoup
from pprint import pprint

# url='https://www.jiosaavn.com/featured/sawan-savan-saawan-saavan/jORiC1Lxp3Q_'
# page=requests.get(url)
# soup=BeautifulSoup(page.text,"html.parser")
# # print(soup)
# div = soup.find('div',class_='infinite-scroll-component__outerdiv')
# ol=div.find('ol',class_="o-list-bare u-margin-bottom-none@sm")
# print(ol.text)




if os.path.exists("/home/navgurukul/Desktop/rAju/data/savan.json"):
	with open("/home/navgurukul/Desktop/rAju/data/savan.json",) as file:
		page=BeautifulSoup(file.read(),"html.parser")
		ol=page.find("ol",class_="o-list-bare u-margin-bottom-none@sm")
		all_li=ol.find_all("li",class_="")
		finaldic={}
		song=0
		for i in all_li:
			song+=1
			lst0=[]
			img=i.find("div",class_="o-flag__img").img["src"]
			figCaption=i.find("figcaption",class_="o-flag__body")
			a_all=figCaption.find_all("a")
			for i in range(len(a_all)):
				dic={}
				if i==0:
					songname=a_all[i].text
					songlink=a_all[i]["href"]
					dic["songname"]=a_all[i].text
					dic["songlink"]="https://www.jiosaavn.com"+a_all[i]["href"]
				elif i==1:
					singername0=a_all[i].text
					singerlink0=a_all[i]["href"]
					dic["singername0"]=a_all[i].text
					dic["singerlink0"]="https://www.jiosaavn.com"+a_all[i]["href"]
				elif i==2:
					singername00=a_all[i].text
					singerlink00=a_all[i]["href"]
					dic["singername00"]=a_all[i].text
					dic["singerlink00"]="https://www.jiosaavn.com"+a_all[i]["href"]
				else:
					break	
				
				lst0.append(dic)
			finaldic[song]=lst0

		pprint(finaldic)
		# with open("/home/navgurukul/Desktop/rAju/data/savanData.json","w") as file:
		# 	file.write(json.dumps(finaldic))





else:
	page=requests.get("https://www.jiosaavn.com/featured/weekly-top-songs/8MT-LQlP35c_")
	with open("/home/navgurukul/Desktop/rAju/data/savan.json","w") as file:
		file.write(page.text)

