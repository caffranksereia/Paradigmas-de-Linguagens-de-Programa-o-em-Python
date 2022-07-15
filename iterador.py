# carrinho = [(1,'carrinho',10),(2,'requeijao',20),(2,'requeijao',20),
# (2,'requeijao',40),(2,'requeijao',60)]
# print(carrinho[1])


carrinho = []

carrinho.append(('carrinho',10))
carrinho.append(('requeijao',20))
carrinho.append(('requeijao',30))
carrinho.append(('requeijao',40))
carrinho.append(('requeijao',60))


total = sum([y for x,y in carrinho])
print(total)
# print(carrinho)
# print(carrinho[1])
# for produto in carrinho:
#     total +=produto[1]
# print(total)


