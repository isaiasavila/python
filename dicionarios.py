#Dicionários
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