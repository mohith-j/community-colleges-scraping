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

extractedText = extract('georgiamilitary.pdf')


pattern = r"[A-Z]{3} \d{3} [A-Z].+"
altpattern = r"[A-Z]{3} \d{3}[A-Z] [A-Z].+"
thirdpattern = r"[A-Z]{3} \d{3}.+"

matches = []

for text in extractedText:
    match = re.findall(pattern, text)
    altmatch = re.findall(altpattern, text)
    thirdmatch = re.findall(thirdpattern, text)
    if match:
        matches.extend(match)
    elif altmatch:
        matches.extend(altmatch)
    if thirdmatch:
        matches.extend(thirdmatch)

count = 0
matches = sorted([*set(matches)])
currmjr = ""

li = []
final = []
currmjr = ""
for z in matches:
    if z[0:7] not in li and len(z) > 17:
        li.append(z[0:7])
        final.append(z)
for f in final:
    if currmjr != f[0:4]:
        if f[0:3] == "EEE" or f[0:3] == "GMC":
            continue
        print('---------------------------------')
        print(f[0:4])
    currmjr = f[0:4]
    f = f.replace("BIO 123 & 124 (minimum score of 50 required)", "BIO 123 General Biology I")
    f = f.replace("  ", " ")
    f = f.replace("BSM 430 . Students must complete the course with a grade of “C” or better.", "BSM 430 Principles of Supply Chain Management")
    f = f.replace("CHE 121 & CHE 122", "CHE 121 Principles of Chemistry I")
    f = f.replace("ECO 201 or 202 for Business majors and Logistics majors if not taken in Area F.", "ECO 201 Macroeconomics\nECO 202 Microeconomics")
    f = f.replace("EDN 236 Teaching and Learning 5qh", "EDN 216 Exploring Socio-Cultural Perspective on Diversity in Educational Settings\nEDN 226 Investigating Critical and Contemporary Issues in Education\nEDN 236 Teaching and Learning ")
    f = f.replace("ENG 201 OR ENG 202", "ENG 201 World Literature I")
    f = f.replace("FRE 102 (minimum score of 60 required)", "FRE 102 Elementary French II")
    f = f.replace("GER 102 (minimum score of 60 required)", "GER 102 Elementary German II")
    f = f.replace("ENG 221 & 222, or ENG 231 & 232) 5", "ENG 221 American Literature")
    f = f.replace("HIS 121 (Does NOT MEET GA History requirement)", "HIS 121 American History I")
    f = f.replace("HIS 122 (Does NOT MEET GA History requirement)", "HIS 122 American History II")
    f = f.replace("HPE 200/202/250/255/260, REL 220/225", "HPE 200 Introduction to Health & Physical Education")
    f = f.replace("HSE 101, HSE 299, PLS 205", "HSE 101 Introduction to Homeland Security and Emergency Management")
    f = f.replace("MAT 112 (grade of C or better); RDG 099 or placement.", "MAT 112 Precalculus")
    f = f.replace("NTR 110 recommended) (excluding BIO", "NTR 110 Nutrition")
    f = f.replace("PLS 101 (Does NOT MEET GA Constitution", "PLS 101 Introduction to American Government")
    f = f.replace("PSY 200 (if not used in Social Sciences core", "PSY 200 Introduction to Psychology")
    f = f.replace("SPA 101 & 102 (minimum score of 63 required)", "SPA 101 Elementary Spanish I\nSPA 102 Elementary Spanish II")
    f = f.replace("5qh", "")
    f = f.replace("1qh", "")
    f = f.replace("2qh", "")
    f = f.replace("6qh", "")
    f = f.replace("3qh", "")
    f = f.replace(",", "")
    print(f)