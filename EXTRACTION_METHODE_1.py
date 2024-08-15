import pandas as pd
import emoji
import re

lexique_csv = pd.read_csv("Lexique-query-2024-07-18 11-58-45.csv", sep=";")
corpus_csv = pd.read_csv("EXTRAIT_CORPUS_TREMOLO.csv", sep=";", encoding="UTF-8", engine='python')

# Crée une variable avec une entrée contenant une châine de caractère, qui retourne une chaîne de caractères normalisée
def normalisation(y):
    z=emoji.demojize(y) 
    x=re.sub("#\w+ ?|@XXX:?|RT |:[\w-]+:|url_path|\w+[’']|[^A-Za-zïêëâüçûôéèñàãöùî ]+|\d+\S*","",z)
    w=x.lstrip()
    v=w.lower()
    return v
 
lexique = lexique_csv["Word"]
corpus_csv["Texte_norm"] = corpus_csv["Texte"].apply(normalisation)
#Crée une colonne qui affiche les tweets normalisés grâce à la variable normalisation crée ultérieurement
corpus_csv["mots"] = corpus_csv["Texte_norm"].str.split()


all_words = corpus_csv.explode("mots")[["Text_index", "Texte", "mots"]]
all_words.columns = ["tweet_id", "tweet", "mot"]
# total_word_count = all_words.shape[0] ----> permet de compter le nombre total de mots dans le corpus

# Filtre les mots qui ne sont pas dans le lexique
df_results = all_words_df[~all_words_df["mot"].isin(lexique)]

# Crée un fichier csv qui stocke les mots pas présents dans le corpus
df_results.to_csv("methode_1_sortie.csv", index=False)

print("Mots absents du lexique :")
print(df_results)
# Affiche les mots asbsents du lexique 

