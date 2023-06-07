

# Python program to read CSV file line by line
# import necessary packages
import csv
import requests

def majors(name):
    link=name.replace(" ","-")
    link="https://www.free-4u.com/Colleges/"+link+".html"
    r = requests.get(link)
    if r.status_code != 404:
        return link
    else:
        return None

# Open file 
college_name=[]
college_link=[]
with open('realcollegelist.csv') as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
    reader_obj = csv.reader(file_obj)
      
    # Iterate over each row in the csv 
    # file using reader object
    count=0
    for row in reader_obj:
        if(count>0):
            name=row[0]
            temp=majors(name)
            if(temp):
                college_name.append(name)
                college_link.append(temp)
        count=count+1

file = open("collegeswithlink.csv", "w")
writer = csv.writer(file)
writer.writerow(["Name","Link"])

for name, link in zip(college_name, college_link):
    writer.writerow([name, link])