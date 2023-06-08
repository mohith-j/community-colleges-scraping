from bs4 import BeautifulSoup
import requests
import csv

def namechange(name):
	link=name.replace(" - ","-")
	link = link.replace("- ", "-")
	link = link.replace("/", "-")
	link =link.replace(" ", "-")
	link="https://atlantatech.smartcatalogiq.com/en/2022-2023/College-Catalog/Courses/"+link
	r = requests.get(link)
	if r.status_code != 404:
		return link
	else:
		return None


url = "https://atlantatech.smartcatalogiq.com/en/2022-2023/College-Catalog/Courses"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
majors = soup.findAll("a", attrs={"class":None}, href=True)

li = soup.findAll("li", attrs={"class":"hasChildren"})

for major in majors:
    print(major.text)
    for l in li:
        print(l.text)
    break

