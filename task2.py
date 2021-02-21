import requests,os,json
from bs4 import BeautifulSoup
from pprint import pprint
import task1

def movies_by_year(x):
	yearly_movies={}
	year=[]
	for i in x:
		if i["year"] not in year:
			year.append(i["year"])
	# for m in year:
	# 	lst=[]
	# 	for n in x:
	# 		if n["year"]==m:
	# 			lst.append(n)
	# 	yearly_movies[m]=lst
	
	# return yearly_movies
	
	s={i:[]for i in year}
	for i in s:
		# print()
		# break
		for m in x:
			if m["year"]==i:
				s[i].append(m)
				
	pprint(s)


# z=task1.top_250movies()
# pprint(movies_by_year(z))