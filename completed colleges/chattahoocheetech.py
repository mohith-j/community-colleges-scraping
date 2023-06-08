from bs4 import BeautifulSoup
import requests
import csv

def namechange(name):
	link=name.replace(" - ","-")
	link = link.replace("- ", "-")
	link = link.replace("/", "-")
	link =link.replace(" ", "-")
	link="https://chattahoocheetech.smartcatalogiq.com/en/2022-2023/General-Catalog/Courses/"+link
	if "CMTT" in name:
		link="https://chattahoocheetech.smartcatalogiq.com/2022-2023/General-Catalog/Courses/CMMT"
	if "DMPT" in name:
		link = "https://chattahoocheetech.smartcatalogiq.com/2022-2023/General-Catalog/Courses/DMPT-Design-and-Media-Production"
	if "ELUT" in name:
		link = "https://chattahoocheetech.smartcatalogiq.com/2022-2023/General-Catalog/Courses/ELUT"
	r = requests.get(link)
	if r.status_code != 404:
		return link
	else:
		return None


url = "https://chattahoocheetech.smartcatalogiq.com/en/2022-2023/General-Catalog/Courses"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
majors = soup.findAll("a", attrs={"class":None}, href=True)


for major in majors:
	if "General Catalog" in major.text:
		continue
	if "-" in major.text:
		print('---------------------------------')
		print(major.text)
		newurl = namechange(major.text)
		newhtml = requests.get(newurl)
		newsoup = BeautifulSoup(newhtml.text, "html.parser")
		classes = newsoup.findAll("a", attrs={"class":None}, href=True)
		for classy in classes:
			if "General Catalog" in classy.text:
				continue
			if ("0" in classy.text or "1" in classy.text or "2" in classy.text) and len(classy.text) > 5:
				print(classy.text)
		if "Welding" in major.text:
			break
