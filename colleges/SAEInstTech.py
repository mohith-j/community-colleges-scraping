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

extractedText = extract('saeinsttech.pdf')


classes = r"[A-Z]{3}\d{3}"
classmatches = []


for clas in extractedText:
    match = re.findall(classes, clas)
    if match:
        classmatches.extend(match)

classmatches = sorted([*set(classmatches)])
currmjr = ""
for m in classmatches:
    if currmjr != m[0:3]:
        print("--------------")
        print(m[0:3])
    currmjr = m[0:3]
    print(m)


