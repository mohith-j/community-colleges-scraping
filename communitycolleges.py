from bs4 import BeautifulSoup
import requests
import csv


url = "https://www.free-4u.com/Community-Colleges/Georgia-Community-Colleges.html"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
colleges = soup.findAll("a", attrs={"class":None})

file = open("realcollegelist.csv", "w")
writer = csv.writer(file)
writer.writerow(["Colleges"])

startlist = []
for college in colleges:
	startlist.append(college.text)

collegelist = []

for c in startlist:
	if "Colleges" not in c and ("Institute" in c or "College" in c):
                collegelist.append(c)


final = sorted([*set(collegelist)])
for x in final:
	print(x)
	writer.writerow([x])
file.close()

