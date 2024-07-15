# Example 10.27 Convert pdf to word

from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfile
from PyPDF2 import PdfFileReader

# Select an input pdf file
input_file = askopenfilename(defaultextension=".pdf", 
                            filetypes=[("Pdf files","*.pdf")])
text = ""

pdfFile = open(input_file, 'rb')
# creating a pdf reader object
read_pdf = PdfFileReader(pdfFile) 

c = read_pdf.numPages
for i in range(c):
    page = read_pdf.getPage(i)
    text+=(page.extractText()) 

# closing the pdf file object 
pdfFile.close()

# Select an output Doc file  
wordfile = asksaveasfile(mode='w',defaultextension=".doc", 
                        filetypes=[("word file","*.doc"),
                                    ("text file","*.txt")])

# convert the pdf file to doc file
wordfile.write(text)
wordfile.close()
print("saved: ",wordfile) 
