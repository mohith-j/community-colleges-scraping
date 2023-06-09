from bs4 import BeautifulSoup
import requests
import csv


url = "https://atlantatech.smartcatalogiq.com/2022-2023/College-Catalog/Courses"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
classy = soup.findAll("a", attrs={"class":None}, href=True)


li = []
count = 0
for classes in classy:
	if "ACCT 1100" not in classes.text and count < 1:
		continue
	if "ACCT 1100" in classes.text:
		count += 10

	mjr = classes.text[0:4]
	if mjr not in li:
		print('---------------------------------')
		print(mjr)
		final = classes.text[10:]
		print(final)
		li.append(mjr)
	else:
		final = classes.text[10:]
		if final[0] == " ":
			final = classes.text[11:]
		print(final)
