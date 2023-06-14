"""
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
"""
import PyPDF2
import re

def extract(pdfs):
	with open(pdfs, "rb") as pdf:
		reader = PyPDF2.PdfReader(pdf, strict=False)
		text = []

		for page in reader.pages:
			content = page.extract_text()
			text.append(content)

		return text

extractedText = extract('completed colleges/laniertech.pdff')


pattern = r"[A-Z]{4} \d{4} [A-Z].+ \("
matches = []

for text in extractedText:
	match = re.findall(pattern, text)
	if match:
		matches.extend(match)


li = []
final = []
for m in matches:
	if m[0:9] not in li:
		li.append(m[0:9])
		final.append(m)
final = sorted(final)
currmjr = ""
for i in final:
	if currmjr != i[0:4]:
		print('---------------------------------')
		print(i[0:4])
	currmjr = i[0:4]
	if i[0:9] == "EMSP 2510":
		print("EMSP 2510 Clinical Applications for the Paramedic - I")
		continue
	if i[0:9] == "EMSP 2520":
		print("EMSP 2510 Clinical Applications for the Paramedic - II")
		continue
	if i[0:9] == "EMSP 2530":
		print("EMSP 2510 Clinical Applications for the Paramedic - III")
		continue
	i = i.strip("(")
	print(i)