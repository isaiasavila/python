# Pandas [funções de utilidades]
# NumPy [funciona melhor quando se trabalha com números]
# SciPy [Arrays, funções matemáticas]
import pandas as pd

class Manipular_Pandas:
    #from pandas import Series, DataFrame # Muito utilizado com a biblioteca
    def testes(self):
        obj = pd.Series([4, 7, -5, 3]) # Semelhante ao array do NumPy
        obj.values
        obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c']) # Cria um array e adiciona um index, algo parecido com o dicionário?
        obj2.index
        'b' in obj2 # retorna True 
        'e' in obj2 # retorna False
        sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
        obj3 = pd.Series(sdata) # Uma Series recebe um dicionário, por estar na biblioteca pandas, melhor usar ela ao invés de um dicionário
        states = ['California', 'Ohio', 'Oregon', 'Texas']
        obj4 = pd.Series(sdata, index=states) # Associamos a Series ao obj4 porém usando o índice criado na linha acima
        pd.isnull(obj4) # Detecta dados ausentes
        pd.notnull(obj4) # Detecta dados ausentes
        obj4.isnull() # Utilizando um método agora, mesmo utilidade que acima?
        obj3 + obj4 # Alinhamento de dados
        obj4.name = 'population' # Um índice de Series pode ser alterado in-place por atribuição
        obj4.index.name = 'state' # Um índice de Series pode ser alterado in-place por atribuição
        obj
        obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']

        players_data = {
            'Player': ['Superman','Batman','Thanos','Deadpool','Thanos','Spider-man','Thor','Ironman','Wolverine','Blade','Captain America','Blackwidow'],
            'Year': [2015,2015,2015,2016,2016,2017,2017,2017,2019,2020,2019,2018],
            'Point': [23,43,45,65,76,36,23,78,89,76,92,87]
        }

        df = pd.DataFrame(players_data)
        print(df)
        group_df = df.groupby('Player')

        for player, group in group_df:
            print(f'-------- {player} --------')
            print(f'{group}\n')

        best_df = df.loc[df.Point>60]
        print(best_df)
        best_df = df.loc[(df.Point>60)|(df.Player!='Ironman')&(df.Player!='Batman')]
        print(best_df)
        print(best_df.shape)
        print(best_df.describe())
        print(best_df[['Player','Point']].head())
        #best_df = pd.read_csv("C:\python\dados.csv")
        #print('1.\n',best_df)
        vendas_df = pd.read_excel('C:\python\Vendas.xlsx') # Não funciona por quê? 'Vendas.xlsx'
        #print(vendas_df.loc(0)) # Busca por índice
        #print(vendas_df.head(3), '...', vendas_df.loc[0:3])
        # Procuro o que eu quero e listo só as colunas que tem necessidade
        print(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['ID Loja','Produto','Quantidade']])
        print(vendas_df.loc[1,'Produto'])
        vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
        vendas_df.loc[:, 'Imposto'] = 0
        print(vendas_df['Comissão'],'',vendas_df['Imposto'])
        players_data = pd.read_excel('C:\python\Vendas.xlsx')
        vendas_df.append(players_data)
        #vendas_df = vendas_df.drop(0, axis=0)
        # Apaga o vazio em todo o eixo selecionado
        #vendas_df = vendas_df.dropna(how=all, axis=1)
        # Apaga a linha se algo estiver em branco
        #vendas_df = vendas_df.dropna()
        # Preenche o nAm com o valor especificado
        #vendas_df['Comissão'] = vendas_df['Comissão'].fillna(vendas_df['Comissão'].mean())
        #print(vendas_df)
        #vendas_df = vendas_df.ffill()
        #print(vendas_df)
        df = vendas_df['ID Loja'].value_counts()
        print(df)
        df = vendas_df.groupby('Produto').sum()
        print(df)
        gerentes_df = pd.read_excel('C:\python\Gerentes.xlsx')
        vendas_df.merge(gerentes_df)
        input('...')

class NBAPlayers:
    def __init__(self):
        '''
        Busca o dataset que será utilizado pela classe
        '''
        self._ds = pd.read_csv('https://raw.githubusercontent.com/isaiasavila/datasets/main/Players.csv')

    def valores_unicos(self, _nome_coluna):
        '''
        Retorna uma lista dos elementos únicos com base na ocorrência.
        Retorna a quantidade de valores distintos da coluna.
        '''
        print('Elementos únicos:\n')
        print(self._ds[_nome_coluna].unique())
        print('Quantidade de elementos únicos:\n')
        print(self._ds[_nome_coluna].nunique())

    def estatistica(self):
        '''
        Retorna as estatísticas descritivas, como média, desvio padrão, máximo, mínimo e outras tendências
        centrais, além da forma da distribuição.
        '''
        print(self._ds.describe())
    
    def classificar(self,_nome_colunas,_crescente=True):
        '''
        Retorna um dataset classificado pela(s) coluna(s) desejadas
        pode ser ordenado por várias colunas, o padrão é True de ascending
        '''
        print(self._ds.sort_values(by=_nome_colunas, ascending=_crescente))

    def contar_valores(self, _nome_colunas):
        '''
        Retorna o valor da contagem para cada item exclusivo presente na coluna.
        '''
        print(self._ds[_nome_colunas].value_counts())

    def nulo(self):
        '''
        Retorna a quantidade de valores nulos no dataset criado para a classe
        '''
        for col in self._ds.columns:
            if self._ds[col].isnull().sum() > 0:
                total_nulos = self._ds[col].isnull().sum()
                porcentagem = round(total_nulos * 100 / len(self._ds),2)
                print(f'Coluna {col} possui um total de {total_nulos} valores nulos: {porcentagem}%')

    def completar_valores(self, _nome_coluna):
        '''
        Valores nulos são preenchidos com um valor baseado na média 
        '''
        self._ds[_nome_coluna].fillna(value=self._ds[_nome_coluna].median(),inplace=True)
        self._ds[_nome_coluna].isnull().sum()
        print(self._ds)
    
    def agrupar_valores(self, _agrupador, _parametro):
        '''
        Retorna valores agrupados para utilização com outras funções
        '''
        print(self._ds.groupby([_agrupador])[_parametro].agg(['max','min','mean','median']))

    def alterar_valores(self):
        '''
        Altera valores passados como parâmetros em forma de dicionário
        '''
        parametros = {1918:0, 1921:3}

        print(self._ds['born'].map(parametros))

    def aplicar_mudanca_mt_pol(self):
        '''
        Aplica as modificações de altura no dataframe
        '''
        def converte_para_polegada(metro):
            return metro / 100 * 39,37
        
        print(self._ds['height'].apply(converte_para_polegada))

    def aplicar_faixa_altura(self, _coluna, _coluna_nova):
        '''
        Aplica uma criação de faixa de altura
        '''
        self._ds[_coluna_nova] = self._ds[_coluna].apply(lambda x : 1 if x<=180 else 
                                   (2 if x>180 and x<=200 else 3))
        # return  self._ds

    def aplicar_faixa_peso(self, _coluna, _coluna_nova):
        '''
        Aplica uma criação de faixa de peso
        '''
        self._ds[_coluna_nova] = self._ds[_coluna].apply(lambda x : 1 if x<85 else 2)
        # return self._ds

    def pivo(self, _indice, _coluna, _valor):
        '''
        Retorna um dataframe manipulado baseado no índice ou valor de coluna
        '''
        print(self._ds.pivot(index=_indice, columns=_coluna, values=_valor))

# ds = NBAPlayers()
# opcoes = ('0-pivot','1-(n)unique','2-describe','3-sort_values','4-value_counts','5-is_null','6-fillna',\
#          '7-groupby','8-map','9-apply')
# while True:
#     print(opcoes)
#     opcao = input('Escolha: ')
#     if opcao == '1':
#         ds.valores_unicos('Player')
#     elif opcao == '2':
#         ds.estatistica()
#     elif opcao == '3':
#         ds.classificar(['Player','height'], False)
#     elif opcao == '4':
#         ds.contar_valores(['height','weight'])
#     elif opcao == '5':
#         ds.nulo()
#     elif opcao == '6':
#         ds.completar_valores('born')
#     elif opcao == '7':
#         ds.agrupar_valores('birth_city','height')
#     elif opcao == '8':
#         ds.alterar_valores()
#     elif opcao == '9':
#         ds.aplicar_mudanca_mt_pol()
#     elif opcao == '0':
#         ds.aplicar_faixa_altura('height','range')
#         ds.aplicar_faixa_peso('weight','mesure')
#         teste = ds._ds
#         df = pd.DataFrame({'Class':['1st','2nd','3rd','1st','2nd','3rd'],'Section':['A','A','A','B','B','B'],'Gr':[1,2,3,4,5,6]})
#         print(df,'......')
#         print(df.pivot(index='Class', columns='Section',values='Gr'))
#     else:
#         break

class Titanic:

    def __init__(self):
        self.df = pd.read_csv('https://github.com/isaiasavila/datasets/raw/main/train.csv')

    def show_dataframe(self):
        print(self.df)

    def tipo_dados(self):
        '''
        Mostrar o tipo dos dados do dataset
        '''
        print(type(self.df))
        print(self.df.dtypes)

    def selecionar_numericos(self):
        '''
        '''
        self.df.select_dtypes(include='number')
        self.show_dataframe()

    def selecionar_objetos(self):
        '''
        '''
        self.df.df.select_dtypes(include='object')
        self.show_dataframe()

    def selecionar_datas(self):
        '''
        '''
        self.df.select_dtypes(include='datetime')
        self.show_dataframe()

    def naoselecionar_varios(self, parametros):
        '''
        '''
        self.df.select_dtypes(exclude=parametros)
        self.show_dataframe()

    def selecionar_varios(self, parametros):
        '''
        '''
        self.df.select_dtypes(include=parametros)
        self.show_dataframe()

    def converter_coluna(self, coluna):
        '''
        '''
        # Uma opção para alterar o tipo de coluna
        # self.df[coluna] = self.df[coluna].astype(int)
        # Uma outra opção para alterar o tipo de coluna
        # self.df = self.df.astype({coluna: 'int'})
        # A melhor opção para alterar o tipo de coluna
        self.df[coluna] = pd.to_numeric(self.df[coluna], errors='coerce')
        self.show_dataframe()

ds = Titanic()
opcoes = ('1-type','2-select|type')

while True:
    print(opcoes)
    opcao = input('Escolha: ')
    if opcao == '1':
        ds.tipo_dados()
    elif opcao == '2':
        ds.selecionar_varios(['int', 'datetime', 'object'])
    else:
        break