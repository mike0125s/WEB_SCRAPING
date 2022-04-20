
import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.giiresearch.com/material_report.shtml"

page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('table',class_='plist_item')

with open('BookShop.csv','w',encoding='utf8',newline='') as f:
    thewriter = writer(f)
    header = ['title','Published_By','Product_Code','Published_Date','Content_Info','Price']
    thewriter.writerow(header)
    for list in lists:
    
       title = list.find('div',class_='list_title').text.replace('\n','')
       Published_By = list.find('div',class_='plist_pubinfo').text.replace('\n','')
       Product_Code = list.find('div',class_='plist_codeinfo').text.replace('\n','')
       Published_Date = list.find('div',class_='plist_dateinfo').text.replace('\n','')
       Content_Info = list.find('div',class_='plist_pageinfo').text.replace('\n','')
       Price = list.find('span',class_='price_usd').text.replace('\n','')
       info=[title,Published_By,Product_Code,Published_Date,Content_Info,Price]
       thewriter.writerow(info)