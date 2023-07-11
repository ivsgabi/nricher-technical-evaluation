#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## algo
## File description:
## for nricher entry test
##

from unidecode import unidecode
import pandas as pd

def is_in_name_article_base(article_name, split_nature):
    i = 0;
    word = article_name.split(" ")[i]
    next_word = article_name.split(" ")[i + 1]
    third_word = article_name.split(" ")[i + 2]

    if isinstance(article_name, str):
        for word in article_name.split(" "):
            if unidecode(word.lower()) == unidecode(split_nature[0].lower()) or (unidecode(word.lower()) == unidecode(split_nature[0].lower()) + "s") or (unidecode(word.lower()) == unidecode(split_nature[0].lower())[:-1]):
                #print("word = {}, nature = {}".format(word, split_nature[0]))
                return 0
        for i in range(len(article_name.split(" ")) - 2):
            if unidecode(word.lower()) == "table" and unidecode(next_word.lower()) == "de" and unidecode(third_word.lower()) == "cuisson" and unidecode(split_nature[0].lower()) == "plaque" and unidecode(split_nature[1].lower()) == "de" and unidecode(split_nature[2].lower()) == "cuisson":
                return 0
        i = 0
        for i in range(len(article_name.split(" ")) - 1):
            if unidecode(word.lower()) == "table" and unidecode(next_word.lower()) == "basse" and unidecode(split_nature[0].lower()) == "table" and unidecode(split_nature[1].lower()) == "basse":
                return 0
            if unidecode(word.lower()) == "table" and unidecode(next_word.lower()) != "basse" and unidecode(split_nature[0].lower()) == "table" and unidecode(split_nature[1].lower()) != "basse":
                return 0
            if unidecode(word.lower()) == "apple" and unidecode(next_word.lower()) == "iphone" and unidecode(split_nature[0].lower()) == "smartphone":
                return (0)
            if unidecode(word.lower()) == "apple" and unidecode(next_word.lower()) == "watch" and unidecode(split_nature[0].lower()) == "acc" and unidecode(split_nature[1].lower()) == "telephonie":
                return (0)
        return 84

def nature_checker(array):

    intrus_list = []

    for row in array:
        init_nature = row[4]
        if isinstance(init_nature, str):
            split_nature = init_nature.split(" ")
            result = is_in_name_article_base(row[1], split_nature)
            if (result != 0) :
                intrus_list.append(f"{row[1]} - {row[4]}")

    for intrus in intrus_list:
        print(intrus)

#given_path = input("Entrez le chemin vers le fichier à analyser : ")

given_path = "data/test.xlsb"
df = pd.read_excel(given_path, engine='pyxlsb')
array = df.values.tolist()
nature_checker(array)

