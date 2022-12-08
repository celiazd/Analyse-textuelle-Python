# -*- coding: utf-8 -*-

import os                     #  permet de communiquer avec le système d'exploitation
os.chdir(r"/Users/celiazaidi/Desktop/Textometrie")         # on fixe le répertoire de travail
chemin = "macron.txt"           # nom du fichier contenant nos textes 

import re            # module "regular expression" 
f=open(chemin,"r")   
voeuxbrut = f.read() 
voeuxchaine = re.sub(r"[.:' ;,?=!\n\xa0]+"," ",voeuxbrut) # remplacement de la ponctuation par des blancs, dont les retours à la ligne (\n)
texte = voeuxchaine[5:].split("****") #  on passe d'un texte unique à une liste de textes identifiés par le séparateur prévu par l'auteur du corpus (****)

année = []    
voeux = []    
for nt in range (len(texte)):    
	titre = texte[nt].split()[0] # split sépare la chaîne textuelle en mots, on prend ici le premier, donc le titre
	année.append(titre)           # on enregistre le nième titre
	long_titre = len(titre) + 1   # on repère où commence le texte à la suite du titre
	voeux.append(texte[nt][long_titre:]) # on extrait le texte sans le titre et on l'enregistre

année
voeux

nt = len(année)   #renvoi au nombre d'élement dans idtex (5 car il ya  5 poèmes)   #len c'est la longueur
d = ' '.join(voeux)  # fusion de l'ensemble des textes
e = d.split()        # conversion des textes en une seule liste de mots qui s'appelle e

motot={}    # motot est un objet de type dictionnaire "mot + effectif"
for mot in e:
	motot[mot] = 0  
for  mot in e:
	motot[mot] += 1  # chaque mot du dictionnaire est associé à un effectif simple




motex = {} #motex permet de dénombrer les mots par poèmes
for mot in motot:
    motex[mot] = [0]*nt   # chaque mot du dictionnaire est associé à une liste d'effectifs plutôt qu'à un effectif simple (en vue de la construction de la table lexicale)

for i in range(nt):   
	for mot in texte[i].split():
		motex[mot][i] += 1   # chaque mot est associé à son effectif dans chaque texte


nb_texte = len(année)  # nbre de textes
s = sorted(motot)          
ch_csv = r"C:\Users\sandr\OneDrive\Bureau\Textométrie\DM\macron.csv"

g = open(ch_csv, "w+")     

#on commence par éditer la ligne d'intitulés de variables
g.write ( "Année ; ")       # nom de colonne pour le csv
for j in range(nb_texte):        # boucle pour la ligne des titres
	g.write(année[j])              # titres des textes
	if(j < nb_texte - 1):
		g.write("; ")              
g.write("\n")                      


#puis on passe aux mots
for i in range(len(s)):       # boucle pour les mots
	if(motot[s[i]] >= 2):        #  on ne garde l'affichage des mots qui sont présents au moins 2 fois
		g.write(s[i])                
		g.write("; ")                
		for j in range(nb_texte):        # boucle fille pour les effectifs du mot dans chaque texte
			g.write(str(motex[s[i]][j])) 
			if(j < nb_texte - 1):
				g.write("; ")      
		g.write("\n")              

print("Export du tableau lexical entier effectué \n")

g.close()           



