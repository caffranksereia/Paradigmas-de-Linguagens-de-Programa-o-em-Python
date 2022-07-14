string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789'
n= 10
lista_ex = [string [x:x +n] for x in range(0,len(string),n)]
retorno = '.'.join(lista_ex)
print(lista_ex)
print(retorno)