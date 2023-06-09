from bs4 import BeautifulSoup
import requests
import csv


url = "https://southernregional.edu/college-catalog/current/courses"
html = requests.get(url, verify=False)
soup = BeautifulSoup(html.text, "html.parser")
classy = soup.findAll("div", attrs={"class":"page-title"})


li = []
for classes in classy:
    mjr = classes.text[0:4]
    if mjr not in li:
        print('---------------------------------')
        print(mjr)
        if "L&L" in x:
            final = x[8:]
            print(final)
        else:
            final = x[9:]
            if " L" in final[0:2]:
                final = final[2:]
            print(final)
        li.append(mjr)
    else:
        final = x[9:]
        if " L" in final[0:2]:
            final = final[2:]
        if final[0] == " ":
            final = final[1:]
        if "RNSG" in mjr and final[0] == "B":
            final = final[1:]
        print(final)
