#Listas
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