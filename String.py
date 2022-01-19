# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 21:01:54 2022

@author: Sana Braham
"""

a = "Hello My name's Sana Braham"

#Slicing
print(a[0],a[-1],a[:6],a[6:],a[::-1],sep="\n")

#Convert String to list
print(list(a))
#Convert String to sorted list
print(sorted(list(a)))

#delimiter a en eliminant les doublons
print(set(a))

#delimiter a selon les espaces
print(a.split())

#delimiter a selon un caractere
print(a.split('m'))

#delimiter String par ligne
b="Hello \n My\n name's\n Sana\n Braham\n"
print(b)
print(b.splitlines())

#diviser(repartition) vs delimiter(split):
c = "Hello_My_name's_Sana_Braham"
print(c.split("_")) #delimiter la chaine en eliminant le caractere
print(c.partition("_")) #diviser la chaine en trois chaines: avant char , char , apres char
print(c.rpartition("_")) #diviser la chaine en trois chaines: avant char , char , apres char en commencant de droite

#find:chercher la premiere occurance
d= "he is a good man"
print(d.find("a")) # en commencant de gauche
print(d.rfind("a")) #en commencant de droite

#index:chercher l'index de premiere occurance
d.index("good")

#in the case that the char doesn't exist find() returns -1 index returns error

#replacer un mot dans une chaine
print(c.replace("Sana","Sondes"))

#compter le nombre des caracteres
print(c.count("n"))

#la premiere lettre de phrase est majuscule
e="it's a good boy "
print(e.capitalize())
#la premiere lettre de chaque mot est majuscule
print(e.title())
#toute les lettres en majuscules
print(e.upper())

#inverser les majuscules en miniscules et vise versa
f="How aRe YOU?"
print(f.swapcase())
#ajouter espace à gauche et à droite  de facon que la logueur finale de f =30
print(f.center(30))
#ajouter espace à gauche cad decaler vers la droite de facon que la logueur finale de f =30
print(f.rjust(30))
#ajouter espace à droite cad decaler vers la gauche de facon que la logueur finale de f =30
print(f.ljust(30))