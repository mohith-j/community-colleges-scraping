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


extractedText = extract('coastalpinestech.pdf')


pattern = r"[A-Z]{4} \d{4}\: [A-Za-z].+"
matches = []

for text in extractedText:
    match = re.findall(pattern, text)
    if match:
        matches.extend(match)


count = 0
matches = sorted(matches)
currmjr = ""
for m in matches:
    if currmjr != m[0:4]:
        print('---------------------------------')
        print(m[0:4])
    currmjr = m[0:4]
    print(m)