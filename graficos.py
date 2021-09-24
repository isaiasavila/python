import pandas as pd
import matplotlib.pyplot as plt
import utilidades as ut

# df = pd.read_excel('C:\python\Gerentes.xlsx')
# ax = plt.subplots(figsize=(8,6))
dicionario = {
    'Player': ['Superman','Batman','Thanos','Deadpool','Thanos','Spider-man','Thor','Ironman','Wolverine','Blade','Captain America','Blackwidow'],
    'Year': [2015,2015,2015,2016,2016,2017,2017,2017,2019,2020,2019,2018],
    'Point': [23,43,45,65,76,36,23,78,89,76,92,87]
}
dfp = pd.DataFrame(list(dicionario.items()))
#columns=['Player', 'Year', 'Point']))
print(dfp)
while True:
    pais = input('Digite:')
    print(dfp.loc[dfp['Player'] == pais, ['Player','Year', 'Point']])

#ax.plot(x, y1, c='r', label='expoential')
#ax.plot(x, y2, c='g', label='Straight line')
#ut.menu('teste','','2')
#leg = plt.legend()

# ax.get_legend().remove()
# plt.show() 