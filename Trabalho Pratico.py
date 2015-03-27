#Exercicio1
from math import *

X1 = int(raw_input('digite o X1 '))
Y1 = int(raw_input('digite o Y1 '))
X2 = int(raw_input('digite o X2 '))
Y2 = int(raw_input('digite o Y2 '))

def distancia (X1, Y1, X2, Y2):
    distancia = sqrt((X2-X1)**2 + (Y2-Y1)**2)
    return distancia

print ' a distancia entre os pontos:', distancia(X1,Y1,X2,Y2)

#Exercicio2

from math import *

lista = [(0,0),(2,4),(3,1), (-4,-6),(-7,-5)]

i = 0
j=i+1

def maiordistancia (lista):
    dmax = 0
    for i in range(len(lista)):
        X1 = lista [i][0]
        Y1 = lista [i][1]
        for j in range(len(lista)):     
            X2 = lista [(j)][0]
            Y2 = lista [(j)][1]
            d = sqrt((X2-X1)**2 + (Y2-Y1)**2)
            if (d > dmax):
                dmax = d
    print (dmax)
        

maiordistancia(lista)

#Exercicio3

from math import *

X1 = int(raw_input('digite o X1 '))
Y1 = int(raw_input('digite o Y1 '))
X2 = int(raw_input('digite o X2 '))
Y2 = int(raw_input('digite o Y2 '))

def modulo(x,y):
    modulo = sqrt((x**2) + (y**2))
    return modulo

def fase (x,y):
    fase = atan2(y,x)
    return fase

print 'Primeira coordenada: modulo: ' , modulo(X1,Y1) , 'fase: ', fase(X1,Y1)
print 'Segunda coordenada : modulo: ' , modulo(X2,Y2) , 'fase: ', fase(X2,Y2)

#Exercicio4

from math import *

a = int(raw_input('digite o primeiro cateto '))
b = int(raw_input('digite o segundo cateto '))
c = int(raw_input('digite a hipotenusa '))

if (a+b) > c:
    area = b*a/2
    print (' O triangulo retangulo e sua area vale: ' , area)
else:
        print (' o triangulo {0},{1},{2} nao e retangulo'.format (a,b,c))
        
#Exercicio5

from math import *


x = float(raw_input('digite o X '))
y = float(raw_input('digite o Y '))
z = float(raw_input('digite o Z '))



def gps (x,y,z):
    h = 0
    N = 1
    a = 6378160
    E = 0.00669454185
    i = 0

    lat = atan2(y,x)
    p = sqrt((x**2)+(y**2))

    aux = (z/p)* (1 - E)** -1
    teta = atan (aux)
    for i in range(5):
        N = a/ (sqrt(1 - E*sin(teta)**2))
        h = (p/cos(teta))-N
        aux = ((z/p)* (1 - E*N/(N+h))** -1)
        teta = atan(aux)
    teta1 = teta * 180/pi
    print lat,teta1,h

gps (x,y,z)
