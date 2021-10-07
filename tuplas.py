# Tuplas
def funcoes_basicas_tuple():
    a,b = 0,'Deu certo?'
    print(a,b)
    a,b=b,a
    print(a,b)
    vogais = ('a', 'e', 'i', 'o', 'u')
    print(f"Tipo do objeto vogais = {type(vogais)}")
    for p, x in enumerate(vogais):
        print(f"Posição = {p}, valor = {x}")

    vogais = ('a', 'e', 'i', 'o', 'u')

    for item in enumerate(vogais):
        print(item)

    print(tuple(enumerate(vogais)))
    print(list(enumerate(vogais)))
    
# Set (Conjuntos)
def funcoes_basicas_set():
    # Observe como a sintaxe é parecida com a criação de um dicionário
    vogais_1 = {'aeiou'} # sem uso do construtor
    print(type(vogais_1), vogais_1)
    vogais_2 = set('aeiouaaaaaa') # construtor com string
    print(type(vogais_2), vogais_2)
    vogais_3 = set(['a', 'e', 'i', 'o', 'u']) # construtor com lista
    print(type(vogais_3), vogais_3)
    vogais_4 = set(('a', 'e', 'i', 'o', 'u')) # construtor com tupla
    print(type(vogais_4), vogais_4)
    print(set('banana'))
    # Exemplo de Diferença de conjuntos
    componentes_verificados = set(['caixas de som', 'cooler', 'dissipador de calor', 'cpu', 'hd', 'estabilizador', 'gabinete', 'hub', 'impressora', 'joystick', 'memória ram', 'microfone', 'modem', 'monitor', 'mouse', 'no-break', 'placa de captura', 'placa de som', 'placa de vídeo', 'placa mãe', 'scanner', 'teclado', 'webcam'])
    componentes_com_defeito = set(['hd', 'monitor', 'placa de som', 'scanner'])
    
    qtde_componentes_verificados = len(componentes_verificados)
    qtde_componentes_com_defeito = len(componentes_com_defeito)
    
    componentes_ok = componentes_verificados.difference(componentes_com_defeito)
    
    print(f"Foram verificados {qtde_componentes_verificados} componentes.\n")
    print(f"{qtde_componentes_com_defeito} componentes apresentaram defeito.\n")
    
    print("Os componentes que podem ser vendidos são:")
    for item in componentes_ok:
        print(item)
    # União
    componentes_ok = componentes_verificados.union(componentes_com_defeito)
        for item in componentes_ok:
          print(item)
    # Intersecção
    componentes_ok = componentes_verificados.intersection(componentes_com_defeito)
        for item in componentes_ok:
          print(item)
