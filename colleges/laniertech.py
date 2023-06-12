from bs4 import BeautifulSoup
import requests
import csv


def namechange(name):
	link = name.replace(" & ", "-")
	link = link.replace(" - ","-")
	link = link.replace("- ", "-")
	link = link.replace("/", "-")
	link = link.replace(".", "")
	link = link.replace(" ", "-").lower()
	link="https://iq3.smartcatalogiq.com/Catalogs/Lanier-Technical-College/2022-2023/Catalog/Course-Descriptions/"+link
	r = requests.get(link)
	if r.status_code != 404:
		return link
	else:
		return None



url = "https://iq3.smartcatalogiq.com/Catalogs/Lanier-Technical-College/2022-2023/Catalog/Course-Descriptions"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
majors = soup.findAll("a", attrs={"class":None}, href=True)

count = 0
for major in majors:
	if major.text == "Print this page" or count > 0:
		count += 1
		if major.text != "Print this page":
			print('---------------------------------')
			print(major.text)
			name = namechange(major.text)
			print(name)
			newhtml = requests.get(name)
			newsoup = BeautifulSoup(newhtml.text, "html.parser")
			classes = newsoup.findall("a", attrs={"class":None}, href=True)
			for classy in classes:
				print(classy.text)
	if major.text != "Print this page":
		continue
