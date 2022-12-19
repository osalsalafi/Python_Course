# ------------------------------------------------------------------------------------------------------------------
# -- Python Course => Handling of Word and PDF documents => 02. Create PDF documents and perform operations on it --
# ------------------------------------------------------------------------------------------------------------------
import PyPDF2

# To read a file :
# 1) open the file in an object
pdfFileObj = open('Software Engineer Osama alsalafi.pdf', 'rb')
# 2) open the reader
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# To wrtie to a file
# 1) open the file in an object
pdfFileObj1 = open('TestFile.pdf', 'wb')
# 2) open the writer 
pdfWriter = PyPDF2.PdfFileWriter(pdfFileObj1)


pdfWriter.add_blank_page(219,279)
pdfWriter.add_blank_page(219,279)

# 3) write to the file
pdfWriter.write(pdfFileObj1)

pdfFileObj1.close()
pdfFileObj.close()
# ----------------------------------- #
pdfFileObj2 = open('الملف التعريفي لشركة فاست نت.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj2)

pageobj = pdfReader.getPage(1)

pdfFileObj3 = open('TestFile.pdf', 'wb')
pdfWriter = PyPDF2.PdfFileWriter(pdfFileObj3)

pdfWriter.add_blank_page(219,279)
pdfWriter.add_blank_page(219,279)
pdfWriter.add_page(pageobj)
pdfWriter.write(pdfFileObj3)

pdfFileObj2.close()
pdfFileObj3.close()