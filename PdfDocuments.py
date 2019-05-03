import PyPDF2

if False:
    with open("messi.pdf", "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        print(reader.numPages)
        page = reader.getPage(0)
        page.rotateClockwise(90)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open("rotateted_messi.pdf", "wb") as output:
            writer.write(output)

merger = PyPDF2.PdfFileMerger()
file_names = ["messi.pdf", "xplit.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("combine_messi.pdf")
