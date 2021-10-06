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