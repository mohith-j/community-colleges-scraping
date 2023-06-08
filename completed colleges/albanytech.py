from bs4 import BeautifulSoup
import requests
import csv

def get_classes(name, link):
    html=requests.get(link)
    soup=BeautifulSoup(html.text, "html.parser")
    classes=soup.findAll("a", attrs={"class":"course-name"})
    print(name)
    for clas in classes:
        print(clas.text)
        # insert writing spreadsheet code here

url = "https://www.albanytech.edu/college-catalog/current/programs"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
majors = soup.findAll("td", attrs={"class":"program-name"})
# print(len(majors))
for major in majors:
    link=major.find("a", attrs={"class":None}, href=True)
    link="https://www.albanytech.edu"+link['href']
    name=major.text
    get_classes(name, link)


#     each=l.split("\n")
#     each=each[1:-1]
#     for e in each:
#         all_majors.append(e)
# print(all_majors)
#     listOfMajorsEachField.append(u.text)
# major=[]
# for majors in listOfMajorsEachField:
#     print(majors+"*")


