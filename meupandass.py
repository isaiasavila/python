# Exemplos de pandas (classes geralmente utilizadas junto, NumPy[melhor uso é com numeros], SciPy)
import pandas as pd # Convenção internacional
#from pandas import Series, DataFrame # Muito utilizado com a biblioteca

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