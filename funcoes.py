def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)

def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)

def codigoMorse():
    from winsound import Beep
    from time import sleep
    print('Escolha a velocidade de tradução')
    print('Rápido (1)')
    print('Lento (2)')
    if int(input('Velocidade: ')) == 1:
        vel = 0.4
    else:
        vel = 1
    texto = input('Texto a ser traduzido (minúsculas, sem acentos): ')
  
    morse = {'m': '--', ',': '--..--', '.': '.-.-.-', '1': '.----', '0': '-----', '3': '...--', '2': '..---', '5': '.....', '4': '....-', '7': '--...','6': '-....', '9': '----.', '8': '---..', '?': '..--..', 'a': '.-', 'c':'-.-.', 'b': '-...', 'e': '.', 'd': '-..', 'g': '--.', 'f': '..-.', 'i':'..', 'h': '....', 'k': '-.-', 'j': '.---', 'l': '.-..', 'o': '---', 'n':'-.', 'q': '--.-', 'p': '.--.', 's': '...', 'r': '.-.', 'u': '..-', 't':'-', 'w': '.--', 'v': '...-', 'y': '-.--', 'x': '-..-', 'z': '--..', '':'\n'}
    for i in texto:
        print(i, morse[i])
        for j in range(len(morse[i])):
            if morse[i][j] == '.':
                Beep(500,50 * vel)
                sleep(0.1 * vel)
            elif morse[i][j] == '-':
                Beep(500,150 * vel)
                sleep(0.1 * vel)
            else:
                sleep(0.3 * vel)
                sleep(0.3 * vel)

def calculate_storage(filesize):
    '''
    Função do curso Coursera
    '''
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    print(full_blocks)
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    print(partial_block_remainder)
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * (full_blocks + 1)
    return block_size * (full_blocks)

def jogoMemoria():
    import os
    import random
    r = random.randrange(10)
    print('Jogo de Memória\nDigite todos os numeros que forem informados pelo programa')
    print(f'╔═════╗')
    print(f'║ {r}   ║') # arrumar a questão visual
    print(f'╚═════╝')
    user = input('Tente: ')
    print('Jogo de Memória')
    c = 0
    while user == str(r):
        c += 1
        r = random.randrange(10)
        print(f'╔═════╗')
        print(f'║ {r}   ║')
        print(f'╚═════╝')
        MusicMemoria(1)
        user = input('Tente: ')
        os.system('cls')
        print('Jogo de Memória')
    print(f'Voce perdeu!')
    print(f'Seu saldo: {c}')

def MusicMemoria(n):
    import os
    from winsound import Beep
    t = '.'
    for i in range(n):
        t = t + '.'
        Beep(400, 400)
    os.system('cls')

def calcular_valor(valor_prod, qtde, moeda="real", desconto=None, acrescimo=None):
    v_bruto = valor_prod * qtde
    # 06/10/21
    dolar = 5.48
    euro = 6.32

    if desconto:
        v_liquido = v_bruto - (v_bruto * (desconto / 100))
    elif acrescimo:
        v_liquido = v_bruto + (v_bruto * (acrescimo / 100))
    else:
        v_liquido = v_bruto
   
    if moeda == 'real':
        return v_liquido
    elif moeda == 'dolar':
        return v_liquido * dolar
    elif moeda == 'euro':
        return v_liquido * euro
    else:
        print("Moeda não cadastrada!")
        return 0

   
valor_a_pagar = calcular_valor(valor_prod=32, qtde=5, desconto=5)
print(f"O valor final da conta é {valor_a_pagar}")

def calcular_valor_kw(valor_prod, qtde, moeda="real", **kwargs):
    v_bruto = valor_prod * qtde
   
    if 'desconto' in kwargs:
        desconto = kwargs['desconto']
        v_liquido = v_bruto - (v_bruto * (desconto / 100))
    elif 'acrescimo' in kwargs:
        acrescimo = kwargs['acrescimo']
        v_liquido = v_bruto + (v_bruto * (acrescimo / 100))
    else:
        v_liquido = v_bruto
   
    if moeda == 'real':
        return v_liquido
    elif moeda == 'dolar':
        return v_liquido * 5
    elif moeda == 'euro':
        return v_liquido * 5.7
    else:
        print("Moeda não cadastrada!")
        return 0

   
valor_a_pagar = calcular_valor_kw(valor_prod=32, qtde=5, desconto=5)
print(f"O valor final da conta é {valor_a_pagar}")

def converter_mes_para_extenso(data):
    mes = '''janeiro fevereiro março
      abril maio junho julho agosto
      setembro outubro novembro
      dezembro'''.split()
    d, m, a = data.split('/')
    mes_extenso = mes[int(m) - 1] # O mês 1, estará na posição 0!
    return f'{d} de {mes_extenso} de {a}'

print(converter_mes_para_extenso('10/05/2021'))

def calcular_desconto(valor, desconto=0): 
    # O parâmetro desconto possui zero valor default
    valor_com_desconto = valor - (valor * desconto)
    return valor_com_desconto

def imprimir_parametros(*args):
    qtde_parametros = len(args)
    print(f"Quantidade de parâmetros = {qtde_parametros}")
   
    for i, valor in enumerate(args):
        print(f"Posição = {i}, valor = {valor}")

       
print("\nChamada 1")        
imprimir_parametros("São Paulo", 10, 23.78, "João")

print("\nChamada 2")        
imprimir_parametros(10, "São Paulo")

def imprimir_parametros(**kwargs):
    print(f"Tipo de objeto recebido = {type(kwargs)}\n")
    qtde_parametros = len(kwargs)
    print(f"Quantidade de parâmetros = {qtde_parametros}")
   
    for chave, valor in kwargs.items():
        print(f"variável = {chave}, valor = {valor}")

       
print("\nChamada 1")        
imprimir_parametros(cidade="São Paulo", idade=33, nome="João")

print("\nChamada 2")        
imprimir_parametros(desconto=10, valor=100)

# Exemplo simples de lambda
somar = lambda x, y: x + y
somar(x=5, y=3)

# Exemplo de enumerate
nome = "Guido"
for i, c in enumerate(nome):
    print(f"Posição = {i}, valor = {c}")

def extrair_lista_email(dict_1, dict_2):
    lista_1 = list(zip(dict_1['nome'], dict_1['email'], dict_1['enviado']))
    print(f"Amostra da lista 1 = {lista_1[0]}")
    lista_2 = list(zip(dict_2['nome'], dict_2['email'], dict_2['enviado']))
    dados = lista_1 + lista_2
    print(f"\nAmostra dos dados = \n{dados[:2]}\n\n")
    # Queremos uma lista com o email de quem ainda não recebeu o aviso
    emails = [item[1] for item in dados if not item[2]]
    return emails

dados_1 = {
    'nome': ['Sonia Weber', 'Daryl Lowe', 'Vernon Carroll', 'Basil Gilliam', 'Mechelle Cobb', 'Edan Booker', 'Igor Wyatt', 'Ethan Franklin', 'Reed Williamson', 'Price Singleton'],
    'email': ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org', 'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu', 'semper.auctor.Mauris@Crasdolordolor.edu', 'risus.Quisque@condimentum.com', 'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu'],
    'enviado': [False, False, False, False, False, False, False, True, False, False]
}

dados_2 = {
    'nome': ['Travis Shepherd', 'Hoyt Glass', 'Jennifer Aguirre', 'Cassady Ayers', 'Colin Myers', 'Herrod Curtis', 'Cecilia Park', 'Hop Byrd', 'Beatrice Silva', 'Alden Morales'],
    'email': ['at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'non.arcu@mauriseu.com', 'fringilla.cursus.purus@erategetipsum.ca', 'Fusce.fermentum@tellus.co.uk', 'dolor.tempus.non@ipsum.net', 'blandit.congue.In@libero.com', 'nec.tempus.mauris@Suspendisse.com', 'felis@urnaconvalliserat.org'],
    'enviado': [False, False, False, True, True, True, False, True, True, False]
}

# emails = extrair_lista_email(dict_1=dados_1, dict_2=dados_2)
# print(f"E-mails a serem enviados = \n {emails}")


def ordenar_dois_valores(lista = [7, 4]):
    if lista[0] > lista[1]:
        aux = lista[1]
        lista[1] = lista[0]
        lista[0] = aux
    return lista

def ordenar_dois_valores_python(lista = [7, 4]):
    if lista[0] > lista[1]:
        lista[0], lista[1] = lista[1], lista[0]
    return lista

# print(ordenar_dois_valores())
# print(ordenar_dois_valores_python())

def executar_selection_sort(lista):
    n = len(lista)
    for i in range(0, n):
        index_menor = i
        for j in range(i+1, n):
            if lista[j] < lista[index_menor]:
                index_menor = j
        lista[i], lista[index_menor] = lista[index_menor], lista[i]
    return lista

def executar_selection_sort_2(lista):
    lista_ordenada = []
    while lista:
        minimo = min(lista)
        lista_ordenada.append(minimo)
        lista.remove(minimo)
    return lista_ordenada

def executar_bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def executar_insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        valor_inserir = lista[i] 
        j = i - 1
        
        while j >= 0 and lista[j] > valor_inserir:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor_inserir
    
    return lista

def executar_merge_sort(lista):
    if len(lista) <= 1: return lista
    else:
        meio = len(lista) // 2
        esquerda = executar_merge_sort(lista[:meio])
        direita = executar_merge_sort(lista[meio:])
        return executar_merge(esquerda, direita)
    
def executar_merge(esquerda, direita):
    sub_lista_ordenada = []
    topo_esquerda, topo_direita = 0, 0
    while topo_esquerda < len(esquerda) and topo_direita < len(direita):
        if esquerda[topo_esquerda] <= direita[topo_direita]:
            sub_lista_ordenada.append(esquerda[topo_esquerda])
            topo_esquerda += 1
        else:
            sub_lista_ordenada.append(direita[topo_direita])
            topo_direita += 1
    sub_lista_ordenada += esquerda[topo_esquerda:]
    sub_lista_ordenada += direita[topo_direita:]
    return sub_lista_ordenada

def executar_quicksort(lista, inicio, fim):
    if inicio < fim:
        pivo = executar_particao(lista, inicio, fim)
        executar_quicksort(lista, inicio, pivo-1)
        executar_quicksort(lista, pivo+1, fim)
    return lista

def executar_particao(lista, inicio, fim):
    pivo = lista[fim]
    esquerda = inicio
    for direita in range(inicio, fim):
        if lista[direita] <= pivo:
            lista[direita], lista[esquerda] = lista[esquerda], lista[direita]
            esquerda += 1
    lista[esquerda], lista[fim] = lista[fim], lista[esquerda]
    return esquerda

def executar_quicksort_2(lista):
    if len(lista) <= 1: return lista    
    pivo = lista[0]
    iguais  = [valor for valor in lista if valor == pivo]
    menores = [valor for valor in lista if valor <  pivo]
    maiores = [valor for valor in lista if valor >  pivo]
    return executar_quicksort_2(menores) + iguais + executar_quicksort_2(maiores)

# Parte 1 - Implementar o algoritmo de ordenação merge sort
def executar_merge_sort_v2(lista, inicio=0, fim=None):
    if not fim:
        fim = len(lista)
        
    if fim - inicio > 1:
        meio = (inicio + fim) // 2
        executar_merge_sort(lista, inicio, meio)
        executar_merge_sort(lista, meio, fim)
        executar_merge(lista, inicio, meio, fim)
    return lista

def executar_merge_v2(lista, inicio, meio, fim):
    esquerda = lista[inicio:meio]
    direita = lista[meio:fim]
    topo_esquerda = topo_direita = 0
    for p in range(inicio, fim):
        if topo_esquerda >= len(esquerda):
            lista[p] = direita[topo_direita]
            topo_direita += 1
        elif topo_direita >= len(direita):
            lista[p] = esquerda[topo_esquerda]
            topo_esquerda += 1
        elif esquerda[topo_esquerda] < direita[topo_direita]:
            lista[p] = esquerda[topo_esquerda]
            topo_esquerda += 1
        else:
            lista[p] = direita[topo_direita]
            topo_direita += 1

# Parte 2 - Implementar o algoritmo de busca binária
def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
        meio = (minimo + maximo) // 2
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True
    return False

# Parte 3 - Implementar a função que faz a verificação do cpf, o dedup e devolve o resultado esperado
def criar_lista_dedup_ordenada(lista):
    lista = [str(cpf).replace('.','').replace('-','') for cpf in lista]
    lista = [cpf for cpf in lista if len(cpf) == 11]
    lista = executar_merge_sort(lista)
    
    lista_dedup = []
    for cpf in lista:
        if not executar_busca_binaria(lista_dedup, cpf):
            lista_dedup.append(cpf)
    return lista_dedup

# Parte 4 - Criar uma função de teste
def testar_funcao(lista_cpfs):
    lista_dedup = criar_lista_dedup_ordenada(lista_cpfs)
    print(lista_dedup)
    
lista = [11, 20, 18, 10, 9, 5, 8, 11, -1, 3]
lista_cpfs = ['44444444444', '111.111.111-11', '11111111111', '222.222.222-22', '333.333.333-33', '22222222222', '444.44444']
# testar_funcao(lista_cpfs)
# print(executar_quicksort_2(lista))
# print(executar_quicksort(lista, inicio=0, fim=len(lista)-1))
# print(executar_merge_sort(lista))
# print(executar_insertion_sort(lista))
# print(executar_bubble_sort(lista))
# print(executar_selection_sort_2(lista))
# print(executar_selection_sort(lista))
# lista_ordenada1 = sorted(lista)
# lista_ordenada2 = lista.sort()
# print('lista = ', lista, '\n')
# print('lista_ordenada1 = ', lista_ordenada1)
# print('lista_ordenada2 = ', lista_ordenada2)
# print('lista = ', lista)

def lambda_exemplos():
    preco = 1000
    # Função normal
    def imposto_f(preco):
        return preco * .3
    # Função Lambda
    imposto_l = lambda x: x * .3
    print(imposto_f(preco))
    print(imposto_l(preco))
    precos = [100, 500, 10, 25]
    # lista, retornando list usando map para atualizar todos os valores
    impostos = list(map(lambda x:x*0.3, precos))
    print(impostos)
