import pandas as pd
import emoji
import re

lexique_csv = pd.read_csv("C:/Users/Utilisateur/Downloads/Lexique-query-2024-07-18 11-58-45.csv", sep=";")
corpus_csv = pd.read_csv("C:/Users/Utilisateur/Documents/EXTRAIT_CORPUS_TREMOLO.csv", sep=";", encoding="UTF-8", engine='python')

def normalisation(y):
    z=emoji.demojize(y) 
    x=re.sub("#\w+ ?|@XXX:?|RT |:[\w-]+:|url_path|\w+[’']|[^A-Za-zïêëâüçûôéèñàãöùî ]+|\d+\S*","",z)
    w=x.lstrip()
    v=w.lower()
    return v
 
lexique = lexique_csv["Word"]
corpus_csv["Texte_norm"] = corpus_csv["Texte"].apply(normalisation)
corpus_csv["mots"] = corpus_csv["Texte_norm"].str.split()

# Create a DataFrame with all words, their tweet_id, and tweet text
all_words_df = corpus_csv.explode("mots")[["Text_index", "Texte", "mots"]]
all_words_df.columns = ["tweet_id", "tweet", "mot"]
#total_word_count = all_words.shape[0] permet de compter le nombre total de mots

# Filter words not in the lexicon
df_results = all_words_df[~all_words_df["mot"].isin(lexique)]

df_results.to_csv("methode_1_sortie.csv", index=False)

print("Mots absents du lexique :")
print(df_results)

