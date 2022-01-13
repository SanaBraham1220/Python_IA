# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 11:21:17 2022

@author: Sana Braham
"""

import numpy as np;

#Matrice 1d
a=[1,2,4,6,9,10]
M_a= np.array(a)
print(M_a)

#Matrice 2d
b=[[1,5,6],[10,9,1],[12,8,7]]
M_b= np.array(b)
print(M_b)

#Create Matrice using range 
M_c = np.array([range(i,i+3) for i in [2,4,6]])
print(M_c)

#We can define the structure of column U5,i2,f4 (convention) 
M_d = np.array([('x',3,4.2),('y',4,5.3),('z',5,6.3)],
           dtype =[('name','U5'),('number','i2'),
                   ('value','f4')])
print(M_d)

#empty matrice
M_e = np.empty((3,2))

print(M_e)

#to get only one number between 1 and 10
aa = np.random.uniform(1,10)
#to get 20 numbers between 1 and 10
bb = np.random.uniform(1,10,20)

print("one random number:",aa)
print('-------------------------')
print("20 random numbers",bb)
print('-------------------------')

#to get a random matrice , the numbers are between 0 and 1
M_f= np.random.random((3,2))
print(M_f)
