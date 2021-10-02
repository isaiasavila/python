import time as tm
import bisect

from datetime import datetime, date

f = True
def formatarHora(dataParaFormatar=None):
    #dt.strftime('%m/%d/%Y %H:%M')
    #%D Atalho para %m/%d/%y (por exemplo, 04/18/12)
    if dataParaFormatar is not None:
         dt = dataParaFormatar
         #datetime.strptime('20091031', '%Y%m%d')
         #'{%H:%M:%S}'.format(dt)
    else:
        dt = tm.localtime()
    return dt.strftime('%m/%d/%Y %H:%M')

def padronizaNumero(numero):
    texto = str('{:02d}'.format(numero))
    return texto

def append_element(some_list, element):
    some_list.append(element)

def add_and_maybe_multiply(a, b, c=None):
    result = a + b
    if c is not None:
        result = result * c
    return result

def teste():
    while f == True:
        #data = [1, 2, 3]
        #append_element(data, 4)
        #data.append(5)
        #print(data)
        c = 2**(3+6)
        print(int(c))
        print(int(c % 7))
        print(int(c // 7))
        input('ok...')

        if isinstance(int(c),int):
            v = [1, 2, 3, 4]
            #Observe que interessante esse controle de fluxo
            if v[3] > v[2] > v[1] > v[0] > 0:
                print(f'Zero é menor do que {v[0]} {v[1]} {v[2]} {v[3]}')

        #Exemplos For:
        sequence = [1, 2, None, 4, None, 5]
        total = 0
        for value in sequence:
            if value is None:
                continue #Se o valor não for nada, pula para o próximo
            #print(str(total),'\n')
            total += value
        sequence = [1, 2, 0, 4, 6, 5, 2, 1]
        total_5 = 0
        for value in sequence:
            #print(str(total_5),'\n')
            if value == 5:
                break
            total_5 += value

        x = 256
        total = 0
        while x > 0:
            if total > 500:
                break
            total += x
            x = x // 2
        
        if x < 0:
            print('negative!')
        elif x == 0:
            TODO: print('inteligente')
            pass
        else:
            print('positive!')

        x = int(input('Digite!\n'))
        print('Non-negative') if x >= 0 else print('Negative')
        #Abaixo um exemplo de tupla
        tupla = 4, 5, 6, 7, 10, 34
        print(tupla)
        a = 0
        b = 0
        #Exemplo de swap
        tmp = a
        a = b
        b = tmp
        #Swap no Python
        a, b = 1, 2
        b, a = a, b
        #Mais rápido
        list_of_lists = ''
        everything = []
        for chunk in list_of_lists:
            everything.extend(chunk)
        #Mais lento
        everything = []
        for chunk in list_of_lists:
            everything = everything + chunk

        a = [7, 2, 5, 1, 3]
        a.sort()
        b = ['saw', 'small', 'He', 'foxes', 'six']
        b.sort(key=len)

        c = [1, 2, 2, 2, 3, 4, 7]
        bisect.bisect(c, 2)
        bisect.insort(c, 6)
        #Zip
        seq1 = ['foo', 'bar', 'baz']
        seq2 = ['one', 'two', 'three']
        zipped = zip(seq1, seq2)
        list(zipped)
        seq3 = [False, True]
        list(zip(seq1, seq2, seq3))
        for i, (a, b) in enumerate(zip(seq1, seq2)):
            print('{0}: {1}, {2}'.format(i, a, b))

        pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
        first_names, last_names = zip(*pitchers)
        list(reversed(range(10)))

        #Diferenças entre tupla e lista
        tupla = (1, 2, 3, 4, 5)
        lista = [1, 2, 3, 4, 5]
        lista = lista + [6, 7] #Operação custosa
        lista.extend(8, 9) #Melhor adicionar assim
        lista = list(tupla) #Método para passar uma tupla para uma lista
        lista.append(6) #Cria um novo index e adiciona o valor 6 nele
        lista.insert(0, 0) #Maior custo de processamento
        b_list = ['foo', 'red', 'baz', 'dwarf']
        b_list.pop(0)
        b_list.remove('foo')
        'dwarf' not in b_list #Serve como um teste lógico, com ou sem not

        seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        seque = 1, 2, 3, 4, 3, 3, 5, 6, 3, 4
        cont = seq.count(3)
        for a, b, c in seq:
            print('a={0}, b={1}, c={2}'.format(a, b, c))
        
        values = 1, 2, 3, 4, 5
        a, b, *rest = values #Costumam usar também *_
        print(a, b) 
        print(rest)

def teste_string():
    '''
    Método que abre um arquivo cheio de palavras, escolhe as maiores do que 4 e grava em um outro arquivo
    '''
    with open('temp.txt') as file_object:
        # le todas as linhas
        lista = file_object.readlines()

    palavras = ''
    for i in range(len(lista)):
        if len(lista[i]) > 5:
            # registro.append(lista[i])
            palavras = palavras + lista[i]
    # print(registro)

    with open('words.txt', 'w') as file_object:
                    # escreve no arquivo
        file_object.write(palavras)

teste_string()

        #if isinstance(c,int):
        #    f = True
        #else:
        #    f = False
        #print('----------------------------------------------------------------------------')
        #entrada = (input('Digite!\n'))
        #entrada = int(entrada)
        #temp = padronizaNumero(entrada)
        #print(temp)
        #obs = str(data[2]) + '/' + str(data[1]) + '/' + str(data[0]) 
        #+ 'w,' + str(data[3]) + ':' + str(data[4]) + ','    '{:%Y-%m-%d %H:%M:%S}'.format(d)
            #não funcionou, obs = '{%H:%M:%S}'.format(data)
        #obs = str(data.tm_mday)
        #if entrada == 's':
        #    f = False
        #Strings https://docs.python.org/3.6/library/string.html)
        #{0:.2f} significa formatar o primeiro argumento como um número de ponto flutuante com duas casas decimais.
        #{1:s} significa formatar o segundo argumento como uma string.
        #{2:d} significa formatar o terceiro argumento como um inteiro exato.