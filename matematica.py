#Utilidades
import os
from random import randint

def fibonacci(numero):
    if numero <= 1:
        return numero
    else:
        # recursividade
        return fibonacci(numero - 1) + fibonacci(numero - 2)
    
def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        # recursividade
        return numero * fatorial(numero - 1)

def testar_par(x):
    if x % 2 == 0:
        print(x,'é um número par')
    else:
        print(x,'é um número ímpar')

def testar_primo(numero):
    c = 1
    if numero > 1:
        for i in range(2, numero):#(3, numero // 2 + 1):#Nenhum número é divisível pela sua metade mais 1, depois de sua metade, só o será por ele mesmo. Que nesta lógica não será aplicada
            if numero % i == 0:
                c += 1
        if c != 1:
            return False #'Número não é primo'
        else:
            return True #'Número é primo'
    else:
        return False #'Número não é primo'

def testar_primo_v2(valor):
    teste = 0
    for individuo in range(2, valor):
        if valor % individuo == 0:
            teste = teste + 1
    if teste != 0:
        print(valor,'não é primo')
    else:
        print( valor,'é primo')

def testar_numero_perfeito(gretagarbo):
    verifica = 0
    for qualquerum in range(1, gretagarbo):
        if gretagarbo % qualquerum == 0:
            verifica = verifica + qualquerum
    if verifica == gretagarbo:
        print(gretagarbo,'é perfeito')
    else:
        print(gretagarbo,'não é perfeito')

def procurar_divisores(n):
    lista_de_divisores = []
    for i in range(1, n):
        if n % i == 0:
            lista_de_divisores.append(i)
    if len(lista_de_divisores) == 0:
        print(n,'Não tem divisores')
    else:
        print('Divisores de',n,':')
        for i in lista_de_divisores:
            print(i)
        print(n)

def ler_matriz():
    ordem = int(input('Ordem da matriz: '))
    matriz = []
    print('Digite os termos da matriz A')
    for i in range(ordem):
        matriz.append([])
        for j in range(ordem):
            termo = 'A' + str(i + 1) + str(j + 1)
            matriz[i].append(float(input('Termo'+ termo +': ')))
        #print('\n')
    print('Matriz A\n')
    for k in range(ordem):
        for w in range(ordem):
            print('%7.2f' %matriz[k][w])

def somar_algarismos(n):
    n = str(n)
    while len(n) > 1:
        m = 0
        for i in n:
            m += int(i)
        n = str(m)
    print(n)

def testar_quadrado(numero, expoente):
    '''Esta função eleva o primeiro parâmetro
       para o segundo parâmetro
    '''
    return numero ** expoente

def gerar_numero_aleatorio(tipo, min, max):
    import random
    if tipo == 0: #retorna um inteiro
        return random.randint(min, max)
    elif tipo == 1: #retorna um número real
        return random.random() + random.randint(min, max)
    else:
        return tipo

def gerar_texto_aleatorio(_listaPrimeiro, _listaSegundo = ''):
    import random
    p1 = _listaPrimeiro
    p2 = _listaSegundo
    saida = random.choice(p1)
    if _listaSegundo != '':
        saida += ' ' + random.choice(p2)
    return saida
        
#Uma função para fazer uma leitura de número Real, retornando o valor digitado
def ler_numero_real(texto = 'Digite um número Real...\n'):#Se não for informado um parâmetro, usa o texto pré setado
    while True:
        try:
            valor = float(input(texto))#Trocando float por int, tem-se uma para leitura de números inteiros
            break
        except:
            os.system('cls') #para usar essa função precisa importar a biblioteca os, ela limpa a tela
            print('Erro de digitação!!!')
    return float(valor)

def ler_numero_inteiro(texto):
    while True:
        try:
            valor = int(input(texto,'\n'))
            break
        except:
            os.system('cls')
            print('Erro de digitação!!!')
    return valor

def matrizes():
    matriz = ((1,0,0),(0,1,0),(0,0,1))
    for i in range(len(matriz)): # é o mesmo que range(3), ok?
        print('\n')
        for j in range(len(matriz)): # idem
            print(f'{matriz[i][j]}.')

lista = [['julian', '0', '5'], ['ana', '10', '4']]

# vamos criar uma função de 'busca'
def encontrar(elemento):
    pos_i = 0 # variável provisória de índice
    pos_j = 0 # idem

    for i in range (len(lista)): # procurar em todas as listas internas
        for j in range (i): # procurar em todos os elementos nessa lista
            if elemento in lista[i][j]: # se encontrarmos elemento ('ana')
                pos_i = i # guardamos o índice i
                pos_j = j # e o índice j
                break # saímos do loop interno
            break # e do externo
    return (pos_i, pos_j) # e retornamos os índices


r = encontrar('ana') # chamamos a função e salvamos em r
print(r) # imprime índices
print(lista[r[0]][r[1]]) # usa índices na lista como prova

b=10
while 1:
    b-=1
    print(f'{b}')
    if b<7: break

def cambio(componente):
    print(componente[0], 'R$ ', componente[1])
    print(componente[0], 'US$ ', componente[1] / 3.0)
    print('\n')

def funcao_derivada():
    import math
    from os import startfile
    from time import time, localtime
    print('Operadores especiais disponíveis:')
    print('sin, cos, log (neperiano),')
    print('log10 (base 10), e sqrt (raiz quadrada).\n')
    funcao = input('Função: ')
    derivada = input('Derivada: ')
    x0 = float(input('Valor inicial: '))
    t0 = time()
    f ='x-(('+funcao+')/('+derivada+'))'
    w = open('c:/newton-raphson.txt','w')
    w.write(' Newton-Raphson\n\n')
    if localtime()[3] <= 12:
        w.write(' Bom dia!\n\n')
    elif 12 < localtime()[3] < 18:
        w.write(' Boa tarde!\n\n')
    else:
        w.write(' Boa noite!\n\n')
    w.write('Procedimentos para encontrar a raiz de '+ funcao +'\n\n')
    w.write('Valor inicial: ' + str(x0) + '\n\n')
    x = x0
    for p in range(10):
        w.write('Iteração '+ str(p + 1) +':\n')
        x = eval(f)
        w.write(str(x)+'\n')
        w.write('\n')
    w.write('Valor aproximado da raiz: '+ str(x) +'\n\n')
    w.write('Tempo para cálculos: '+ str(time() - t0) +'\n')
    w.close()
    startfile('c:/newton-raphson.txt')
