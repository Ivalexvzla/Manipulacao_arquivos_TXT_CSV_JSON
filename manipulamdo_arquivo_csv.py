#Manipulaçao de arquivo CSV, para manipar ler , criar arquivos CSV utilizamos a biblioteca CSV

import csv

# Usando gerenciador de contexto de arquivos para criar um CSV

with open('arquivos/nomes,csv','w+',encoding='UTF8',newline="") as fcsv:
    escrever = csv.writer(fcsv,delimiter=',')
    escrever.writerow(('Nome','Sobrenome','Idade'))
    escrever.writerow(('Iván','Valery',30))
    escrever.writerow(('Pedro','Marquez',38))
    escrever.writerow(('Naty','Perdomo',36))


#Ler o arquivo criado com a funçao CSV.reader

with open('arquivos/nomes,csv','r',encoding='UTF8') as fcsv:
    ler = csv.reader(fcsv)

    lista1 = list(ler)
    print(lista1)

    for i in lista1:
        print(i)

#Ler o arquivo CSV e transforma-lo em dicionario

with open('arquivos/nomes,csv','r',encoding='UTF8') as fcsv:
    ler_dict = csv.DictReader(fcsv)

#Iterando directamente o objeto convertido

    """for i in ler_dict:
        print(i)"""

    for d in ler_dict:
        print(d['Nome'])

#Ler um arquivo CSV e gravar numa lista

with open('arquivos/arquivo CSV.csv','r') as arq1:
    arq1 = csv.reader(arq1)

#Iterar os valores do csv

    """for i in arq1:
        print(i)"""

#Transformar uma lista

    lista2 = list(arq1)
    print(lista2)
