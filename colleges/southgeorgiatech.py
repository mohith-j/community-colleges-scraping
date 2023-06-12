# from bs4 import BeautifulSoup
# import requests
# import csv

# def namechange(name):
# 	link=name.replace(" - ","-")
# 	link = link.replace("- ", "-")
# 	link = link.replace("/", "-")
# 	link =link.replace(" ", "-")
# 	link="https://www.southgatech.edu/programs/"+link
# 	r = requests.get(link)
# 	if r.status_code != 404:
# 		return link
# 	else:
# 		return None


# url = "https://www.southgatech.edu/academics/all-programs/"
# html = requests.get(url)
# soup = BeautifulSoup(html.text, "html.parser")
# majors = soup.findAll("a", attrs={"class":None}, href=True)

# print(len(majors))
# for major in majors:
# 	print('---------------------------------')
# 	print(major.text)



from bs4 import BeautifulSoup
import requests
import csv

def get_classes(name, link):
    html=requests.get(link)
    soup=BeautifulSoup(html.text, "html.parser")
    classes=soup.findAll("li", attrs={"class":"acalog-course"})
    print(name)
    for clas in classes:
        clas_name=clas.find("a", attrs={"class":None}, href=True)
        print(clas_name.text)
        # insert writing spreadsheet code here

url = "https://www.southgatech.edu/academics/all-programs/"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
print(soup.text)
# programs= div.findAll("a", attrs={"class":None}, href=True)
# print(len(programs))
# for program in programs:
#     if "African American Studies Pathway, A.A." in major.text:
#         break
#     c+=1
# majors=majors[c:]
# print(len(majors))
# for major in majors:
#     link=major.find("a", attrs={"class":None}, href=True)
#     link="https://catalogs.gsu.edu/"+link["href"]
#     # print(link)
#     # print(major.text)
#     get_classes(major.text, link)
#     # link=major.find("a", attrs={"class":None}, href=True)
    
