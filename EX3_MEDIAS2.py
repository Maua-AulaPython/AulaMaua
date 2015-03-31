import math


lista = []

def media(lista):
    i = 0
    soma = 0
    for i in range (len(lista)):
        soma = soma + lista[i]
        media = soma/(len(lista))
    return media
    
a = 0
while a>=0:
    a = int(raw_input('digite a nota  '))
    lista.append(a)
    
    
print media (lista[:-1])

# Nota: 1.0
# Comentario: **
