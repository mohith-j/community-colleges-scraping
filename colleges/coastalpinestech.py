from bs4 import BeautifulSoup
import requests
import csv

def namechange(name):
	link=name.replace(" - ","-")
	link = link.replace("- ", "-")
	link = link.replace("/", "-")
	link =link.replace(" ", "-")
	link="https://catalog.coastalpines.edu/classes/"+link
	r = requests.get(link)
	if r.status_code != 404:
		return link
	else:
		return None


url = "https://catalog.coastalpines.edu/classes"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
majors = soup.findAll("div", attrs={"class":"field field--name-field-class-program field--type-entity-reference field--label-hidden field__item"})
classname = soup.findAll("span", attrs={"class": "field field--name-field-item field--type-string field--label-hidden field__item"})

for major in majors:
	if "Program" in major.text or "Course" in major.text:
		continue
	print('---------------------------------')
	print(major.text)
	for classy in classname:
		print(classy.text)