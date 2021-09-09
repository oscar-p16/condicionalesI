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
print('el descuento fue de:','$',descuento)    
