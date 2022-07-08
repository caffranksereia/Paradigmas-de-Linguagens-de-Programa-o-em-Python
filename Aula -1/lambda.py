"""
aqui estamos estudando a expressão lambda que ajuda a criar um parametro para outra função 
"""

lista = [
    ['arroz',10.79],
     ['feijao',7.9],
     ['abobora',1.00],
     ['kiwi',0.10],
     ['abacaxi',20]
    ]
lista.sort(key=lambda item:item[1], reverse=True)
print(lista)