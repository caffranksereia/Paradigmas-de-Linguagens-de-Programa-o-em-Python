from dado import lista, pessoas, produtos


# nova_lista = map(lambda x: x * 2, lista)
# print(lista)
# print(list(nova_lista))


# for produto in produtos:
#     print(produto)

# def aumenta_preco(p):
#     p['preço'] = round(p['preço'] * 1.06, 2)
#     return p

# novos_produtos = map(aumenta_preco,produtos)

# for produto in novos_produtos:
#     print(produto)

# print(list(novos_produtos))

# for preco in precos:
#     print(preco)

# print(precos)

# nomes = map(lambda n: n['nome'], pessoas)

# for nome in nomes:
#     print(nome)

def aumento_idade(p):
    p['nova_iadde'] = round(p['idade'] * 1.20)
    return p 

idades= map(aumento_idade, pessoas)

for pessoa in idades:
    print(pessoa)
