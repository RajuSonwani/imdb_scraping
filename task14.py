import os,json,requests,time,random,task1,task12,task13
from bs4 import BeautifulSoup
from pprint import pprint

def analyse_co_actors(moviesDtl_Lst):
	dicL={}
	lst0=[]
	for dic in moviesDtl_Lst:
		count0=0
		for dic0 in dic["cast"]:
			if count0==5:
				break
			elif dic0["imdb_id"] not in dicL:
				count0+=1
				dicL[dic0["imdb_id"]]={}
				dicL[dic0["imdb_id"]]["name"]=dic0["name"]
				dicL[dic0["imdb_id"]]["frequent_co_actors"]=lst0.copy()
				# movieNo=0
				for x in moviesDtl_Lst:
					for y in x["cast"]:
						if y["imdb_id"]==dic0["imdb_id"]:
							count1=0
							# movieNo+=1
							for dic00 in x["cast"]:
								if dic00["imdb_id"]!=dic0["imdb_id"] and count1<4:
									count1+=1
									dicT={}
									dicT["imdb_id"]=dic00["imdb_id"]
									dicT["name"]=dic00["name"]
									# dicT["movies_num"]=movieNo
									dicL[dic0["imdb_id"]]["frequent_co_actors"].append(dicT)
							break


	return dicL


moviesLst=task1.top_250movies()
cast=task12.movie_Cast(moviesLst)
Lst=task13.movie_detailsLst(moviesLst,cast)

pprint(analyse_co_actors(Lst))