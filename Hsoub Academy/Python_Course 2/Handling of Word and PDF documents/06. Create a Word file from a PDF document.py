# -------------------------------------------------------------------------------------------------------
# -- Python Course => Handling of Word and PDF documents => 06. Create a Word file from a PDF document --
# -------------------------------------------------------------------------------------------------------

from pdf2docx import Converter

docx_file = 'Software Engineer Osama alsalafi.docx'
pdf_file = 'Software Engineer Osama alsalafi.pdf'

# Convert Pdf tp Docx
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()