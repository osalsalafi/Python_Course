# --------------------------------------------------------------------------------------------------------------------
# -- Python Course => Handling of Word and PDF documents => 01. Recognize PDF documents and extract texts from them --
# --------------------------------------------------------------------------------------------------------------------

import PyPDF2

pdfFileObj = open('Software Engineer Osama alsalafi.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# PAEGS NUMBER
print(pdfReader.numPages)

# READ 
pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())
print(pageObj.extract_text())


# CLOSE
pdfFileObj.close()

