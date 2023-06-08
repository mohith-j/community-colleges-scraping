from bs4 import BeautifulSoup
import requests
import csv


def namechange(name):
	link = name.replace(" - ", "-")
	link = link.replace("- ", "-")
	link = link.replace("/", "-")
	link = link.replace(" ", "-")
	link = "https://chattahoocheetech.smartcatalogiq.com/en/2022-2023/General-Catalog/Courses/"+link
	r = requests.get(link)
	if r.status_code != 404:
		return link
	else:
		return None


url = "https://www.aimm.edu/aimm-degrees"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
majors = soup.findAll("h2", attrs={"class": "course-post-title"})


for major in majors:
	print('---------------------------------')
	print(major.text)
	newurl = "https://www.aimm.edu/programs/degree/music-production-audio-for-media"
	newhtml = requests.get(newurl)
	newsoup = BeautifulSoup(newhtml.text, "html.parser")
	classes = newsoup.findAll("td", attrs={"class": None, "style": "width: 64.6562%; padding: 4px;"})
	for classy in classes:
		word = classy.text.strip("\n")
		print(word)
		if classy.text == "Location Sound I":
			break
	break


for major2 in majors:
	print('---------------------------------')
	print(major2.text)
	url2 = "https://www.aimm.edu/programs/degree/guitar"
	html2 = requests.get(url2)
	soup2 = BeautifulSoup(html2.text, "html.parser")
	classes2 = soup2.findAll("strong", attrs={"class": None})
	for classy2 in classes2:
		if classy2.text == "Program Total" or classy2.text == "Total" or classy2.text == "Elective Credits Required" or classy2.text == "Associate of Applied Science in Music and Technology: Guitar Concentration" or classy2.text == "Music Production and Audio for Media Associate Degree" or "18 months of accelerated studies" in classy2.text:
			continue
		word = classy2.text.strip("\n")
		print("----------")
		print(word)
		if classy2.text == "Location Sound I":
			break
	break
