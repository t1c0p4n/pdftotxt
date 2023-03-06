from PyPDF2 import PdfFileWriter, PdfFileReader

file = "5G_Core_Security_in_Edge_Networks_A_Vulnerability_Assessment_Approach.pdf"

inputpdf = PdfFileReader(open(file, "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)