import pandas as pd
import emoji
import re

lexique_csv = pd.read_csv("Lexique.csv", sep=";")
corpus_csv = pd.read_csv("EXTRAIT_CORPUS_TREMOLO.csv", sep=";", encoding="UTF-8", engine='python')

def normalisation(y):
    z=emoji.demojize(y) 
    x=re.sub("#\w+ ?|@XXX:?|RT |:[\w-]+:|url_path|\w+[’']|[^A-Za-zïêëâüçûôéèñàãöùî ]+|\d+\S*","",z)
    w=x.lstrip()
    v=w.lower()
    return v
    # Crée une variable avec une entrée contenant une chaîne de caractère et retourne une chaîne de caractères normalisée.
 
lexique = lexique_csv["Word"]
corpus_csv["Texte_norm"] = corpus_csv["Texte"].apply(normalisation)
# Crée une colonne qui affiche les tweets normalisés grâce à la variable normalisation crée ultérieurement.

corpus_csv["mots"] = corpus_csv["Texte_norm"].str.split()
# Crée une colonne de mots en séparant les phrases dans la colonne des tweets

all_words = corpus_csv.explode("mots")[["Text_index", "Texte", "mots"]]
# Sépare les listes de mots crée avec la méthode .split afin d'avoir un mot par ligne dans la colonne all_words.

all_words.columns = ["tweet_id", "tweet", "mot"]
# Donne un nom aux colonnes
# total_word_count = all_words.shape[0] ----> permet de compter le nombre total de mots dans le corpus.

resultats = all_words[~all_words["mot"].isin(lexique)]
# Filtre les mots qui ne sont pas dans le lexique.

resultats.to_csv("methode_TEST_sortie.csv", index=False)
# Crée un fichier .csv qui stocke les colonnes dans le corpus.

print("Mots absents du lexique :")
print(resultats)
# Affiche les mots asbsents du lexique.
