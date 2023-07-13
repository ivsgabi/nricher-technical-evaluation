#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## algo
## File description:
## for nricher entry test
##

from unidecode import unidecode
import pandas as pd

def check_categoriasation(article_name, split_nature):
    i = 0;
    if isinstance(article_name, str):
        for word in article_name.split(" "):
            if unidecode(word.lower()) == unidecode(split_nature[0].lower()) or (unidecode(word.lower()) == unidecode(split_nature[0].lower()) + "s") or (unidecode(word.lower()) == unidecode(split_nature[0].lower())[:-1]):
                #print("word = {}, nature = {}".format(word, split_nature[0]))
                return 0
            if unidecode(word.lower()) == "plancha" and unidecode(split_nature[0].lower()) == "barbecue":
                return 0
            if unidecode(word.lower()) == "ipad" and unidecode(split_nature[0].lower()) == "tablette":
                return 0
            if unidecode(word.lower()) == "televiseur" and unidecode(split_nature[0].lower()) == "tv":
                return 0
            if unidecode(word.lower()) == "fauteuil" and unidecode(split_nature[0].lower()) == "chaise":
                return 0
            if unidecode(word.lower()) == "sommier" and unidecode(split_nature[0].lower()) == "lit":
                return 0
            if unidecode(word.lower()) == "commode" and unidecode(split_nature[0].lower()) == "mini" and unidecode(split_nature[1].lower()) == "commode":
                return 0
            if unidecode(word.lower()) == "trotinette" and unidecode(split_nature[0].lower()) == "gyropode":
                return 0
            if unidecode(word.lower()) == "mug" and unidecode(split_nature[0].lower()) == "vaisselle":
                return 0
            if unidecode(word.lower()) == "tasse" and unidecode(split_nature[0].lower()) == "vaisselle":
                return 0
            if unidecode(word.lower()) == "assiette" and unidecode(split_nature[0].lower()) == "vaisselle":
                return 0
            if unidecode(word.lower()) == "theiere" and unidecode(split_nature[0].lower()) == "vaisselle":
                return 0
            if unidecode(word.lower()) == "bol" and unidecode(split_nature[0].lower()) == "vaisselle":
                return 0
            if unidecode(word.lower()) == "garantie" and unidecode(split_nature[0].lower()) == "garant.":
                return 0
            if unidecode(word.lower()) == "penderie" and unidecode(split_nature[0].lower()) == "armoire":
                return 0
            if unidecode(word.lower()) == "meuble" and unidecode(split_nature[0].lower()) == "rangement":
                return 0
            if unidecode(word.lower()) == "cable" and unidecode(split_nature[0].lower()) == "connectique":
                return 0
            if unidecode(word.lower()) == "ensemble" and unidecode(split_nature[0].lower()) == "ens":
                return 0
            if unidecode(word.lower()) == "+" and unidecode(split_nature[0].lower()) == "ensemble":
                return 0
            if unidecode(word.lower()) == "etagere" and unidecode(split_nature[0].lower()) == "bibliotheque":
                return 0
            if unidecode(word.lower()) == "tagere" and unidecode(split_nature[0].lower()) == "bibliotheque":
                return 0
            if unidecode(word.lower()) == "console" and unidecode(split_nature[0].lower()) == "bureau":
                return 0
        for i in range(len(article_name.split(" ")) - 1):
            word = article_name.split(" ")[i]
            next_word = article_name.split(" ")[i + 1]
            if unidecode(word.lower()) == "table" and unidecode(next_word.lower()) == "basse" and unidecode(split_nature[0].lower()) == "table" and unidecode(split_nature[1].lower()) == "basse":
                return 0
            if unidecode(word.lower()) == "table" and unidecode(next_word.lower()) != "basse" and unidecode(split_nature[0].lower()) == "table" and unidecode(split_nature[1].lower()) != "basse":
                return 0
            if unidecode(word.lower()) == "apple" and unidecode(next_word.lower()) == "iphone" and unidecode(split_nature[0].lower()) == "smartphone":
                return 0
            if unidecode(word.lower()) == "apple" and unidecode(next_word.lower()) == "watch" and unidecode(split_nature[0].lower()) == "acc" and unidecode(split_nature[1].lower()) == "telephonie":
                return 0
            if unidecode(word.lower()) == "apple" and unidecode(next_word.lower()) == "macbook" and unidecode(split_nature[0].lower()) == "pc":
                return 0
        for i in range(len(article_name.split(" ")) - 2):
            word = article_name.split(" ")[i]
            next_word = article_name.split(" ")[i + 1]
            third_word = article_name.split(" ")[i + 2]
            if unidecode(word.lower()) == "table" and unidecode(next_word.lower()) == "de" and unidecode(third_word.lower()) == "cuisson" and unidecode(split_nature[0].lower()) == "plaque" and unidecode(split_nature[1].lower()) == "de" and unidecode(split_nature[2].lower()) == "cuisson":
                return 0
            if unidecode(word.lower()) == "salon" and unidecode(next_word.lower()) == "de" and unidecode(third_word.lower()) == "jardin" and unidecode(split_nature[0].lower()) == "ens" and unidecode(split_nature[1].lower()) == "table" and unidecode(split_nature[2].lower()) == "chaises":
                return 0
        return 84

def nature_checker(array):
    intrus_list = []

    for row in array:
        init_nature = row[4]
        if isinstance(init_nature, str):
            split_nature = init_nature.split(" ")
            result = check_categoriasation(row[1], split_nature)
            if result != 0:
                intrus_list.append(f"{row[1]} - {row[4]}")
                #intrus_list.append(row)

    #for intrus in intrus_list:
    #    print(intrus)
    for intrus in intrus_list:
        corrected_value = input(f"Corrigez la nature si elle est incorrecte -> {intrus}: ")
        if corrected_value != "":
            index = array.index(intrus)
            #Mettre à jour la colonne row[4] avec la valeur corrigée
            array[index][4] = ' '.join(list(corrected_value))    
    
    #corrected_array = array
    for row in array:
        print (row)

    #df_corrected = pd.DataFrame(corrected_array, columns=df.columns)
    #df_corrected.to_excel("nouveau_fichier.xlsx", index=False)

#given_path = input("Entrez le chemin vers le fichier à analyser : ")

given_path = "data/test.xlsb"
df = pd.read_excel(given_path, engine='pyxlsb')
array = df.values.tolist()
nature_checker(array)

