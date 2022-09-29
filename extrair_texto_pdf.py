from cgitb import text
import PyPDF2

#Ccarrega o arquivo PDF
pdfFileObj = open('teste.pdf', 'rb')

#Faz a leitura do arquivo PDF
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#capatura a pagina do PDF
pageObj = pdfReader.getPage(1)

#extrai o texto do PDF e passa para variavel
text = pageObj.extractText()

#mostra o texto
print(text)