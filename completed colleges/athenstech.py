from bs4 import BeautifulSoup
import requests
import csv

def namechange(name):
	link=name.replace(" - ","-")
	link = link.replace(" -- ", "-")
	link = link.replace("- ", "-")
	link = link.replace(", ", "-")
	link = link.replace("/", "-")
	link =link.replace(" ", "-")
	link="https://athenstech.smartcatalogiq.com/2022-2023/Catalog/Courses/"+link
	if "AUMF" in link:
		link = "https://athenstech.smartcatalogiq.com/2022-2023/Catalog/Courses/AUMF-Automated-Manufacturing"
	if "EMET" in link:
		link = "https://athenstech.smartcatalogiq.com/2022-2023/Catalog/Courses/EMET-Electromechanical-and-Manufacturing-Engineering-Technology"
	if "EMSP" in link:
		link = "https://athenstech.smartcatalogiq.com/2022-2023/Catalog/Courses/EMSP-Emergency-Medical-Technician-Paramedic-Technology"
	if "FSSE" in link:
		link = "https://athenstech.smartcatalogiq.com/2022-2023/Catalog/Courses/First-Semester-Seminar"
	if "GIFS" in link:
		link = "https://athenstech.smartcatalogiq.com/2022-2023/Catalog/Courses/Geographic-Information-Systems"
	if "HACE" in link:
		link = "https://athenstech.smartcatalogiq.com/2022-2023/Catalog/Courses/HACE"
	if "HIMT" in link:
		link = "https://athenstech.smartcatalogiq.com/2022-2023/Catalog/Courses/HIMT-Health-Information-Technology"
	if "METR" in link:
		link = "https://athenstech.smartcatalogiq.com/2022-2023/Catalog/Courses/Metrology"
	if "MKTG" in link:
		link = "https://athenstech.smartcatalogiq.com/2022-2023/Catalog/Courses/MKTG-Marketing"
	if "MRIM" in link:
		link = "https://athenstech.smartcatalogiq.com/2022-2023/Catalog/Courses/MRIM-Magnetic-Resonance-Imaging-Specialist"
	if "PHTA" in link:
		link = "https://athenstech.smartcatalogiq.com/2022-2023/Catalog/Courses/PHTA-Physical-Therapist-Assist"
	if "THEA" in link:
		link = "https://athenstech.smartcatalogiq.com/2022-2023/Catalog/Courses/Syllabi"
	r = requests.get(link)
	if r.status_code != 404:
		return link
	else:
		return None


url = "https://athenstech.smartcatalogiq.com/2022-2023/Catalog/Courses"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
majors = soup.findAll("a", attrs={"class":None}, href=True)


for major in majors:
	if "General Catalog" in major.text or "Catalog 2022-2023" in major.text:
		continue
	if "-" in major.text:
		print('---------------------------------')
		print(major.text)
		newurl = namechange(major.text)
		newhtml = requests.get(newurl)
		newsoup = BeautifulSoup(newhtml.text, "html.parser")
		classes = newsoup.findAll("a", attrs={"class":None}, href=True)
		for classy in classes:
			if "General Catalog" in classy.text or "Catalog 2022-2023" in classy.text:
				continue
			if ("0" in classy.text or "1" in classy.text or "2" in classy.text) and len(classy.text) > 5:
				print(classy.text)
		if major.text == "WELD - Welding Technology":
			break