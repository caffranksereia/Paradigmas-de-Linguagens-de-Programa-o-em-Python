from dado import produtos, pessoas, lista
from functools import reduce


# soma_lista = reduce(lambda ad,i :i['preço'] +ad,produtos,0)


# print(soma_lista/len(produtos))

soma_idade = reduce(lambda zc, p: zc+p['idade'], pessoas, 0)


print(soma_idade/ len(pessoas))