# Example 10.26 Convert pdf to word

from pdf2docx import Converter

pdf_file = 'source.pdf'
docx_file = 'source1.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()
