# Vamos abrir um arquivo para leitura

arq1 = open('Arquivos/Arquivo.txt','r')

# \ de windows
# / de linux

# Ler o arquivo

print(arq1.read())

# Retorna ao inicio do arquivo com a funçao seek

arq1.seek(0)

print(arq1.read())

#Fechar o arquivo

arq1.close()

# Abrir o arquivo para opçao de gravaçao e leitura

arq2 = open('Arquivos/Arquivo.txt','w+')

arq2.write('Tem novo conteudo\n')
arq2.write('Tem novo conteudo de novo\n')

#Voltar o curso para cima

arq2.seek(0)

# Ler o arquivo
print(arq2.read())

# Fechar o arquivo
arq2.close()

# Inserir mais dados sem sobrescrever com a funçao appneed ou a+

arq3 = open('Arquivos/Arquivo.txt','a+')

arq3.write('Nova escrita sem excluir')

arq3.seek(0) #Voltar o curso para cima

print(arq3.read())

arq3.close()

#  Utilizando contecto de manipulaçao de Arquivos. Pode ser qualquer tipo. É uma boa pratica e mantem o codigo organziado e perfomado.

#With open vai gerar um nome de contexto para o arquivo.

with open('Arquivos/Arquivo.txt','w+') as f:
    f.write('Nova Linhas\n')
    f.write('De novo Linhas\n')
    f.seek(0)
    print(f.read())
    f.close()


#Criando um novo arquivo

with open('Arquivos/Arquivo1.txt','a') as n:
    n.write('Nova Linhas\n')
    n.write('De novo Linhas\n')
    n.seek(0)
    print(n.read())
    n.close()




