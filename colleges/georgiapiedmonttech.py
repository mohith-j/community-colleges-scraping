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

extractedText = extract('piedmont.pdf')


classes = r"[A-Z]{4} \d{4} .+"
majors = r"[A-Z]{4} – .+"
majormatches = []
classmatches = []
#classmatches = sorted([*set(classmatches)])

for majo in extractedText:
    mat = re.findall(majors, majo)
    if mat:
        majormatches.extend(mat)

for clas in extractedText:
    match = re.findall(classes, clas)
    if match:
        classmatches.extend(match)

count = 0
for mm in majormatches:
    if "ACCT – Accounting" in mm or count > 0:
        count += 1
        print('---------------------------------')
        print(mm)
        mjr = mm[0:4]
        for m in classmatches:
            if m[0:4]== mjr:
                m = m.strip("                       3")
                m = m.strip("(4)")
                m = m.strip("(3)")
                m = m.strip("(2)")
                m = m.strip("(1)")
                m = m.strip(" (4)6")
                m = m.replace("     ", " ")
                m = m.replace("    ", " ")
                m = m.replace(" – ", " ")
                print(m)
    else:
        continue

