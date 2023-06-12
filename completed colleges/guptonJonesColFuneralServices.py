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
extractedText = extract('guptonjones.pdf')


pattern = r"[A-Z]{3} [0-9]{3} [A-Z].+\("
matches = []

for text in extractedText:
    match = re.findall(pattern, text)
    if match:
        matches.extend(match)

#matches = sorted(matches)
for m in matches:
    m=m[:-1]
    print(m)

