# Exemplos de manipulação de arquivos
import os

arquivo = open('tabela.txt','w') # Cria um arquivo novo chamado tabela.txt se já existir sobreescre, cuidado!
arquivo.close()
arquivo = open('tabela.txt', 'a') # Abri o arquivo tabela.txt em modo de edição
arquivo.write('%s\n' %'Tabela de dólares')
for i in range(100):
    arquivo.write('%i dólares valem %f reais\n' %(i, i * 5.21))
arquivo.close()
arquivo = open('tabela.txt', 'r') # Abri o arquivo tabela.txt em modo de leitura
arquivo.readline() # Lê linha por linha do arquivo, quando acabar retorna uma string vazia
lista = arquivo.readlines() # Lê todo o arquivo armazenando o conteúdo em listas
arquivo.close()
atalho = os.startfile 
atalho('tabela.txt') # Abri o arquivo especifícado quando desejar (funciona só com exe e bat?)
arquivo = os.system
arquivo('tabela.txt') # Abri o arquivo tabela.txt
comando = os.system
comando('copy c:\meumodulo.py c:\Python23') # Copia um arquivo para um diretório
NOME = input('Seu nome: ') # Solicita um nome para a criação
NOME = 'Exemplo-' + NOME # Concatena
comando('md c:\''+ NOME) # Cria uma pasta com o nome anteriormente solicitado
comando('copy c:\meuprograma.py c:\'' + NOME) # Copia outro aquivo para a pasta recém criada
abrir = os.startfile # abri o arquivo abaixo.
abrir('leiame.txt')
arquivo = open("saidas.tnts", "r")
linhas = arquivo.readlines()
arquivo.close()
#i = 0
#for g in linhas:
dic = dict(linhas)
    #print(tupla)
    #dict[ key ] = value
    #user_input = input('1 abcde')# simulando a entrada do usuário  
    #user_input = user_input.split(' ')  
    #user_notes[user_input[0]] = user_input[1];
    # dic['codigo'] = tupla[0]
    # dic['data'] = tupla[1]
    # dic['hora'] = tupla[2]
    # dic['obs'] = tupla[3]
    # dic['descricao'] = tupla[4]
    #i += 1
    # print

print(dic)