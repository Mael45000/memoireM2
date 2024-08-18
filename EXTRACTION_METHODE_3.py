import pandas as pd
import re

corpus_csv= pd.read_csv("corpus_tremolo_full.txt", sep='\t', encoding="Windows-1252", engine='python')

texte=corpus_csv['Texte']
ID=corpus_csv['Text_index']
f_sortie=open("methode_3_sortie.csv","w",encoding="UTF-8")
# Crée un fichier qui stocke les phénomènes.
f_sortie.write("id"+"\t"+"expression"+"\t"+"tweet"+"\n")
c=-1
for line in texte:
    c=c+1
    expr_reg=re.search(r"orthographe|\bon dit(?!\squ)|le (terme|mot)|langage",str(line),re.IGNORECASE)
   # Recherche l'expression régulière dans le tweet. La méthode IGNORECASE permet d'ignorer les cases vides.
    if expr_reg :
        f_sortie.write(ID[c]+"\t"+expr_reg.group()+"\t"+line+"\n")
        # Si l'expression régulière est présente dans le tweet, alors on stocke le tweet. 
        print(expr_reg.group(),line)
         
f_sortie.close()
