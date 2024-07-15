# Example 10.28 Merge pdf files
# https://stackoverflow.com/questions/3444645/merge-pdf-files
#
from PyPDF2 import PdfFileMerger

#pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']
pdfs = ['file1.pdf', 'file2.pdf']
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
