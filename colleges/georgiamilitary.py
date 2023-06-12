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
#AC-Catalog-2022-2023-08082022
extractedText = extract('georgiamilitary.pdf')


pattern = r"[A-Z]{3} \d{3} [A-Z].+"
altpattern = r"[A-Z]{3} \d{3}[A-Z] [A-Z].+"
#thirdpattern = r"[A-Z]{3} \d{3}[A-Za-z\s]+"
matches = []

for text in extractedText:
    match = re.findall(pattern, text)
    altmatch = re.findall(altpattern, text)
#    thirdmatch = re.findall(thirdpattern, text)
    if match:
        matches.extend(match)
    if altmatch:
        matches.extend(altmatch)
#    if thirdmatch:
#        matches.extend(thirdmatch)

count = 0
matches = sorted(matches)
currmjr = ""
for m in matches:
    if currmjr != m[0:4]:
        print('---------------------------------')
        print(m[0:4])
    currmjr = m[0:4]
    if "or higher" in m or "CHE 105 OR CHE 12 1 6" in m or "Prerequisites" in m or "ENG 201 OR ENG 202" in m:
        continue
    if len(m) > 17:
        print(m)
