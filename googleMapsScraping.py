import googlemaps
import pprint
import urllib.request, json
from bs4 import BeautifulSoup
import os
import lxml 
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options 
import time


path = r"D:/selenium drivers"
chrome_options = Options()
chrome_options.add_argument("--headless")
os.environ['PATH'] += path
driver = webdriver.Chrome(os.path.join(path,'chromedriver.exe'),options=chrome_options)




driver = webdriver.Chrome()


api_key=open('API.txt').read()
def getDetails():
    shop_name=input("Enter what do you want to search : ")
    shop_name=shop_name.replace(' ','+')
    with urllib.request.urlopen("https://maps.googleapis.com/maps/api/place/textsearch/json?query="+shop_name+"&key="+api_key) as url:
        data = json.load(url)
        for d in data['results']:
            try:
                print(d['name'])
                url = 'https://google.com/search?q='+str(d['name'])
                driver.get(url)
                html=driver.page_source
                soup = BeautifulSoup(html , 'html.parser')
                div=soup.find("div",{"class":"I6TXqe"})
                
                maindiv=BeautifulSoup(str(div),'lxml')
                link=maindiv.find('a',{'class':'ab_button'})
                ratings=maindiv.find('span',{'class':'Aq14fc'})
                address=maindiv.find('span',{'class':'LrzXr'})
                hours=maindiv.find('span',{'class':'TLou0b'})
                phone=maindiv.find('span',{'class':'LrzXr zdqRlf kno-fv'})
                des=maindiv.find('span',{'class':'Yy0acb'})
                
                with open(shop_name+".txt","a") as f:
                    print("place : "+str(d['name']))
                    f.write("place : "+str(d['name'])+"\n")
                    print("link : "+link['href'])
                    f.write("link : "+link['href']+"\n")
                    print("ratings : "+ratings.text)
                    f.write("ratings : "+ratings.text+"\n")
                    print("address : "+address.text)
                    f.write("address : "+address.text+"\n")
                    print("hours : "+hours.text)
                    f.write("hours : "+hours.text+"\n")
                    print("phone : "+phone.text)
                    f.write("phone : "+phone.text+"\n")
                    print("description : "+des.text)
                    f.write("description : "+des.text+"\n")
                    print("place id : "+d['place_id'])
                    f.write("place id : "+d['place_id']+"\n")
                    f.write("\n")
                    print()
            except:
                continue
        if 'next_page_token' in data:
            getDetails2(shop_name,data['next_page_token'])
            
            
def getDetails2(shop_name,nexPageToken):
    with urllib.request.urlopen("https://maps.googleapis.com/maps/api/place/textsearch/json?query="+shop_name+"&key="+api_key+"&pagetoken="+nexPageToken) as url:
        data = json.load(url)
        for d in data['results']:
            try:
                print(d['name'])
                
                url = 'https://google.com/search?q='+str(d['name'])
                driver.get(url)
                html=driver.page_source
                soup = BeautifulSoup(html , 'html.parser')
                div=soup.find("div",{"class":"I6TXqe"})
                
                maindiv=BeautifulSoup(str(div),'lxml')
                link=maindiv.find('a',{'class':'ab_button'})
                ratings=maindiv.find('span',{'class':'Aq14fc'})
                address=maindiv.find('span',{'class':'LrzXr'})
                hours=maindiv.find('span',{'class':'TLou0b'})
                phone=maindiv.find('span',{'class':'LrzXr zdqRlf kno-fv'})
                des=maindiv.find('span',{'class':'Yy0acb'})
                
                with open(shop_name+".txt","a") as f:
                    print("place : "+str(d['name']))
                    f.write("place : "+str(d['name'])+"\n")
                    print("link : "+link['href'])
                    f.write("link : "+link['href']+"\n")
                    print("ratings : "+ratings.text)
                    f.write("ratings : "+ratings.text+"\n")
                    print("address : "+address.text)
                    f.write("address : "+address.text+"\n")
                    print("hours : "+hours.text)
                    f.write("hours : "+hours.text+"\n")
                    print("phone : "+phone.text)
                    f.write("phone : "+phone.text+"\n")
                    print("description : "+des.text)
                    f.write("description : "+des.text+"\n")
                    print("place id : "+d['place_id'])
                    f.write("place id : "+d['place_id']+"\n")
                    f.write("\n")
                
                    print()
            except:
                continue
        if 'next_page_token' in data:
            getDetails2(shop_name,data['next_page_token'])


getDetails()



