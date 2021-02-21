import os,json,requests,time,random,task1
from bs4 import BeautifulSoup
from pprint import pprint

def movie_Cast(moviesLst):
	finalDict={}
	for movieDic in moviesLst:
		link=movieDic["link"]
		movieId=link[-10:-1]
		# print(movieId)
		# a=https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast
		
		if os.path.exists("/home/navgurukul/Desktop/rAju/data/castData/"+movieId+"_cast.json"):
			with open("/home/navgurukul/Desktop/rAju/data/castData/"+movieId+"_cast.json") as file:
				data=json.loads(file.read())
			finalDict[movieId]=data
		else:
			time.sleep(random.randint(1,5))
			page=requests.get(link+"fullcredits?ref_=tt_cl_sm#cast").text
			page0=BeautifulSoup(page,"html.parser")
			castLst=page0.find("table",class_="cast_list")
			all_td=castLst.find_all("td",class_="")
			finalLst=[]
			for td in all_td:
				dic={}
				dic["imdb_id"]=td.a["href"][-10:-1]
				dic["name"]=td.text.strip()

				finalLst.append(dic)
			with open("/home/navgurukul/Desktop/rAju/data/castData/"+movieId+"_cast.json","w") as file:
				file.write(json.dumps(finalLst))
			finalDict[movieId]=finalLst

	return finalDict


# moviesLst=task1.top_250movies()
# pprint(movie_Cast(moviesLst))