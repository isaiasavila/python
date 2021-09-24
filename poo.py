class Pessoa():
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

class Nota_Fiscal():
    def __init__(self, nome, produto, preco):
        self.nome = nome
        self.produto = produto
        self.preço = preco

pes = Pessoa('Isaias',39,'m')
nf = Nota_Fiscal('Avila','Carro','50000.')
print(pes.nome)
print(nf.nome)