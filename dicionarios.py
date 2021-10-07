#Dicionários
def funcoes_basicas():
    dici_1 = {}
    dici_1['nome'] = "João"
    dici_1['idade'] = 30
    # Exemplo 2 - Criação de dicionário usando um par elementos na forma, chave : valor
    dici_2 = {'nome': 'João', 'idade': 30}
    # Exemplo 3 - Criação de dicionário com uma lista de tuplas. Cada tupla representa um par chave : valor
    dici_3 = dict([('nome', "João"), ('idade', 30)])
    # Exemplo 4 - Criação de dicionário com a função built-in zip() e duas listas, uma com as chaves, outra com os valores.
    dici_4 = dict(zip(['nome', 'idade'], ["João", 30]))
    # Testando se as diferentes construções resultam em objetos iguais.
    print(dici_1 == dici_2 == dici_3 == dici_4)
    # Exemplo 1 - Criação de dicionário vazio, com atribuição posterior de chave e valor 
    cadastro = {
                'nome' : ['João', 'Ana', 'Pedro', 'Marcela'],
                'cidade' : ['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Curitiba'],
                'idade' : [25, 33, 37, 18]
                }
    print("len(cadastro) = ", len(cadastro))
    print("\n cadastro.keys() = \n", cadastro.keys())
    print("\n cadastro.values() = \n", cadastro.values())
    print("\n cadastro.items() = \n", cadastro.items())
    print("\n cadastro['nome'] = ", cadastro['nome'])
    print("\n cadastro['nome'][2] = ", cadastro['nome'][2])
    print("\n cadastro['idade'][2:] = ", cadastro['idade'][2:])
    print(len(cadastro['nome']))
    print(len(cadastro['cidade']))
    print(len(cadastro['idade']))
    qtde_itens = sum([len(cadastro[chave]) for chave in cadastro])
    print(f"\n\nQuantidade de elementos no dicionário = {qtde_itens}")
    
def exemplo_um():
    aurelio={'denomiação':'ilha solteira','população':23000,'renda':1500}
    print(aurelio)
    aurelio['vocação']='turismo'
    print(aurelio)
    aurelio['renda']+=200
    print(aurelio)
    print(aurelio.keys())
    print(aurelio.items())

def exemplo_dois():
    empty_dict = {}
    d1 = {'a' : 'some value', 'b' : [1, 2, 3, 4]}
    d1[7] = 'an integer'
    print(d1)
    print(d1['b'], ' ', d1[7])
    d1[5] = 'some value'
    d1['dummy'] = 'another value'
    print(d1[5], ' ', d1['dummy'])
    del d1[5]
    d1.pop('dummy')
    print(list(d1.keys()))
    print(list(d1.values()))
    d1.update({'b' : 'foo', 'c' : 12})
    print(d1)
    key_list = [1, 2, 3]
    value_list = ['a', 'b', 'c']
    mapping = {}
    for key, value in zip(key_list, value_list):
        mapping[key] = value
    mapping = dict(zip(range(5), reversed(range(5))))
    words = ['apple', 'bat', 'bar', 'atom', 'book']
    by_letter = {}
    for word in words:
        letter = word[0]
        if letter not in by_letter:
            by_letter[letter] = [word]
        else:
            by_letter[letter].append(word)
    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7, 8}
    a.union(b)
    b.add(9)
    a | b
    a.intersection(b)
    a & b
# using Python to showcase dictionary comprehension
# creation of two lists to represent keys and values
#id = '', idade = '', peso = '', genero = '', habitat = '', especie = '', nome = '', dataDeEntrada = '', origem = ''):
# for i in range(20):
#     keys = ['id', 'peso', 'genero', 'habitat', 'especie', 'nome']
#     values = ['m{i}', 10 + i, 'Macho' 'Savana', 'Macaco', 'João']
# # implementing dictionary comprehension
# new_dict = { k:v for (k,v) in zip(keys, values)}
# print(new_dict)
