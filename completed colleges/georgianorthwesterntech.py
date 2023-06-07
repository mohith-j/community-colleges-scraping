from bs4 import BeautifulSoup
import requests
import csv

def namechange(name):
	link = name.replace(" - ","-")
	link = link.replace("- ", "-")
	link = link.replace("/", "-")
	link = link.replace(" ", "-").lower()
	link = "https://gntc.smartcatalogiq.com/en/2023-2024/semester-catalog/course-descriptions/"+link+"/"
	if "busn" in link:
		link = "https://gntc.smartcatalogiq.com/en/2023-2024/semester-catalog/course-descriptions/busn-business-administrative-techno/"
	if "flpd" in link:
		link = "https://gntc.smartcatalogiq.com/en/2023-2024/semester-catalog/course-descriptions/flpd-flooring-production/"
	if "lact" in link:
		link = "https://gntc.smartcatalogiq.com/en/2023-2024/semester-catalog/course-descriptions/lact-lactation/"
	if "ped" in link:
		link = "https://gntc.smartcatalogiq.com/en/2023-2024/semester-catalog/course-descriptions/peds-pediatric-echocardiography/"
	r = requests.get(link)
	if r.status_code != 404:
		return link
	else:
		return None


url = "https://gntc.smartcatalogiq.com/en/2023-2024/semester-catalog/course-descriptions/"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
majors = soup.findAll("a", attrs={"class":None}, href=True)


for major in majors:
	if "General Catalog" in major.text or "2023-2024 Catalog" in major.text or "Programs of Study" in major.text or "Programs-of-Study" in major.text:
		continue
	if "-" in major.text:
		print('---------------------------------')
		print(major.text)
		newurl = namechange(major.text)
		newhtml = requests.get(newurl)
		newsoup = BeautifulSoup(newhtml.text, "html.parser")
		classes = newsoup.findAll("a", attrs={"class":None}, href=True)
		for classy in classes:
			if "General Catalog" in classy.text or "2023-2024 Catalog" in classy.text or "Programs Available 100% Online" in classy.text:
				continue
			if ("0" in classy.text or "1" in classy.text or "2" in classy.text) and len(classy.text) > 5:
				print(classy.text)
		if "Welding" in major.text:
			break

