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
   



















    