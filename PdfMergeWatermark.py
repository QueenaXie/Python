import PyPDF4
import sys

FILE_PATH = 'Scott Schedule.pdf'
reader = PyPDF4.PdfFileReader(open(FILE_PATH, 'rb'))

page = reader.getPage(0)

print(page.extractText())


#
# inputs = sys.argv[1:]
#
# def pdf_combiner(pdf_list):
#     merger = PyPDF4.PdfFileMerger()
#     for pdf in pdf_list:
#         print(pdf)
#         merger.append(pdf)
#     merger.write('super.pdf')



# template = PyPDF4.PdfFileReader(open('super.pdf', 'rb'))
# watermark = PyPDF4.PdfFileReader(open('wtr.pdf', 'rb'))
# output = PyPDF4.PdfFileWriter()
#
# for i in range(template.getNumPages()):
#     page = template.getPage(i)
#     page.mergePage(watermark.getPage(0))
#     output.addPage(page)
#
#     with open('watermarked_output.pdf', 'wb') as file:
#         output.write(file)