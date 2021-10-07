#Listas
def outras_funcoes():
        lista = ['Python', 30.61, "Java", 51 , ['a', 'b', 20], "maça"]
    # uma lista, dentro de outra lista conta como um elemento
    print(f"Tamanho da lista = {len(lista)}")

    for i, item in enumerate(lista):
        print(f"Posição = {i},\t valor = {item} -- tipo individual = {type(item)}")

    print("lista[1] = ", lista[1])
    print("lista[0:2] = ", lista[0:2])
    print("lista[:2] = ", lista[:2])
    print("lista[3:5] = ", lista[3:5])
    print("lista[3:6] = ", lista[3:6])
    print("lista[3:] = ", lista[3:])
    print("lista[-2] = ", lista[-2])
    print("lista[-1] = ", lista[-1])
    print("lista[4][1] = ", lista[4][1])
    # Listcomp
    linguagens = 'Python Java JavaScript C C# C++ Swift Go Kotlin'.split()
    print("Antes da listcomp = ", linguagens)
    # padrão Python de atualizar a lista para tudo minúsculo
    linguagens = [item.lower() for item in linguagens]
    print("Depois da listcomp = ", linguagens)
    # sem utilizar o padrão Listcomp
        linguagens = 'Python Java JavaScript C C# C++ Swift Go Kotlin'.split()
    print("Antes da listcomp = ", linguagens)
    for i, item in enumerate(linguagens):
        linguagens[i] = item.lower()
    print("\nDepois da listcomp = ", linguagens)
    linguagens_java = [item for item in linguagens if "Java" in item]
    print(linguagens_java)
    # Outra forma de fazer sem usar Listcomp
    linguagens_java = []
    for item in linguagens:
    if "Java" in item:
        linguagens_java.append(item)
    print(linguagens_java)
    # Exemplo 1
    print("Exemplo 1")
    linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()
    nova_lista = map(lambda x: x.lower(), linguagens)
    print(f"A nova lista é = {nova_lista}\n")
    nova_lista = list(nova_lista)
    print(f"Agora sim, a nova lista é = {nova_lista}")
    # Exemplo 2
    print("\n\nExemplo 2")
    numeros = [0, 1, 2, 3, 4, 5]
    quadrados = list(map(lambda x: x*x, numeros))
    print(f"Lista com o número elevado a ele mesmo = {quadrados}\n")
        # Gera uma lista com os números de 0 a 20
    numeros  = list(range(0, 21))
    # guarda os números pares
    numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
    # guarda os números ímpares
    numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))
    print(numeros_impares)
    print(numeros_pares)
    
def exemplos_basicos():
    lista=[1,2,3]
    lista=lista+[4,0,0,0]
    numero=lista[0]+lista[3]
    lista.append(9)
    lista.extend(['teste', 2, False])
    lista.remove(False)
    lista.pop(0) #Remover
    lista.count(0)#Número de vezes dessa ocorrência

    Mohs=['Talco', 'Gipsita', 'Calcita', 'Fluorita', 'Apatita', 'Ortoclásio', 'Quartzo', 'Topázio', 'Coríndon', 'Diamante']
    Mohs[::-1] #Classificando do trás para frente

    print(lista)
    print(f'{lista[0]} + {lista[3]} = ',numero)
    print(len(lista))
    print(lista[-1])
    print(lista[2:-2])
    lista[0] = 'zero'
    lista[1] = lista[1]+lista[2]
    print(lista)
    print('...')
    linha1=[1,2,3]
    linha2=[0,-1,1]
    linha3=[3,3,3]
    matriz=[linha1,linha2,linha3]

    for i in range(3):
        for j in range(3):
            print(matriz[i][j])
