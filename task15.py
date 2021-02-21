import os,json,requests,time,random,task1,task12,task13
from bs4 import BeautifulSoup
from pprint import pprint

def count_movies(moviesLst):
	dicT={}
	for dic in moviesLst:
		for dic0 in dic["cast"]:
			if dic0["imdb_id"] not in dicT:
				dicT[dic0["imdb_id"]]={}
				count=0
				for x in moviesLst:
					for y in x["cast"]:
						if y["imdb_id"]==dic0["imdb_id"]:
							count+=1
							break
				dicT[dic0["imdb_id"]]["name"]=dic0["name"]
				dicT[dic0["imdb_id"]]["movies_did"]=count

	return dicT








moviesLst=task1.top_250movies()
cast=task12.movie_Cast(moviesLst)
Lst=task13.movie_detailsLst(moviesLst,cast)

pprint(count_movies(Lst))
