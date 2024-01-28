import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

###BeautifulSoup is a Python package for parsing HTML & XML documents. It will create a parse tree for parsed pages
###Requests library is one of the integral part of Python for making HTTP requests to a specified URL
for i in range(2,3):
  url="https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

  r= requests.get(url)
  #print(r)  ##we can see the total url's which we want to pass in it


  soup=BeautifulSoup(r.text, "lxml")
  box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")
  ##
  names = soup.find_all("div",class_ = "_4rR01T")
  for i in names:
      name = i.text
      Product_name.append(name)
  #print(Product_name)  ##It will print the names of the product which contain in the selected box

  ##
  prices = box.find_all("div",class_ = "_30jeq3 _1_WHN1")

  for i in prices:
     name = i.text
     Prices.append(name)
  #print(Prices)  

  ##
  desc = box.find_all("ul",class_ = "_1xgFaf")
  for i in desc:
     name = i.text
     Description.append(name)
  #print(Description)

  ##
  reviews = box.find_all("div",class_ = "_3LWZlK")
  for i in reviews:
     name = i.text
     Reviews.append(name)

  #print(Reviews)

data_frame = pd.DataFrame({"Product Name":Product_name,"Prices":Prices,"Description":Description,"Reviews":Reviews})
#print(data_frame)  #Now the data will be stored into the data frame


data_frame.to_csv("C:/Users/rames/Desktop/Python/flipkart_mobiles_under_50k.csv") #Location of the excel where we have to keep
print("done") ##Finally after this print we will get the csv file into the given location


