# Documentation des pratiques prescriptives chez les non-experts de la langue française sur les réseaux sociaux.

## Description des fichiers
Cette page regroupe tous les documents présents dans la construction de mon mémoire.
On retrouve :
- Le corpus TREMoLo

  Il contient le fichier sous trois formats :
  * un fichier .csv 
  * un fichier .tsv
  * un fichier .txt
 
- Le corpus prétraité
  * PRETRAITEMENT_CORPUS
  
Il contient le corpus TREMoLo traité avec la variable `normalisation`, présent dans le script EXTRACTION_METHODE_1

Ces fichiers contiennent l'intégralité du corpus. Les trois documents s'ouvrent avec comme délimitation une tabulation.

- le lexique
  * Lexique383
  
  Il contient le tableau de l'ensemble des mots en français.
  
- les scripts
  * EXTRACTION_METHODE_1
  * EXTRACTION_METHODE_2
  * EXTRACTION_METHODE_3
    
Chaque fichiers contient le script python des trois méthode utilisées lors du mémoire.
  
- les documents de sortie des scripts
  * methode_1_sortie
  * methode_2_sortie
  * methode_3_sortie
    
 Ces documents sont les fichiers de sortie des scripts Python de chaque méthode.

- les annotations des documents de sortie
  * ANNOTATION_METHODE_2
  * ANNOTATION_METHODE_3
    
Ces fichiers sont les annotations qui annotent les documents de sortie des scripts de la méthode 2 et 3. 

## Prérequis

### Bibliothèques python et Pyhon 

Le logiciel Python est téléchargeable facilement sur tous les environnements et est gratuit. Vous pouvez l'installer sur le site officiel : https://www.python.org/

Voici les bibliothèques Python nécéssaires au fonctionnement des scripts : 
- `Pandas`: voici le site officiel de Pandas : https://pandas.pydata.org/docs/getting_started/install.html
- `emoji`: voici le lien d'installation de la bibliothèque : https://pypi.org/project/emoji/
- `re`: voici le lien d'installation de re : https://pypi.org/project/regex/
- `spacy`: voici le site de spacy : https://spacy.io/usage

Spacy nécéssite quelques réglages afin d'avoir le pipline français. Tout d'abord, ouvrez un terminal de commande, puis inscrivez dans l'ordre :

`pip install -U pip setuptools wheel`
`pip install -U spacy`
`python -m spacy download fr_core_news_sm`

Le pipline `fr_core_news_sm` est celle qui est utilisée dans les scripts. 
