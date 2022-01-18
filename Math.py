# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 12:54:07 2022

@author: Sana Braham
"""

import math as m

# Factorial
a = m.factorial(7)
print(7*6*5*4*3*2*1)
print(a)

#exponentiel e=2.718
b= m.exp(3)
print(2.718*2.718*2.718)
print(2.718**3)
print(b)

#fonction logarithme népérien (base=e=2.718)
c=m.log(7)
print(c)

#fonction logarithme decimale (base=10)
f=m.log10(10000)
print(f)

#fonction logarithme  (base=x) m.log(x,y)
d=m.log(7,2.718)
e=m.log(10,1000)
print(d,e)

#la racine carrée
g=m.sqrt(81)
print(g)

#degree vs radians
'''
180°=pi
90°=pi/2
60°=pi/3
45°=pi/4
15°=pi/6
'''
h=m.degrees(m.pi)
i=m.radians(180)
print(h,i)

# sin(x) : x mesured in radians
k=m.sin(m.pi/2)
l=m.sin(m.radians(90))
print(k,l)


#constantes
print("e=", m.e)
print("pi=", m.pi)
print("infinity=",m.inf)

#copysign(a,b)  attribuer le signe de b pour a 
print(m.copysign(7,-3))
print(m.copysign(7,23))
print(m.copysign(-7,-93))
print(m.copysign(7,3))

#ceil
print("arrondi sup:",m.ceil(8.3))
print("arrondi inf:",m.floor(8.3))