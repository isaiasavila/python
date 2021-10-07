import itertools
import numpy as np

def funcoes_array_numpy():
    # Cria matriz 1 linha e 1 coluna
    matriz_1_1 = np.array([1, 2, 3])
    # Cria matriz 2 linhas e 2 colunas
    matriz_2_2 = np.array([[1, 2], [3, 4]])
    # Cria matriz 3 linhas e 2 colunas
    matriz_3_2 = np.array([[1, 2], [3, 4], [5, 6]])
    # Cria matriz 2 linhas e 3 colunas
    matriz_2_3 = np.array([[1, 2, 3], [4, 5, 6]])
    print(type(matriz_1_1))
    print('\n matriz_1_1 = ', matriz_1_1)
    print('\n matriz_2_2 = \n', matriz_2_2)
    print('\n matriz_3_2 = \n', matriz_3_2)
    print('\n matriz_2_3 = \n', matriz_2_3)
    # Cria matriz 3 x 3 somente com zero
    m1 = np.zeros((3, 3))
    # Cria matriz 2 x 2 somente com um
    m2 = np.ones((2,2))
    # Cria matriz 4 x 4 identidade
    m3 = np.eye(4)
    # Cria matriz 2 X 5 com números inteiros
    m4 = np.random.randint(low=0, high=100, size=10).reshape(2, 5)
    print('\n np.zeros((3, 3)) = \n', np.zeros((3, 3)))
    print('\n np.ones((2,2)) = \n', np.ones((2,2)))
    print('\n np.eye(4) = \n', np.eye(4))
    print('\n m4 = \n', m4)
    print(f"Soma dos valores em m4 = {m4.sum()}")
    print(f"Valor mínimo em m4 = {m4.min()}")
    print(f"Valor máximo em m4 = {m4.max()}")
    print(f"Média dos valores em m4 = {m4.mean()}")
    
def attempt_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x

def abrirArquivo():
    
    path = 'c:/teste.tnts'
    with open(path) as f:
        lines = [x.rstrip() for x in f]

    #f = open(path, 'w') #padrão usa r
    lines = [x.rstrip() for x in open(path)]
    try:
        f.seek(1)
    except:
        print('Failed')
    else:
        print('Succeeded')
    finally:
        f.close()

first_letter = lambda x: x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names)) # names é um gerador

a = ['João', 'Rafael', 'Douglas']
for x in a:
    print('%s tem %i letras' %(x,len(x)))

x = input('...')
