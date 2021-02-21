import requests,os,json
from bs4 import BeautifulSoup
from pprint import pprint
# response=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")

# soup = BeautifulSoup(response.text,'html.parser')
# tbody = soup.find('tbody',class_="lister-list")
# tr = tbody.find_all('tr')

# for i in tr:
# 	td = i.find('td',class_="titleColumn")
# 	a = td.find('a').text
# 	span = td.find('span',class_="secondaryInfo")
# 	print(a)
# 	print(span.text)
# 	Link0=td.find('a')['href']
# 	Link = 'https://www.imdb.com/'+Link0
# 	print(Link)
# 	strong = i.find('strong').text
# 	print(strong)
###################33
def top_250movies():
	if os.path.exists("/home/navgurukul/Desktop/rAju/data/top_250.json"):
		with open("/home/navgurukul/Desktop/rAju/data/top_250.json","r") as file:
			
			data=BeautifulSoup(file.read(),"html.parser")
			tbody=data.find("tbody",class_="lister-list")
			all_tr=tbody.find_all("tr")
			rank=1
			listFinal=[]
			for tr in all_tr:
				name=tr.find("td",class_="titleColumn").a.text
				# td_Column=tr.find("td",class_="titleColumn")
				# name=td_Column.find("a").text
				# year=td_Column.find("span",class_="secondaryInfo").text
				year=tr.find("td",class_="titleColumn").span.get_text()
				# link=td_Column.find("a")["href"]
				link=tr.find("td",class_="titleColumn").a["href"]
				# td_rating=tr.find("td",class_="ratingColumn imdbRating")
				# rating=td_rating.find("strong").text
				rating=tr.find("td",class_="ratingColumn imdbRating").strong.text
				dic={}
				lst=["rank","name","year","rating","link"]
				for i in lst:
					if i=="rank":
						dic[i]=rank
					elif i=="name":
						dic[i]=name
					elif i=="year":
						dic[i]=int(year[1:5])
					elif i=="rating":
						dic[i]=float(rating)
					else:
						dic[i]="https://www.imdb.com"+link
				listFinal.append(dic)
				rank+=1
			return listFinal

				
	else:
		dataGot=requests.get("https://www.imdb.com/india/top-rated-indian-movies/").text
		with open("/home/navgurukul/Desktop/rAju/data/top_250.json","w") as file:
			file.write(dataGot)

# pprint(top_250movies())
