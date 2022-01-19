# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 10:53:25 2022

@author: Sana Braham
"""
#Lists can contain different data type
L = []
s = [1,2,3,6,9,8,7]
s = [ 'sam' , 5 , 3.2 , 5+2j ] 
s = [ 2 , 3, [ 4 , 5 ] ]


print("=============================================")

#Covert String to a list
a = "Hello world !"
print(list(a))
b="sana"
b1,b2,b3,b4 = list(b)
print(b1,b2,b3,b4)

print("=============================================")

#yes for access by index or sclicing
print(a[4])
print(a[:4])

#yes it's mutable
l=[1,2,4,9,7,12,6]
l[0]=10
print(l)
l[1]=[9,7,15]
print(l)
l[2:4]=[]
print(l) #c'est une facon que permet de vider la liste , il ya d'autres methodes pour le supprimer
l[:] = []
print(l)


print("=============================================")
#liste qui contient des liste
A =[[8,2,3,41],[7,12,14],[8,2,3,41],'rrrr',1,1,1]
A[2]=[8,2,41]
print(A[0][2])
print(A)

#comment supprimer un élement(3facons)
B=[1,5,'a','f',45,47,120,844,963,1200,5222,744]
B[3:6]=[]
del(B[0])
B.remove('a')
B.pop(2) #supprimer l'élement d'index 2 default index = last one
print(B)


#comment supprimer une liste (2facons)
C=[1,5,'a','f',45,47,120]
del(C)
D=[1,5,'a','f',45,47,120]
D[:]=[] #c'est une facon que permet de vider la liste 
print(D)

print("=============================================")
#additioner 3 listes
a=[1,5,'rrr']
b=[True,False,5]
f=["",""]
c=a+b+f
print(c)
b.extend(a)
print(b)

print("************************************************")
#multiplier une liste
k=a*2
print("k=",k)
h=[0]*1000
# print(h)
m=[3.0]*1000
# print(m)
m=['s']*1000
# print(m)
x = [[0]*8] *10 #10 lignes et 8 colonnes
# print(x)

#calculer la somme des elements de liste (only for list of number)
ff=[1,12,5,9,6,7,8,9]
print("somme=",sum(ff))

#count the number of items of list for numbers , strings and mixed data
dd=['r','w','d']
print("somme=",len(ff),len(dd))

#the max of list that contain only numbers or only strings
print("Max Letter: %s  and Max Number : %d" %(max(dd),max(ff)))
#the min of list that contain only numbers or only strings
print("Min Letter: %s  and Min Number : %d" %(min(dd),min(ff)))

#Trier la liste à l'ordre croissant (reverse = True) à l'ordre decroissant (reverse = False) sans modifier la liste originale
print(ff)
print(sorted(ff,reverse = True))
print(sorted(ff,reverse = False))
print("=============================================")
#Trier la liste en modifiant la liste originale à l'ordre croissant (reverse = True) à l'ordre decroissant (reverse = False)
print(ff)
ff.sort(reverse=True)
print(ff)
ff.sort(reverse=False)
print(ff)

#sorted with key 
m= [('At', 85), ('Br', 35), ('Cl', 17), ('F', 9), ('I', 53),('pr', 35), ('xl', 17), ('u', 9)]
ms=sorted(m,key=lambda item:item[0])
print(ms)
ms=sorted(m,key=lambda item:item[1])
print(ms)

print("=============================================")
#sorted with key and reverse
m= [('At', 85), ('Br', 35), ('Cl', 17), ('F', 9), ('I', 53),('pr', 35), ('xl', 17), ('u', 9)]
ms=sorted(m,key=lambda item:item[0] , reverse=True)
print(ms)
ms=sorted(m,key=lambda item:item[1],reverse=False)
print(ms)

#stringObject.Split() returns a list default sep=" "
str= "I love my sons Mohamed Seddik and Ayoub"
print(str.split())
str= "I_love_my_sons_Mohamed_Seddik_and_Ayoub"
print(str.split(sep='_',maxsplit=5))#split only the first fifth ones


print("=============================================")
#tester si un element existe ou non dans une liste
print(ff)
print(5 in ff)
print(555 in ff)
print(dd)
print('r' in dd)
print('m' in dd)

#append():ajouter seulement un element1
list1=[12,8,7,'r','t',8,8]
list1.append(80)#automatiquement l'ajout se fait à la fin de liste
list1.insert(3,'hello')
print(list1)

#count() : compter l'occurance
print("Nbre d'occurance:",list1.count(8))

#connaitre l'index d'un element
print(list1.index(8)) #la premiere occurance
# print(list1.index(744)) #error if the element isn't in the list


print("=============================================")
#renverser la list
print(list1)
list1.reverse()
print(list1)


print("=============================================")
list2=[2,8,9,'a','b']
list2.pop() # the last element
list2.pop(2) #
print(list2)


print("=============================================")  
a=range(30) # range(14,30) the default start is 0
print(a) 
print(list(a)) 
b=list(range(1,100,2))  #range with step=2
print(b)

print("=============================================") 
y=list( i**2 for i in range(10)) 
print(y)
y=[ i**2 for i in range(10)]
print("y =",y)

z=list(map(lambda x : x**2 , range(10)))
print("z =",z)

f=[(x,y) for x in [1,2,3] for y in [3,5,7] if x!=y] #2 boucles for imbriquées python
print(f)

list2=[[0 for i in range(5)] for j in range(7)] #creer une liste null 7 lignes 5 colonnes
print(list2)


print("********************************************************************")
x = iter([0,1,2,3,4,5,6,7,8,9])

print(next(x)) #iteration1
print(next(x)) #iteration2
print(next(x)) #iteration3
print(next(x)) #iteration4
print(next(x)) #iteration5


i = iter(range(10))
print(next(i)) #iteration1
print(next(i)) #iteration2
print(next(i)) #iteration3
print(next(i)) #iteration4
print(next(i)) #iteration5

print("********************************************************************")
x1=[1,2,3,4,5,6,7]
x2=x1#les deux listes pointent sur les memes adresses
x1[2]='new value'
print("x1=",x1)
print("x2=",x2)#le changement se fait dans les deux listes

print("********************************************************************")
x1=[1,2,3,4,5,6,7]
x2=x1.copy()   #les deux listes ne pointent pas sur les memes adresses
x1[2]='new value'
print("x1=",x1)
print("x2=",x2) #le changement ne se fait pas dans les deux listes

#enumerate


my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1): # enumerate pour numeroter les elements dans la liste start=1
    print(c, value)
print("********************************************************************")
for c, value in enumerate(range(50), 10): # enumerate pour numeroter les elements dans la liste start=10
    print(c, value)
print("********************************************************************")    
#associer 2 elements chacun d'une liste :le meme nbre des elements dans les deux liste
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print (a, b)
print("********************************************************************") 


from operator import itemgetter,methodcaller
student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10),]

print(sorted(student_tuples, key=itemgetter(2)))#trier selon col=2
print(sorted(student_tuples, key=itemgetter(1,2)))#trier selon col=1 apres selon col2


print("********************************************************************") 
messages = ['critical!!!', 'hurry!', 'bla bla', 'alabama']
print sorted(messages, key=methodcaller( 'count', 'a')) #trier selon le nombre de 'a' dans chaque element
