from fnmatch import translate
import PyPDF2

# Informa o caminho e arquivo PDF
#file = '5G_Core_Security_in_Edge_Networks_A_Vulnerability_Assessment_Approach.pdf'
file = input("Digite o nome do arquivo a ser convertido: ")

# Carrega arquivo PDF
pdfFileObj = open(file, 'rb')

# Leitura do arquivo PDF
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Captura a quantidade de páginas do PDF
numeroPaginas = pdfReader.numPages
#print('Num_Páginas = ' + str(numPage))

# Retirando textos comuns da conversão:
ignore1 = input("Digite o texto a ser retirado da conversão: ")
ignore2 = input("Digite outro texto a ser retirado da conversão: ")

p = 0
while p < numeroPaginas:
    pageObj = pdfReader.getPage(p)

    # Extrai texto do PDF e passa para variável
    text = pageObj.extract_text()

    # Mostra texto extraído
    text = text.replace('\x0c','').replace('\r','').replace('\n',' ')
    #text = text.strip("M. A. Habibi et al.: A Comprehensive Survey of RAN Architectures Toward 5G Mobile Communication System")
    
    # Retirando textos comuns da conversão:
    text = text.strip(ignore1).strip(ignore2).strip('\ufb02')

    # Imprimindo páginas convertidas
    filetxt = (file + '.txt')
    
    ##print("\n### PÁGINA : " + str(p) + " ###\n")
    ##print(text)

    # Abre o arquivo backup.txt e escreve o backup
    print('Aguarda a conversão e escrita do arquivo... Página [' + str(p) + ']')
    txt = open(filetxt, 'a')
    txt.write("\n### PÁGINA : " + str(p) + " ###\n")
    txt.write(str(text.encode('utf-8').replace('\xef\xac\x81','fi').replace('\xef\xac\x82','fl')))
    txt.write('\n')

    p += 1

# Traduzindo o texto extraído
#from googletrans import Translator

#translator = Translator()
#print(translator.translate(text, dest='pt'))


## Tabela de substituição de caracteres:
# \xe2\x80\x93  - 
# \xe2\x80\x94  -
# \xef\xac\x81  fi
# \xef\xac\x82  fl
# \xe2\x80\x99  '
# \xe2\x80\x93  -
# \xe2\x80\x9c  "
# \xe2\x80\x9d  "
