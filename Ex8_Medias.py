import math
import sys

lista = []

def media(lista):
    i = 0
    soma = 0
    for i in range (len(lista)):
        soma = soma + lista[i]
        media = soma/(len(lista))
    return media

maior = 0   
a = 0
while a>=0:
    while True:
        try:
            a = float(raw_input('digite a nota  '))
            if (maior < a):
                maior = a
            break
        except:
            print ' voce nao digitou um numero valido'
    lista.append(a)
   
print ' media: ', media (lista[:-1])
print 'a maior nota e: {0}' .format(maior)

#Nota: 1.1
#Comentario: Valia 1.0, mas dei mais 0.1 por calcular a maior nota em uma unica linha
