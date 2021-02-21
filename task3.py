import requests,os,json
from bs4 import BeautifulSoup
from pprint import pprint
import task1


# def movies_by_decade(movies):
# 	decadeMovies={}
# 	count=0
# 	lst=[1950,1960,1970,1980,1990,2000,2010,2020,2021]
# 	for i in range(len(lst)-1):
# 		x=[]
# 		for m in movies:
# 			if m["year"]>=lst[i] and m["year"]<lst[i+1]:
# 				x.append(m)
# 				count+=1
# 		decadeMovies[lst[i]]=x
# 	return decadeMovies
# 	# return count
# x=task1.top_250movies()
# pprint(movies_by_decade(x))


	# or


# def movies_by_decade(lst):
# 	decadeMovies={}
# 	lst0=[]
# 	for dic in lst:
# 		r=dic["year"]%10
# 		decade=dic["year"]-r
# 		if decade not in lst:
# 			lst0.append(decade)
	 
# 	for i in lst0:
# 		x=[]
# 		for m in lst:
# 			if m["year"]>=i and m["year"]<=i+9:
# 				x.append(m)
				
# 		decadeMovies[i]=x
# 	return decadeMovies

# x=task1.top_250movies()
# pprint(movies_by_decade(x))


# or
# another solution


import task2,task1
def movies_by_decade(mvs):
	lst=[]
	for n in mvs:
		r=n%10
		decade=n-r
		if decade not in lst:
			lst.append(decade)

	decadeMovies={}
	for i in lst:
		x=[]
		for m in mvs:
			if m >=i and m <=i+9:
				for n in mvs[m]:
					x.append(n)
		decadeMovies[i]=x
	return decadeMovies

pprint(movies_by_decade(mvs))

# z=task1.top_250movies()
# x=task2.movies_by_year(z)
# pprint(movies_by_decade(x))