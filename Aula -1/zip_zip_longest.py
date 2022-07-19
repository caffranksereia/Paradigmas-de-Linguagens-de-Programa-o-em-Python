"""
zip - uninfo iteraveis
zip_longest - itertools
"""
from itertools import zip_longest, count

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']
index = count()
cidades_estados = zip(
    index,
    cidades,
    estados
)
for index, estados, cidades in cidades_estados:
    print(index, estados, cidades)

# print(cidades_estados)
# print(list(cidades_estados))
# print(list(cidades_estados))

# for valor in cidades_estados:
#     print(valor)