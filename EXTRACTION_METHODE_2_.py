import pandas as pd
import re
import spacy

nlp=spacy.load(r"fr_core_news_sm")
corpus_csv= pd.read_csv("C:/Users/Utilisateur/Documents/FICHIERS_MEMOIRE/CORPUS/corpus_tremolo_full.txt", sep='\t', encoding="Windows-1252", engine='python')

texte=corpus_csv['Texte']
ID=corpus_csv['Text_index']
f_sortie=open("methode_2_sortie.csv","w",encoding="UTF-8")
f_sortie.write("type"+"\t"+"id"+"\t"+"expression"+"\t"+"tweet"+"\n")
c=-1
for line in texte:
    c=c+1
    doc=nlp(str(line))
    
    expr_reg=re.search(r"comme m[êe]me|[ \n]iel[ \n]|croive|voye[nt]+|malgré qu+",str(line).lower())
    if expr_reg :
        f_sortie.write("ex"+"\t"+ID[c]+"\t"+expr_reg.group()+"\t"+line+"\n")
        print(expr_reg.group(),line)
       
    for token in doc:
        if token.pos_ == "VERB" and (token.text.endswith("er")): 
            token_penu = doc[token.i - 1]
            token_antepenu = doc[token.i - 2]
            if token_penu.lemma_=="avoir" or token_penu.lemma_=="être":
                f_sortie.write("-er"+"\t"+ID[c]+"\t"+token.text+"\t"+line+"\n")
                print(token.text,line)
            elif token_antepenu.lemma_=="avoir" or token_antepenu.lemma_=="être":
                f_sortie.write("-er"+"\t"+ID[c]+"\t"+token.text+"\t"+line+"\n")
                print(token.text,line)
                
        if token.pos_ == "VERB" and (token.text.endswith("é")):
            token_penu = doc[token.i - 1]
            token_antepenu = doc[token.i - 2]  
            if token_penu.lemma_!="être" and token_penu.lemma_!="avoir":
                if token_antepenu.lemma_!="être" and token_antepenu.lemma_!="avoir":
                    f_sortie.write("-é"+"\t"+ID[c]+"\t"+token.text+"\t"+line+"\n")
                    print(token.text,line)

f_sortie.close()

