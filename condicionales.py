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

print();
print('el valor total a pagar es de:','$',total);
print();
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

print();
print('el valor total a pagar es de:','$',totalc);
print();
print('el descuento fue de:','$',descuento);    
   
print('................................................')

#compañia de seguros
capital= int(input("ingrese el capital a financiar:"));

if capital<50000:
    interes=(capital*0.03);
else:
    interes=(capital*0.02);

pago= capital+interes;

print();
print('la cuota total es de:','$',pago);
print();
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

print();
print('el total de puntos recolectados en los  5 dias es:', sumad);
print();
print('el total de las ganancias de los 5 dias es de','$',sumag);
print();
print('la multa por contaminacion es de','$',multa);   
print(); 
print('el total de dinero recibido despues del proceso es','$',gd);

print('................................................')

#decremento aunal
precio_comun= int(input("ingrese el precio del carro y del terreno:"));
incremento= int(input("ingrese el incremento aunal del terreno:"));
decremento= int(input("ingrese el decremento aunal del carro:"));

incremento = (((precio_comun * incremento) / 100) * 3) / 2;
decremento = ((precio_comun * decremento) / 100) * 3;

print();
print('la mitad del incremento del terreno al pasar 3 años es de:','$', incremento);
print();
print('el decremento del carro al pasar 3 años es de','$',decremento);
print();
if decremento<incremento:
    print('conviene comprar el carro');
else:
    print('conviene comprar el terreno');
          
print('................................................')

#computadoras
numero_pc=int(input("ingrese la cantidad de computadoras a comprar:"));
precio=11000;
totalpc=numero_pc*precio;

if numero_pc<5:
   descuento_pc=totalpc*0.10;
if numero_pc>=5 and numero_pc<10:
    descuento_pc=totalpc*0.20;
else:
    descuento_pc=totalpc*0.40;

total_des= totalpc-descuento_pc;

print();
print('el valor total a pagar por',numero_pc,'computadoras es de:','$',total_des);
print();
print('el descuento aplicado es de',"$", descuento_pc);    
    
print('................................................')  

#electrodomesticos
precio_e=int(input("ingrese el precio del electrodomestico:"));
marca=(input("ingrese la marca del electrodomestico:"));
total=precio_e;
iva=16;

if marca=='nosy' and precio_e>=2000:
    descuento=precio_e*0.16;
if precio_e>2000:
    descuento=precio_e*0.10;
    
total_e = precio_e-descuento;
iva_e=(total_e*iva)/100;
total_final=total_e+iva_e;

print();
print('el total a pagar es','$',precio_e);
print();
print('el descuento aplicado es de','$',descuento);
print();
print('saldo total del iva','$',iva_e);
print();
print('el total del precio con iva incluido es de','$',total_final);    

print('................................................') 

#empreza
npiezas=int(input("ingrese el numero de piezas solicitado:"));
costo_p=int(input("ingrese el costo por pieza:"));
totalp=npiezas*costo_p;

if totalp>500000:
     invertir=totalp*0.55;
     prestamo=totalp*0.30;
     credito=totalp*0.15;
else:
     invertir=totalp*0.70;
     prestamo=totalp*0;
     credito=totalp*0.30;

interess=credito*0.20;

print();
print('costo de las piesas','$',totalp);
print();
print('el monto a invertir es de:','$',invertir);
print();
print('el monto del prestamo r es de:','$',prestamo);
print();
print('el monto del credito es de:','$',credito);
print();
print('el interes es de:','$', interess);
    
print('................................................')  

#operaciones
n1=int(input('digite el primer numero:'));
n2=int(input('digite el segundo numero:'));

if n1==n2:
    operacion=n1*n2;
if n1>n2:
    operacion=n1-n2;
if n1<n2:
    operacion=n1+n2;

print();
print('el resultado de la operacion es:', operacion);
    
print('................................................')  

#operaciones II
n1=int(input('digite el primer numero:'));
n2=int(input('digite el segundo numero:'));
n3=int(input('digite el tercer numero:'));
print();
if n1>n2 and n1>n3:
    print('el numero mayor es:',n1);
if n2>n1 and n2>n3:
    print('el numero mayor es:',n2);
if n3>n1 and n3>n2:
    print('el numero mayor es:',n3);    
    
print('................................................')  








    