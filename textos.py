import re

def lerDestinatariosEmail():
    try:
        w = open('c:/mailcollection.txt','a')
    except:
        w = open('c:/mailcollection.txt','w')
    lista = input('Mail: ')
    lista = lista.split()
    for i in range(len(lista)):
        lista[i] = lista[i].replace('<','').replace('>','').replace(',','')
    mail = []
    for i in range(len(lista)):
        if lista[i].__contains__('@'):
            mail.append(lista[i])
    for i in range(len(mail)):
        mail[i] = mail[i] + ','
    print('Enderecos capturados:\n')
    for i in mail:
        print(i)
        w.write(i)
    w.close()
    
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result

def remove_punctuation(value):
        return re.sub('[!#?.,;]', '', value)
    
def exemplo_operacoes_texto():
    texto = "Aprendendo Python na disciplina de linguagem de programação."
    # Tamanho da variável texto
    print(f"Tamanho do texto = {len(texto)}")
    # A 'palavra' está no texto?
    print(f"Python in texto = {'Python' in texto}")
    # Quantidade do valor de parâmetro na variável 
    print(f"Quantidade de y no texto = {texto.count('y')}")
    # Retorna os seis primeiros caracteres da variável
    print(f"As 5 primeiras letras são: {texto[0:5]}")
    # Converte o texto para maiúsculo
    print(texto.upper())
    # Converte o texto para minúsculo
    print(texto.lower())
    # Substitui a letra i por XX
    print(texto.replace("ça", 'ca'))
    # fatia a string, como não foi indicado o separador, por padrão usa o espaço
    palavras = texto.split()
    # imprime a string fatiada
    print(f"palavras = {palavras}")
    # imprime a quantidade das palavras
    print(f"Tamanho de palavras = {len(palavras)}")
    ############### PLN no braço
    # Transforma tudo para letras minúsculas
    texto = texto.lower()
    # Retira do texto tudo que não for palavra
    texto = texto.replace(",", "").replace(".", "").replace("(", "").replace(")", "").replace("\n", " ")
    # Cria um lista com as palavras
    lista_palavras = texto.split()
    # Guarda a quantidade de incidência das palavras 'string' e 'strings'
    total = lista_palavras.count("string") + lista_palavras.count("strings")
    # Mostra a mensagem do total
    print(f"Quantidade de vezes que string ou strings aparecem = {total}")
    vogais = ('a', 'e', 'i', 'o', 'u')
    for vogal in vogais:
        # Imprime o índice, seguido do valor da lista vogais
        print (f'Posição = {vogais.index(vogal)}, valor = {vogal}')
    # Outra forma de fazer
    vogais = []
    # tipo do objeto
    print(f"Tipo do objeto vogais = {type(vogais)}")
    # método para adicionar elemento na lista vogais
    vogais.append('a')
    vogais.append('e')
    vogais.append('i')
    vogais.append('o')
    vogais.append('u')
    for p, x in enumerate(vogais):
        # Imprime o índice, seguido do valor da lista vogais
        print(f"Posição = {p}, valor = {x}")
    
def mostrar(string=None):
    if string is not None:
        print(string)
    else:
        print(palavra)

#Textos
s3 = ('ok','então')
# método de adicionar um caracter coringa em um texto
print("/".join(s3))
palavra='termodinâmica'
mostrar(palavra[0])
mostrar(3*palavra[0])
mostrar(palavra[0:3])
mostrar(palavra[8:])
mostrar(palavra[:8])
mostrar(palavra[:])
mostrar(palavra[1:8:2])
mostrar(palavra[1:8:3])
mostrar(palavra[7:0:-1])
mostrar(palavra[7::-1])
mostrar(palavra[:4:-2])
palavra='socorram me subi no onibus em marrocos'
mostrar()
mostrar(palavra[::-1])
palavra='termodinâmica'
palavra+=' aplicada'
mostrar()
mostrar(int(len(palavra)))

constante=3.1415926535897931
print('O valor de pi é %.3f' %constante)
print('O valor de pi é %12.3f' %constante)#o número antes do ponto corresponde a quantia de caracteres, incluíndo espaços em branco
nome='abacaxi'
caracteristica='amarelo'
print('%s é uma fruta' %nome)
print('%s é %s' %(nome, caracteristica))
print('%f %ss também são %ss' %(constante,nome,caracteristica))
print('%.0f %ss também são %ss' %(constante,nome,caracteristica))

strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x: len(set(list(x))))
print(strings)

def add_numbers(x, y):
    return x + y
add_five = lambda y: add_numbers(5, y)

a = 'Boa tarde!'
a.split()
b = 'Boa tarde!'
print(a.replace('Boa','Mau'))
a = 'Good Night Vietnam'
print(a.__contains__('Vie'))
print(a.split().__contains__('Vie'))
print(a.split().__contains__('Vietnam'))
print(1, 2, 3, sep=' < ')
input('OK!')
