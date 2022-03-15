numero = int(input('Digite um numero:'))
numero_1 = int(input('Digite:'))
op =input("Escolha op (+/-*):")


if op=='+':
    res = numero + numero_1
    print(res)
    print("essa é a sua resposta da conta {},{} resposta {}." .format(numero,numero_1,res))
elif op=='-':
    res = numero - numero_1
    print(res)
    print("essa é a sua resposta da conta {},{} resposta {}." .format(numero,numero_1,res))
elif op=='*':
    res = numero * numero_1
    print(res)
    print("essa é a sua resposta da conta {},{} resposta {}." .format(numero,numero_1,res))
elif op=='/':
    res = numero / numero_1
    print("essa é a sua resposta da conta {},{} resposta {}." .format(numero,numero_1,res))
else:
    ('dunno')
print('thats it')