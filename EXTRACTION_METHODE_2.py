import pandas as pd
import re
import spacy

nlp=spacy.load(r"fr_core_news_sm")
corpus_csv= pd.read_csv("corpus_tremolo_full.txt", sep='\t', encoding="Windows-1252", engine='python')

texte=corpus_csv['Texte']
ID=corpus_csv['Text_index']
f_sortie=open("methode_2_sortie.csv","w",encoding="UTF-8")
#Crée un fichier qui stockera les phénomènes 
f_sortie.write("type"+"\t"+"id"+"\t"+"expression"+"\t"+"tweet"+"\n")
c=-1
for line in texte:
    c=c+1
    doc=nlp(str(line))
    
    expr_reg=re.search(r"comme m[êe]me|[ \n]iel[ \n]|croive|voye[nt]+|malgré qu+",str(line).lower())
    # Recherche l'expression régulière dans le tweet en convertissant le tweet en minuscule
    if expr_reg :
        f_sortie.write("ex"+"\t"+ID[c]+"\t"+expr_reg.group()+"\t"+line+"\n")
        # Si l'expression régulière est dans le tweet, alors on stocke le tweet
        #print(expr_reg.group(),line)
    for token in doc:
        if token.pos_ == "VERB" and (token.text.endswith("er")): 
            # Recherche les mots qui sont étiquetés comme des verbes qui terminent par -er
            token_penu = doc[token.i - 1]
            token_antepenu = doc[token.i - 2]
            if token_penu.lemma_=="avoir" or token_penu.lemma_=="être":
                f_sortie.write("-er"+"\t"+ID[c]+"\t"+token.text+"\t"+line+"\n")
                # Si le mot avant le verbe est un auxiliaire, on le stocke
                #print(token.text,line)
            elif token_antepenu.lemma_=="avoir" or token_antepenu.lemma_=="être":
                f_sortie.write("-er"+"\t"+ID[c]+"\t"+token.text+"\t"+line+"\n")
                # Si le mot en antépenultième position du verbe est un auxiliaire, on le stocke
                #print(token.text,line)
                
        if token.pos_ == "VERB" and (token.text.endswith("é")):
            # Recherche les mots qui sont étiquetés comme des verbes qui terminent par -é
            token_penu = doc[token.i - 1]
            token_antepenu = doc[token.i - 2]  
            if token_penu.lemma_!="être" and token_penu.lemma_!="avoir":
                if token_antepenu.lemma_!="être" and token_antepenu.lemma_!="avoir":
                    f_sortie.write("-é"+"\t"+ID[c]+"\t"+token.text+"\t"+line+"\n")
                    # Si le mot placé avant et en antépénultième position n'est pas un auxiliaire, alors on le stocke
                    #print(token.text,line)

f_sortie.close()

