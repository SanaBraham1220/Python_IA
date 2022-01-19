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
print(e.center(30))
#ajouter espace à gauche cad decaler vers la droite de facon que la logueur finale de f =30
print(e.rjust(30))
#ajouter espace à droite cad decaler vers la gauche de facon que la logueur finale de f =30
print(e.ljust(30))
#ajouter un charactere quelconque à gauche cad decaler vers la droite de facon que la logueur finale de f =30
print(e.rjust(30,'*'))

#ajouter des zeros a gauche de nombre jusqu'a avoir une longueur finale=10
g='2356'
print(g.zfill(10))

#tester si la chaine contient que des lettres
print(g.isalpha())

#supprimer les espaces dans une chaine de caracteres (c'est le contraire de la fonction just)
h=' Hello Python '
print(h.strip(' '))#supprimer l'espace de deux cotés
print(h.rstrip(' '))#supprimer l'espace de droite
print(h.lstrip(' '))#supprimer l'espace de gauche
#strip avec un autre charactere
k='*******Hello Python**********'
print(k.strip('*'))#supprimer l'espace de deux cotés
print(k.rstrip('*'))#supprimer l'espace de droite
print(k.lstrip('*'))#supprimer l'espace de gauche

# '\n' '\t'
i='sweet \n home alabama' #retour a la ligne
print(i)
j= r'C:\some\name' # ignorer \n
print(j)
k="sweet \t home alabama" #tabulation
print(k)
l=""" sweet home
    'my home'
           alabama """ #ecrire sur plusieurs lignes
print(l)

#impimer dans la meme ligne sans retour à la ligne ou espace
m , n = 'aaaa' , 'bbbbb'
print(m,end='')
print(n)

# le caractere'%'
aa = 'alabama'
aaa = "sweet home %s" %aa #s pour String
print(aaa)
bb = 136
bbb = "sweet home %d" %bb #d pour Integer
print(bbb)
print("sweet %s %d" %(aa,bb))

#afficher le nombre 7 avec 5 espaces avant le nombre.
print('numbers %5d' %7) #7 est la 5ieme position
#afficher le nombre 7 avec 5 zeros avant le nombre.
print('numbers %05d' %7) #7 est la 5ieme position
print("%s has %03d qoute types." %("Python", 2)) #2 est la 3ieme position

#astuces d'affichage (doesn't)
print(" it doesn't ") #utuliser "" pour ignorer '
print(' it doesn\'t ') #utuliser \ pour ignorer '
#astuces d'affichage ("yes")
print(' he said "YES" ') #utuliser '' pour ignorer ""
print(" he said \"YES\" ") #utuliser \ pour ignorer 
print('"It doesn\'t," she said.')

#tester si la chaine contient que des nombres
A='55881'
AA='5ml4444'
print('is digit A, AA', A.isdigit(),AA.isdigit())
#test sur la chaine des caracteres
B='AAABNB JNN'
print('is upper =',B.isupper())
print('is lower =',B.islower())
C= 'Ahhhh Kkkk LMn'
D= 'Ahhhh Kkkk Lmn'
print('is title =',C.istitle(),D.istitle())
E= "Sana Braham"
print("starts with:",E.startswith("San"))
print("ends with:",E.endswith("ham"))

#join inserer un caractere entre des membres d'une liste:
print('*******'.join(('st1','st2','st3','st4')))
print('\n'.join(('st1','st2','st3','st4')))

#.format()
pi=3.14562485452
print("The value of pi is {}".format(pi))
print('{0} and {1}'.format('red', 'blue'))
print('{1} and {0}'.format('red', 'blue'))
print("First: {first}. Last: {last}.".format(last='Z', first='A'))
print("pi = {0:.3f}".format(pi))
print('{:s} {:d} years old'.format('Im',20))
print('|' + '{:^30}'.format('Hello') + '|') #justifier le texte 30 au milieu entre les deux symboles '|'
print('|' + '{:^60}'.format('Hello') + '|') #justifier le texte 50 au milieu entre les deux symboles '|'
print('{0:10} ==> {1:10d}'.format('name', 56322))

#chercher une chaine dans un text selon deseign pattern dans la library re en utilisant compile()
import re
#je veux chercher une chaine contient lettres + '@' + lettres +'.' + 3  lettres entre a et z
email = re.compile('\w+@\w+\.[a-z]{3}')
text = "To email Guido, try guido@python.org , guido@google.fr or guido@google.com "
print(email.findall(text)) 

text = "To email Guido, try guido@python.org or guido@google.com "
email3=re.compile(r'([\w.]+)@(\w+)\.([a-z]{3})')
print(email3.findall(text))

#creation d'un dictionnaire
text = "To email Guido, try guido@python.org or guido@google.com "
email4=re.compile(r'(?P<user>[\w.]+)@(?P<domain>\w+).(?P<suffix>[a-z]{3})')
match=email4.match('guido@python.org')
print(match.groupdict())
