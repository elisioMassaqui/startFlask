import os
import random
import subprocess

def chegamos(a=0, b=0):
    somadoAB = a + b
    lista = [1, 2, 3, 4, 5]
    for num in lista:
        num += 1
    print(num)

    x = 'chegamos'
    return f''' Numeros da lista adicionados: {num},
      Sua lista: {lista},
        a somado com b = {somadoAB} 
'''

def chegamosJsonfy(a=0, b=0):
    somadoAB = a + b
    lista = [1, 2, 3, 4, 5]
    for num in lista:
        num += 1
    print(num)

    x = 'chegamos'
    return f''' Numeros da lista adicionados: {num},
      Sua lista: {lista},
        a somado com b = {somadoAB} 
'''

def criarPasta():
    prefixo= 'wandi'
    sufixo = random.randint(10, 99)
    nomeWandi = f'{prefixo}{sufixo}'

    wandicode = os.path.join(os.path.expanduser('~'), 'Documents', nomeWandi)
    os.makedirs(wandicode)
    return f'Pasta{nomeWandi} criada com sucesso em {wandicode}'