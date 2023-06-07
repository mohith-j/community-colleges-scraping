from bs4 import BeautifulSoup
import requests
import csv

def namechange(name):
	link = name.replace(" - ","-")
	link = link.replace("- ", "-")
	link = link.replace("/", "-")
	link = link.replace(" ", "-").lower()
	link="https://savannahtech.smartcatalogiq.com/en/current/academic-catalog/courses/"+link+"/"
	r = requests.get(link)
	if r.status_code != 404:
		return link
	else:
		return None


url = "https://savannahtech.smartcatalogiq.com/en/current/academic-catalog/courses/"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
majors = soup.findAll("a", attrs={"class":None}, href=True)


for major in majors:
	if "General Catalog" in major.text or "2022-2023 Academic Calendar" in major.text or "Statement of Equal Opportunity Non-Discrimination Policy" in major.text:
		continue
	if "-" in major.text:
		print('---------------------------------')
		print(major.text)
		newurl = namechange(major.text)
		newhtml = requests.get(newurl)
		newsoup = BeautifulSoup(newhtml.text, "html.parser")
		classes = newsoup.findAll("a", attrs={"class":None}, href=True)
		for classy in classes:
			if "General Catalog" in classy.text or "2022-2023 Academic Calendar" in classy.text:
				continue
			if ("0" in classy.text or "1" in classy.text or "2" in classy.text) and len(classy.text) > 5:
				print(classy.text)
		if "Welding" in major.text:
			break
