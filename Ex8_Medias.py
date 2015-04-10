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
print 'a maior nota é: {0}' .format(maior)
