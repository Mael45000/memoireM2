# Documentation des pratiques prescriptives chez les non-experts de la langue française sur les réseaux sociaux.

## Description des fichiers
Cette page regroupe tous les documents présents dans la construction de mon mémoire.
On retrouve :

- Le mémoire `MEMOIRE_CHEVAL_2024.pdf`

- Le corpus TREMoLo

  Il contient le fichier sous le format .zip. Une fois décompressé, on peut accéder au fichier sous format .txt `corpus_tremolo_full.txt`.

- Le corpus prétraité `PRETRAITEMENT_CORPUS`
  
  Il contient le corpus TREMoLo traité avec la variable `normalisation`, présente dans le script `EXTRACTION_METHODE_1`.

- le lexique `Lexique383`
  
  Il contient le tableau de l'ensemble des mots en français.
  
- Les scripts :
  * `EXTRACTION_METHODE_1`
  * `EXTRACTION_METHODE_2`
  * `EXTRACTION_METHODE_3`
    
  Chaque fichier contient le script Python des trois méthodes utilisées lors du mémoire.
  
- Les documents de sortie des scripts :
  * `methode_1_sortie`
  * `methode_2_sortie`
  * `methode_3_sortie`
    
   Ces documents sont les fichiers de sortie des scripts Python de chaque méthode.

- Les annotations des documents de sortie :
  * `ANNOTATION_METHODE_1`
  * `ANNOTATION_METHODE_2`
  * `ANNOTATION_METHODE_3`
    
  Ces fichiers .csv sont les documents de sortie annotés des scripts des trois méthodes.

## Prérequis

### Bibliothèques Python et installation de Python 

Le logiciel Python est téléchargeable facilement sur tous les environnements et est gratuit. Vous pouvez l'installer sur le site officiel : https://www.python.org/

Voici les bibliothèques Python nécéssaires au fonctionnement des scripts : 
- `Pandas` le site officiel de Pandas : https://pandas.pydata.org/docs/getting_started/install.html
- `emoji` le lien d'installation de la bibliothèque : https://pypi.org/project/emoji/
- `re` le lien d'installation de re : https://pypi.org/project/regex/
- `spacy` le site de spacy : https://spacy.io/usage

Spacy nécéssite quelques réglages afin d'avoir le pipline français. Tout d'abord, ouvrez un terminal de commande, puis inscrivez dans l'ordre :

`pip install -U pip setuptools wheel`

`pip install -U spacy`

`python -m spacy download fr_core_news_sm`

Le pipline `fr_core_news_sm` est celui qui est utilisé dans les scripts. 

### Ouverture des fichiers

1. Les scripts Python nécéssitent le téléchargement préalable du corpus entier `corpus_tremolo_full.txt` et prétraité `PRETRAITEMENT_CORPUS.csv` pour fonctionner. 

2. Le corpus entier sous le format .txt possède l'encodage `Windows-1252` et possède comme délimiteur de colonne une tabluation : `\t`.

3. Le corpus prétraité possède l'encodage `UTF-8` et le séparateur de colonne `;`.

4. Concernant les fichiers de sortie, ils ont tous un encodage `UTF-8`. `EXTRACTION_METHODE_1` possède une virgule comme délimiteur `,` , `EXTRACTION_METHODE_2` et 
`EXTRACTION_METHODE_3` possèdent le délimiteur `\t`.

5. Les fichiers annotés ont aussi un encodage `UTF-8` , avec comme délimitation `;`.
