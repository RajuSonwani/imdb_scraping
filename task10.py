import os,json,time,requests,task1,task8
from bs4 import BeautifulSoup
from pprint import pprint

def movies_byDirector_language(moviesLst):
	mainDic={}
	for dic in moviesLst:
		subdic={}
		for direc in dic["director"]:
			if direc not in mainDic:
				mainDic[direc]=subdic.copy()
		
				for dic in moviesLst:
					for director in dic["director"]:
						if director ==direc:
							for lang in dic["language"]:
								if lang not in mainDic[direc]:
									mainDic[direc][lang]=1
								else:
									mainDic[direc][lang]+=1

	return mainDic

	# languages={}
	# for movie in moviesLst:
	# 	for lan in movie["language"]:
	# 		if lan not in languages:
	# 			languages[lan]=0

	# # pprint(moviesLst)
	# director_language={}

	# for movie in moviesLst:
	# 	for dirrec in movie["director"]:
	# 		if dirrec not in director_language:
	# 			director_language[dirrec]=languages.copy()
	

	# for direct in director_language:
	# 	for movie in moviesLst:
	# 		for di in movie["director"]:
	# 			if di == direct:
	# 				for la in movie["language"]:
	# 					for l in director_language[direct]:
	# 						if l==la:
	# 							director_language[direct][la]+=1

	# pprint(director_language)


movies_list=task1.top_250movies()
x=task8.movie_detailsLst(movies_list)
pprint(movies_byDirector_language(x))