#Função para gerar escolha aleatória
import random
import winsound
import time
from random import SystemRandom

class Aleatoriedade:

    def testes(self):
        sorteio = random.choice
        a = ['Woiski', 'Barata', 'Labaki', 'Bestinha', 'Osvaldo', 'Fred', 'Thiago', 'Regis']
        numero = random.random # Recebe número randômico

        for i in range(6):
            print(sorteio(a))
            print(int(5 * numero())) # Imprimi um número aleatório * 5

        b = winsound.Beep
        b(1000, 1000)
        b(500, 500)

        s = time.sleep
        for c in range(1, 10):
            for i in range(1, 5):
                for j in range(1, 5):
                    b(100 * j * i, 50)
                    s(0.01)
                s(0.01)

    # Exemplos de manipulações random
    def numeroAleatorio(self, tipo, min, max):
        import random
        if tipo == 0: #retorna um inteiro
            return random.randint(min, max)
        elif tipo == 1: #retorna um número real
            return random.random() + random.randint(min, max)
        else:
            return tipo

    def textoAleatorio(self, _listaPrimeiro, _listaSegundo = ''):
        import random
        p1 = _listaPrimeiro
        p2 = _listaSegundo
        saida = random.choice(p1)
        if _listaSegundo != '':
            saida += ' ' + random.choice(p2)
        return saida
        
    def textoAleatorio(self, _listaPrimeiro, _listaSegundo = ''):
        import random
        p1 = _listaPrimeiro
        p2 = _listaSegundo
        saida = random.choice(p1)
        if _listaSegundo != '':
            saida += ' ' + random.choice(p2)
        return saida

    
    