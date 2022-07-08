def primeira_func(segunda_func):
    return segunda_func()
    
def segunda_func(x,y):
    soma = x+y
    return soma
    
    
a = 10
b = 300

segunda1 = segunda_func(a,b)

print(segunda1)