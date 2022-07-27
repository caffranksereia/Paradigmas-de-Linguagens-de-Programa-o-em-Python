# try:
#     print(a)
# except:
#     print('errado esta')
try:
    a = 0
    try:
        a=1/0
    except:
        print('erro')

except NameError as erro:
    print('Algo esta errado', erro)
except (IndexError,KeyError) as erro:
    print('erro de index ou chaves')
except Exception as erro:
    print('erro inesperado')
else:
    pass
finally:
    a =''

print(a)