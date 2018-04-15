import bs4
import requests
from requests import get
from bs4 import BeautifulSoup

#url='https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/'

url=[]
url.append('https://www.amazon.com/gp/bestsellers/books?ie=UTF8&pg=1')
url.append('https://www.amazon.com/gp/bestsellers/books?ie=UTF8&pg=2')
url.append('https://www.amazon.com/gp/bestsellers/books?ie=UTF8&pg=3')
url.append('https://www.amazon.com/gp/bestsellers/books?ie=UTF8&pg=4')
url.append('https://www.amazon.com/gp/bestsellers/books?ie=UTF8&pg=5')



#urlresponse = get(url)
#Page = urlresponse.text
#GonnaParse = BeautifulSoup(Page, "html.parser")
#containers = GonnaParse.findAll("div",{"class":"zg_itemImmersion"})

filename= "./output/com_book.csv"
fileche = open(filename,"w")

HeaderName = "Name ; URL ;   Author ; Price ; Number of Ratings ; Average Rating"
fileche.write(HeaderName + "\n")
for j in url:
	urlresponse = get(j)
	Page = urlresponse.text
	GonnaParse = BeautifulSoup(Page, "html.parser")
	containers = GonnaParse.findAll("div",{"class":"zg_itemImmersion"})
	
	for i in range(20):
		TitleName = containers[i].a.div.img["alt"]
		lol=containers[i].findAll("span",{"class":"p13n-sc-price"})
		if lol:
			price=lol[0].text
		else:
			price="Not Available"
	
		Author = containers[i].findAll("span",{"class":"a-size-small a-color-base"})
		Author2= containers[i].findAll("a",{"class":"a-size-small a-link-child"})
		if Author:
			Authorprint=Author[0].text
		elif Author2:
			Authorprint = Author2[0].text
		else:
			Authorprint = "Not Available"

		star=containers[i].findAll("i",{"class":"a-icon"})
		if star:
			Starprint=star[0].span.text
			if Starprint=='Prime':
				Starprint="Not Available"
		else:
			Starprint="Not Available"
	
		rating=containers[i].findAll("a",{"class":"a-size-small a-link-normal"})
		if rating:
			ratingprint = rating[0].text
		else:
			ratingprint = "Not Available"

		url=containers[i].findAll("a",{"class":"a-link-normal a-text-normal"})
		urlprint="https://www.amazon.com" + url[0]["href"]
	
		fileche.write(TitleName.replace(","," ") + ";" + urlprint.replace(","," ") + ";" + Authorprint + ";" + price.replace(",","") + ";" + ratingprint.replace(",","") + ";" + Starprint + "\n")
