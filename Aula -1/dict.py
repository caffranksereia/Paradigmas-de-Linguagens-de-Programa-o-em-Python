d1 = {
    'str': 'valor',
    123:'Outro valor',
    (1,2,3,4):'tupla',
    
}
'''d1['naoexiste'] = 'agora existe.'
if 'naoexiste' in d1:
    print(d1['naoexiste'])'''

#print(d1.get('nomedachave'))

'''d1['nomedachave'] = 'agora existe.'
if d1.get('nomedachave') is not None:
    print(d1.get('nomedachave'))
else:
    print('não existe')'''

'''print(d1)
del d1['str']'''
'''print('str' in d1)
print('valor' in d1.values())
print('str' in d1.keys())'''
for k , v in d1.items():
    '''print(k)
    print(k[0],k[1])'''
    print(k,v)


    d1 = {
    'str': 'valor',
    123:'Outro valor',
    (1,2,3,4):'tupla',
    
}
clients = {
     'id1' : {
         'name' : 'abobora',
         'music' : 'poetas no topo'
     },
     'id2' :{
         'name': 'imca',
         'music' : 'imca'
     },
 }
for clients_k, clients_v in clients.items():
     print(f'Esses são os ids {clients_k}')
     for clients_dadosk, clients_dadosv in clients.items():
         print(f'\t esses são os dados comparando {clients_dadosk} = {clients_dadosv}')



perguntas = {
    'perguntas1':{
        'pergunta': 'Quanto que é 2*2',
        'resposta': {
            'a':'1',
            'b':'2',
            'c':'4',
            'd':'5',
        },
        'resposta_certa':'b',
    
    },
    'perguntas2':{
        'pergunta': 'Quanto que é 3*2',
        'resposta': {
            'a':'4',
            'b':'10',
            'c':'6',
        },
        'resposta_certa':'c',
    
    }
}
for pk,pv in perguntas.items():
    print(f'{pk}:{pv["pergunta"]}')
    
    print('repostas:')
    for rk,rv in pv['resposta'].items():
        print(f'[{rk}]:{rv}')
        
        resposta_aluno = input('resposta:')
'''print(perguntas)'''