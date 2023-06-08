from bs4 import BeautifulSoup
import requests
import csv

def namechange(name):
	link=name.replace(" - ","-")
	link = link.replace("- ", "-")
	link = link.replace("/", "-")
	link =link.replace(" ", "-")
	link="https://www.southgatech.edu/programs/"+link
	r = requests.get(link)
	if r.status_code != 404:
		return link
	else:
		return None


url = "https://www.southgatech.edu/academics/all-programs/"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
majors = soup.findAll("a", attrs={"class":None}, href=True)

print(len(majors))
for major in majors:
	print('---------------------------------')
	print(major.text)



