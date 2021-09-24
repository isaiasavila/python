# Exemplos de manipulações com tempo
import time
# Tempo inicial
tInicial = time.localtime() # Retorna uma lista com as informações
salve = time.localtime()
print('Hoje é',salve[2],'do',salve[1],'de',salve[0]) # Usa a lista para apresentar informação
print(f'Hoje é {salve[2]} do {salve[1]} de {salve[0]}') # Mesma saída, melhor apresentada
#tFinal = time.localtime() - tInicial # Tempo final
import calendar
c = calendar.isleap(2004) # Ano bisexto?
print(str(c))
c = calendar.monthrange(2004, 5) # começa o mês (0-domingo, 1-segunda), quantos dias têm o mês
print(str(c))
calendar.prmonth(1922, 2) # Imprime mês do ano passado como parâmetro no terminal