from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_classes(name, link):
    html=requests.get(link)
    soup=BeautifulSoup(html.text, "html.parser")
    classes=soup.findAll("a", attrs={"class":"course-name"})
    print(name)
    for clas in classes:
        print(clas.text)
        df.loc[len(df.index)] = ["Albany Technical College",name, clas.text]
        
        

df = pd.DataFrame(columns=['Colleges','Majors','Courses'])
url = "https://www.albanytech.edu/college-catalog/current/programs"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
majors = soup.findAll("td", attrs={"class":"program-name"})
# c=0
for major in majors:
    link=major.find("a", attrs={"class":None}, href=True)
    link="https://www.albanytech.edu"+link['href']
    name=major.text
    get_classes(name, link)
    # c+=1
    # if c==4:
    #     break
with pd.ExcelWriter('data.xlsx',mode='a', if_sheet_exists='overlay') as writer:  
    df.to_excel(writer,sheet_name="Sheet",header=False, index=False)
 




