from bs4 import BeautifulSoup
import requests,task1,task5,os
from pprint import pprint

def movies_by_director(moviesLst):
	movie_dict={}
	for dic in moviesLst:
		for direc in dic["director"]:
			if direc not in movie_dict:
				movie_dict[direc]=1
			else:
				movie_dict[direc]+=1
	return movie_dict



movies_list=task1.top_250movies()
x=task5.movie_detailsLst(movies_list)
pprint(movies_by_director(x))
