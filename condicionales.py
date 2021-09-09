# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 00:22:09 2021

@author: oscar perez
"""
print('................................................')
#compra de comisa
cantidad=int(input("ingresar la cantidad de camisas:"));
precio=int(input("ingresar el precio:"));
compra= cantidad*precio;
if cantidad>=3:
    descuento=(compra*0.10);
else:
    descuento=(compra*0.20);
total= compra-descuento;
print('el valor total a pagar es de:','$',total);
print('el descuento fue de:','$',descuento);    

print('................................................')

#descuento concurso
total_compra= int(input("ingrese el precio total:"));
numero=int(input("estimado clienta escoja un numero y participe en el descuento:"));
if numero<74:
    descuento=(total_compra*0.15);
else:
    descuento=(total_compra*0.20);
totalc= total_compra-descuento;
print('el valor total a pagar es de:','$',totalc);
print('el descuento fue de:','$',descuento);    
   
print('................................................')

#compañia de seguros
capital= int(input("ingrese el capital a financiar:"));
if capital<50000:
    interes=(capital*0.03);
else:
    interes=(capital*0.02);
pago= capital+interes;
print('la cuota total es de:','$',pago);
print('el interes es de:','$',interes);    
   
print('................................................')

d1=int(input("ingrese puntos del dia 1:"));
d2=int(input("ingrese puntos del dia 2:"));
d3=int(input("ingrese puntos del dia 3:"));
d4=int(input("ingrese puntos del dia 4:"));
d5=int(input("ingrese puntos del dia 5:"));

sumad= d1+d2+d3+d4+d5;

g1=int(input("ingrese las ganancias del dia 1:"));
g2=int(input("ingrese las ganancias del dia 2:"));
g3=int(input("ingrese las ganancias del dia 3:"));
g4=int(input("ingrese las ganancias del dia 4:"));
g5=int(input("ingrese las ganancias del dia 5:"));

sumag= g1+g2+g3+g4+g5;

if sumad>170:
    multa=sumag*0.50;
else:
    multa=0;
gd= sumag-multa;
print('el total de puntos recolectados en los  5 dias es:', sumad);
print('el total de las ganancias de los 5 dias es de','$',sumag);
print('la multa por contaminacion es de','$',multa);    
print('el total de dinero recibido despues del proceso es','$',gd);

print('................................................')











    