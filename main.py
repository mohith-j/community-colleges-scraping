import os
import subprocess
from openpyxl import Workbook
import pandas as pd

def addHeaders():
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.append(["Colleges","Majors","Courses"])
    workbook.save('data.xlsx')

addHeaders()
# Give complete path
directory = '/Users/mohithjothikannan/Desktop/python-scripts/completed colleges'

# Iterate over all files in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    
    # Check if the file is a Python file
    if filename.endswith('.py'):
        print(f'Running file: {filename}')
        
        # Run the Python file using subprocess
        subprocess.run(['python3', filepath])

