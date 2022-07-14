l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [x for x in l]
print(l2)
l1 = [x*2 for x in l]
print(l1)
l3 = [(x ,ls) for x in l for ls in range(3)]
print(l3)
l4 = ['arroba','peixe','bola','gato']
ex5 =[v.replace('a','*') for v in l4 ]
print(ex5)
tupla = (
    ('chave','valor'),
    ('chave2','valor2')
) 
ex6 =[(x,y) for x,y in tupla]
ex6 = dict(ex6)
print(ex6)
l3 = list(range(100))
ex=[x for x in l3 if x %2 ==0 if x % 3 ==0]
print(ex)
ex1 =  [v if v %2 ==0 else 'impar' if v %3==0 else'impar']
print(ex1)