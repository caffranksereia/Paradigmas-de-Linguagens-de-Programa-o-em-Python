'''Sets só recebe valores
    Não tenho acessos nos valores do set
    add adiciona
    update atualiza
    discard apagar


s1 = {1,2,3,4,5,6}
s1.add(60)
s1.discard(3)
s1.update('Python')
print(s1)
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_differece ^(elementos que estão nos dois sets, mas não me ambos)

'''

'''l1 = {1,2,3,4,5,7}
l2 = {1,2,3,4,5,6}
s3 = l1 | l2
s4 = l1 & l2
s5 = l2 - l1
s6 = l1 ^ l2
print(s6)
print(s5)
print(s4)
print(s3)'''

l1 = ['fabio','joao','jessica']
l2 = ['fabio','joao','jessica','Luiz','Luiz']
if set(l1) == set(l2):
    print('ambos são iguais')
else:
    print('tem alguns elemenos que estão presente em um mas no outro não ')