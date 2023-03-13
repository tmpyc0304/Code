import pdfplumber
import csv

pdf = pdfplumber.open(
    "D:/Code/Python/Practice/CAST Score Analysis/111_result_school_data.pdf"
)
csvfile = open("D:/Code/Python/Practice/CAST Score Analysis/2021 Admission Scores.csv", "w")
write = csv.writer(csvfile)

for i in range(len(pdf.pages)):
    page = pdf.pages[i]
    table = page.extract_tables()
    write.writerows(table[0][1:])

pdf.close()
csvfile.close()
