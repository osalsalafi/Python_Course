# -------------------------------------------------------------------------------------------------------
# -- Python Course => Handling of Word and PDF documents => 07. Create a PDF document from a Word file --
# -------------------------------------------------------------------------------------------------------

from docx2pdf import convert

# docx_file = 'Software Engineer Osama alsalafi.docx'
# pdf_file = 'Software Engineer Osama alsalafi Converted.pdf'

# convert(docx_file, pdf_file)

docx_file = './Converted/'
convert(docx_file)