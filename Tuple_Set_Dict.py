# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 06:56:20 2022

@author: Sana Braham
"""
#############################Tuple#############################################
#set doesn't contain duplicate values => output 12,8,9,10
a ={12,8,9,10,8}
print(a)

#tuple is not mutable
b=(12,15,17,18)

#dict
my_dict={1:"sana",2:"sondes"}

print("=================tuple===============================")
print(b[0]) # access by index
print(b[1:]) #slicing
t=('sab',True,1,'ok') #contain mixed data type
print(t)
t=(4,4,4)#contain duplicate values
print(t)

# we can convert tuple to list / list to tuple
list1=[1,'rr',55,'tyyuy']
tuple1=('rrrrr',56666,'ZEEEE')
print("liste=",list1)
print("tuple=",tuple1)
tuplelist1=tuple(list1)
print("list converted to tuple:",tuplelist1)
listtuple1=list(tuple1)
print("tuple converted to list:",listtuple1)

#we can write tuple with () or without ()
t1=1,2,3
print(t1)
t2=(1,2,3)
print(t2)

############################Set################################################

seta = {1,12,14,6,9,1,2,8,14}
print(seta) #elimine les doublous et fait l'ordre croissant

setb = {'A','b','A','r','k','a','A'}
print(setb) #elimine les doublous et ne fait pas l'ordre pour String