def soma_mais_tres(n1,n2):
    porcento = n1 *float(n2)/100
    print('this',porcento)
    soma = n1+porcento
    return soma

numero_soma = int(input('numero:'))
porcentagem = float(input('Porcentagem:'))
result = soma_mais_tres(numero_soma,porcentagem)
print(result)