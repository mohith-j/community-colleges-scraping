from bs4 import BeautifulSoup
import requests
import csv

def get_classes(name, link):
    html=requests.get(link)
    soup=BeautifulSoup(html.text, "html.parser")
    classes=soup.findAll("li", attrs={"class":None})
    print("Program Name:"+name)
    for clas in classes:
        print(clas.text)
        # insert writing spreadsheet code here

url = "https://www.gwinnettcollege.edu/locations/lilburn/"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
div = soup.find("div", attrs={"class":"entry-content"})
majors=div.findAll("a", attrs={"class":None})
for major in majors:
    # print(major["href"])
    # print(major.text)
    get_classes(major.text, major["href"])
