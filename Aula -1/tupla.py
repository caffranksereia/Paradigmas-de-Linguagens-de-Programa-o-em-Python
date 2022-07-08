"""
as tuplas voce não pode modificar

"""

t1 = (1,2,3,4,'abacaxi','arroz')
print(t1)


for x in t1: #mostra em forma de lista
    print(x)
    
for y in range(len(t1)): #tamanho da tuple
    print(y)

tup = () #posso criar uma tuple assim e..'''
tup2 = 1, #tambem assim '''
#posso concatenar as tuple
tx = 123,2314,345,'n10'
ty = 12334233654,4354675,234156

tz = tx+ty
print(tz)
tz = list(tz)#virou uma lista ai posso modificar
tz[1] = 2134 #modifiquei
print(tz)
print(type(tup))
print(type(tup2))