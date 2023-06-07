#testing git
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv

file = open("collegeswithmajor.csv", "w")
writer = csv.writer(file)
writer.writerow(["Name","Major"])

with open('collegeswithlink.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    c=0
    for row in reader_obj:
        if c==0:
            c=c+1
            continue
        name=row[0]
        link=row[1]
        html = requests.get(link)
        soup = BeautifulSoup(html.text, "html.parser")
        # html_div=soup.find(".callout")
        # print(html_div)
        # cnt=soup.findAll('dt',attrs={'class':None})
        # for c in cnt:
        #     if "Majors" in c.text:
        #         c=soup.select('dd')
        #         print(c)
        cnt=soup.select('dt')


        for c in cnt:
            if "Majors" in c.text:
                l=c.text
                # if(l=="Majors "):
                #     continue
                l=l.replace(" \t ","")
                l=l.split("\n   ")
                # if len(l)==0:
                #     continue
                l=l[1:]
                if len(l)==0:
                    continue
                l[-1]=l[-1].replace("\n\t  ","")
                l=sorted([*set(l)])
                print(l)
                for major in l:
                    writer.writerow([name, major])

        
        


