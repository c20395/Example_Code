# Example 10.26a Convert pdf to word

from pdf2docx import Converter
import glob
import os


pdfs_path = "" # folder where the .pdf files are stored
for i, pdf_file in enumerate(glob.iglob(pdfs_path+"*.pdf")):
    print(pdf_file)
    filename = pdf_file.split('\\')[-1]
    in_file = os.path.abspath(pdf_file)
    docx_file = os.path.abspath(filename[0:-4]+ ".docx")
    print(in_file)
    cv = Converter(in_file)
    cv.convert(docx_file)      
    cv.close()
