def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)
    
def fala_oi(nome):
    return f'oi {nome}'
    
def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'
    
    
executation = mestre(fala_oi, 'salvo')
EX = mestre(saudacao,'salvo', saudacao='hola!')
print(executation)
print(EX)