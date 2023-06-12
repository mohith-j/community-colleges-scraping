from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.wiregrass.edu/course-catalog/current/courses"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
classes = soup.findAll("div", attrs={"class":"page-title"})


for classy in classes:
    print(classy.text)