from bs4 import BeautifulSoup
import requests
import csv


def get_classes(name, link):
    html = requests.get(link)
    soup = BeautifulSoup(html.text, "html.parser")
    something= soup.find("html")
    print(something.text)
    # classes = soup.findAll("td", attrs={"class": "sc-coursetitle sc-programtable-column-2"})
    # print(name)
    # print(len(classes))
        # insert writing spreadsheet code here


url = "https://laniertech.smartcatalogiq.com/en/2022-2023/catalog/programs-of-study/"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
programs = soup.find("div", attrs={"id": "sc-program-links"})
programs = programs.findAll("a", attrs={"class": None}, href=True)
for program in programs:
    print("https://laniertech.smartcatalogiq.com"+program["href"])
    get_classes(program.text, "https://laniertech.smartcatalogiq.com"+program["href"])

# departments= programs.findAll("li", attrs={"class":"hasChildren"})
# for department in departments:
#     print(department.text)
# for majors_department in majors_departments:
#     majors_ul=majors_department.find("ul", attrs={"class":None})
#     print(majors_ul.txt)

# major_department = majors_department.findAll("a", attrs={"class":None})
# for major in major_department:
#     print(m.text)
#     print(m["href"])
#     #get_classes(m.text, m["href"])
