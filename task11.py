
import os,json,requests,time,random,task1,task8
from bs4 import BeautifulSoup
from pprint import pprint

def movie_byGenre(movieLst):
	dicFinal={}
	for movieDic in movieLst:
		for genre in movieDic["genre"]:
			if genre not in dicFinal:
				dicFinal[genre]=1
			else:
				dicFinal[genre]+=1
	return dicFinal



movies_list=task1.top_250movies()
movieLst=task8.movie_detailsLst(movies_list)
pprint(movie_byGenre(movieLst[:5]))