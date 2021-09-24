import itertools

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
