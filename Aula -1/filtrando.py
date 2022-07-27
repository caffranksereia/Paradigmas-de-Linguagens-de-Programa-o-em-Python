from distutils.command.config import LANG_EXT
from dado import produtos, pessoas, lista



# nova_lista = filter(lambda x: x>5, lista)

# nova_lista = [x for x in lista if x>5]

def filtar(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False

nova_lista = filter(filtar, pessoas)

for n in nova_lista:
    print(n)

