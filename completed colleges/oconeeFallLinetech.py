from bs4 import BeautifulSoup
import requests
import csv

url = "https://oftc.smartcatalogiq.com/en/2022-2023/ay23-academic-catalog-handbook/courses/"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
classes = soup.findAll("a", attrs={"class":None}, href=True)

count = 0
currmjr = ""
for classy in classes:
    if "XXXX XXXX" in classy.text or "  Choose 3 or more credit hours:" in classy.text:
        continue
    if "0" in classy.text or "1" in classy.text or "2" in classy.text or "3" in classy.text:
        if currmjr != classy.text[0:4]:
            print('---------------------------------')
            print(classy.text[0:4])
        currmjr = classy.text[0:4]
        print(classy.text)

