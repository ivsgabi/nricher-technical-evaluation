#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## algo
## File description:
## for nricher entry test
##

from unidecode import unidecode
import pandas as pd

def check_categorisation(article_name, split_nature):
    i = 0;
    if isinstance(article_name, str):
        for word in article_name.split(" "):
            if unidecode(word.lower()) == unidecode(split_nature[0].lower()) or (unidecode(word.lower()) == unidecode(split_nature[0].lower()) + "s") or (unidecode(word.lower()) == unidecode(split_nature[0].lower())[:-1]):
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
            if unidecode(word.lower()) == "etagere" or unidecode(word.lower()) + "s" and unidecode(split_nature[0].lower()) == "bibliotheque":
                return 0
            if unidecode(word.lower()) == "tagere" or unidecode(word.lower()) + "s" and unidecode(split_nature[0].lower()) == "bibliotheque":
                return 0
            if unidecode(word.lower()) == "console" and unidecode(split_nature[0].lower()) == "bureau":
                return 0
            if unidecode(word.lower()) == "couette" and unidecode(split_nature[0].lower()) == "housse":
                return 0
            if unidecode(word.lower()) == "banc" and unidecode(split_nature[0].lower()) == "chaise":
                return 0
            if unidecode(word.lower()) == "torchon" or unidecode(word.lower()) + "s" and unidecode(split_nature[0].lower()) == "linge":
                return 0
            if unidecode(word.lower()) == "nespresso" and unidecode(split_nature[0].lower()) == "expresso":
                return 0
            if unidecode(word.lower()) == "chaise" and unidecode(split_nature[0].lower()) == "tabouret":
                return 0
            if unidecode(word.lower()) == "sommier" and "sommier" in unidecode(str(split_nature).lower()):
                return 0
            if unidecode(word.lower()) == "couette" and "parure de lit" in unidecode(str(split_nature).lower()):
                return 0
            if unidecode(word.lower()) == "led" and "lumineux" in unidecode(str(split_nature).lower()) or "lumineuse" in unidecode(str(split_nature).lower()):
                return 0
            if unidecode(word.lower()) == "tnt" and "tnt" in unidecode(str(split_nature).lower()):
                return 0
            if unidecode(word.lower()) == "vitrage" and "voilage" in unidecode(str(split_nature).lower()):
                return 0
            if unidecode(word.lower()) == "lattes" and "lattes" in unidecode(str(split_nature).lower()):
                return 0
            if unidecode(word.lower()) == "aspirateur" and "aspirateur" in unidecode(str(split_nature).lower()):
                return 0
            if unidecode(word.lower()) == "souris" and "souris" in unidecode(str(split_nature).lower()):
                return 0
            if unidecode(word.lower()) == "moto" and unidecode(split_nature[0].lower()) == "vehicule":
                return 0
            if unidecode(word.lower()) == "banc" and "pouf" in unidecode(str(split_nature).lower()):
                return 0
            if unidecode(word.lower()) == "four" and "four" in unidecode(str(split_nature).lower()):
                return 0
        for i in range(len(article_name.split(" ")) - 1):
            word = article_name.split(" ")[i]
            next_word = article_name.split(" ")[i + 1]
            if unidecode(word.lower()) == "coque" and unidecode(split_nature[0].lower()) == "acc" and  unidecode(split_nature[1].lower()) == "telephonie":
                return 0
            if unidecode(word.lower()) == "armoire" and unidecode(split_nature[0].lower()) == "structure" and unidecode(split_nature[1].lower()) == "armoire":
                return 0
            if unidecode(word.lower()) == "musculation" and unidecode(split_nature[0].lower()) == "appareil" and unidecode(split_nature[1].lower()) == "musculation":
                return 0
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
            if unidecode(word.lower()) == "clic" and unidecode(next_word.lower()) == "clac" and unidecode(split_nature[0].lower()) == "canape":
                return 0
            if unidecode(word.lower()) == "samsung" and unidecode(next_word.lower()) == "galaxy" and unidecode(split_nature[0].lower()) == "smartphone":
                return 0
        for i in range(len(article_name.split(" ")) - 2):
            word = article_name.split(" ")[i]
            next_word = article_name.split(" ")[i + 1]
            third_word = article_name.split(" ")[i + 2]
            if unidecode(word.lower()) == "table" and unidecode(next_word.lower()) == "de" and unidecode(third_word.lower()) == "cuisson" and unidecode(split_nature[0].lower()) == "plaque" and unidecode(split_nature[1].lower()) == "de" and unidecode(split_nature[2].lower()) == "cuisson":
                return 0
            if unidecode(word.lower()) == "salon" and unidecode(next_word.lower()) == "de" and unidecode(third_word.lower()) == "jardin" and unidecode(split_nature[0].lower()) == "ens" and unidecode(split_nature[1].lower()) == "table" and unidecode(split_nature[2].lower()) == "chaises":
                return 0
            if unidecode(word.lower()) == "parure" and unidecode(split_nature[0].lower()) == "housse" and unidecode(split_nature[1].lower()) == "de" and unidecode(split_nature[2].lower()) == "couette":
                return 0
            if unidecode(word.lower()) == "salle" and unidecode(next_word.lower()) == "de" and unidecode(third_word.lower()) == "bain" and "sdb" in unidecode(str(split_nature).lower()):
                return 0
        return 84

def nature_checker(array):
    intrus_list = []
    corrected_lines = []
    corrections_dict = {}

    for row in array:
        init_nature = row[4]
        if isinstance(init_nature, str) and isinstance(row[1], str):
            split_nature = init_nature.split(" ")
            result = check_categorisation(row[1], split_nature)
            if result != 0 and row not in corrected_lines:
                intrus_list.append(f"{row[1]} - {row[4]}")
                corrected_lines.append(row)
                first_three_words = ' '.join(row[1].split(" ")[:3])
                if first_three_words not in corrections_dict:
                    corrections_dict[first_three_words] = init_nature

    for intrus in intrus_list:
        corrected_value = input(f"Corrigez la nature si elle est incorrecte -> {intrus}: ")
        if corrected_value != "":
            first_three_words = ' '.join(intrus.split()[0:3])
            corrections_dict[first_three_words] = corrected_value

    for row in array:
        init_nature = row[4]
        if isinstance(init_nature, str) and isinstance(row[1], str): 
            split_nature = init_nature.split(" ")
            result = check_categorisation(row[1], split_nature)
            if result == 84:
                first_three_words = ' '.join(row[1].split(" ")[:3])
                if first_three_words in corrections_dict:
                    row[4] = corrections_dict[first_three_words]

    for row in array:
        print(row)
    df_corrected = pd.DataFrame(array, columns=df.columns)
    df_corrected.to_excel("corrected_nature_sales.xlsx", index=False)

#given_path = input("Entrez le nom du fichier à analyser: ")
given_path = "data/20210614 Ecommerce sales.xlsb"
df = pd.read_excel(given_path, engine='pyxlsb')
array = df.values.tolist()
nature_checker(array)

