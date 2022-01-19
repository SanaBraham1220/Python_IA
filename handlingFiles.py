# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 09:29:10 2022

@author: Sana Braham
"""

#ouvrir avec l'acces ecriture (w:write) le fichier text '1.txt' s'il existe en ecrasant l'ancien contenu 
#creer  le fichier text '1.txt' s'il n'existe pas
f= open('D:\\1.txt','w')
#écrire dans le fichier
f.write('write this line in the file')
#fermer le fichier
f.close()

#ouvrir le fichier pour update (a:append)
f= open('D:\\1.txt','a')
f.write('\n second line')
f.write('\n third line')
f.close


#ouvrir le fichier pour lecture (r:read)
f= open('D:\\1.txt','r')
#lecture des lignes
for a in f:
    print(a)

f.close()

#on peut travailler aussi sur des fichiers excel .csv ou .xls
outfile = open('D:\\5.csv', 'w')
outfile.write('a')
outfile.close()
outfile = open('D:\\5.xls', 'w')
outfile.write('a\nb\nc\nd\n')
outfile.close()

outfile = open('D:\\5.xls', 'r')
for g in outfile:
    print(g)
    
#afficher le repertoire courant:
import os
a=os.getcwd()
print(a)

#creer un nouveau dossier
#exist_ok = True en ecrasant l'ancien existant
os.makedirs('D:\\1\\00' , exist_ok = True)
#os.makedirs('D:\\1\\01' , exist_ok = False)

#verfier l'existance d'un fichier ou dossier
print(os.path.exists('D:\\1\\00'))
print(os.path.exists('D:\\1\\0.txt'))

#shutil library pour copier et deplacer les fichiers
import shutil as sh
sh.copyfile( 'D:\\1\\00\\1.txt', 'D:\\1\\00\\2.txt')#copier dans un fichier existant
sh.copyfile( 'D:\\1\\00\\1.txt', 'D:\\1\\00\\3.txt')#copier en creeant un nouveau fichier
#sh.copytree('D:\\1\\00' , 'D:\\1\\01\\00copy') 
sh.move('D:\\1\\00\\1.txt' , 'D:\\1\\01') 






    
