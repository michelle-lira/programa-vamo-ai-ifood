# importa a biblioteca matplotlib e o módulo pyplot, da mesma biblioteca
import matplotlib.pyplot
# cria uma lista com os meses do ano
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril',
'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
'Outubro', 'Novembro', 'Dezembro']
# cria uma lista de valores
valores = [234, 345, 765, 897, 342, 879, 132, 564,
888, 333, 938, 895]
# cria o gráfico e passa meses e valores como parâmetro
matplotlib.pyplot.plot(meses, valores)
# mostra o gráfico
matplotlib.pyplot.show()