# -*- coding: utf-8 -*-
"""data crowling 3 (working) .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wcTdElaA1VE5wXDTofX9BlUyyg8ncTW_

# Let us try to understand this piece of code.

First of all import the requests library.
Then, specify the URL of the webpage you want to scrape.
Send a HTTP request to the specified URL and save the response from server in a response object called r.
Now, as print r.content to get the raw HTML content of the webpage. It is of ‘string’ type.
"""

#Install working file
#!pip install requests
#!pip install BeautifulSoup
#!pip install bs4

import requests 
URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL) 
print(r.content)

"""# Step 3: Parsing the HTML content
We create a BeautifulSoup object by passing two arguments:

r.content : It is the raw HTML content.

html5lib : Specifying the HTML parser we want to use.

Now soup.prettify() is printed, it gives the visual representation of the parse tree created from the raw HTML content.
"""

#This will not run on online IDE 
import requests 
from bs4 import BeautifulSoup 
  
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content,'html5lib') 
print(soup.prettify())

"""# Step 4: Searching and navigating through the parse tree"""



#Python program to scrape website  
#and save quotes from website 

import requests 
from bs4 import BeautifulSoup 
import csv 
 
URL = "https://www.passiton.com/inspirational-quotes"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 
  
quotes=[]  # a list to store quotes 

  
table = soup.find('div', attrs = {'id':'container'}) 
  
for row in soup.find_all('div', attrs = {'class':'quote'}): 
    quote = {} 
    quote['theme'] = row.h5.text 
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['src'] 
    quote['lines'] = row.h6.text 
    quote['author'] = row.p.text 
    quotes.append(quote) 
  
filename = 'inspirational_quotes.csv'
with open(filename, 'wb') as f: 
    w = csv.DictWriter(f,['theme','url','img','lines','author']) 
    w.writeheader() 
    for quote in quotes: 
        w.writerow(quote)

import pandas as pd
data =  pd.read_csv('inspirational_quotes.csv')

data.head()