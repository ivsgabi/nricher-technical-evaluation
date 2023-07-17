#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## second task
## File description:
## for nricher entry test
##

import re
from unidecode import unidecode
import pandas as pd

def has_numbers(str):
    return any(char.isdigit() for char in str)

def detect_colors(string):
    color_pattern = r'\b(black|noir|noire|noires|white|blanc|blanche|blanches|rouge|rouges|bleu|blue|bleus|vert|verts|verte|vertes|jaune|jaunes|orange|violet|violette|rose|roses|marron|gris|anthracite|taupe|beige)\b'
    colors = re.findall(color_pattern, string, flags=re.IGNORECASE)
    return colors

def extract_infos(array, input_str):
    article_found = False
    encountered_values = set()
    printed_coloris = set()
    coloris_status = False

    for row in array:
        value = str(row[1])
        value_str = value.split(" ")
        if input_str in value:
            article_found = True
            article_name = row[1]

            if any(color in article_name for color in detect_colors(article_name)):
                for color in detect_colors(article_name):
                    if color not in printed_coloris:
                        printed_coloris.add(color)
                        coloris_status = True
                        print("Coloris:", color)

            i = 0
            while i < len(value_str):
                article_name = row[1]

                dimensions_match = re.search(r'\b(\d+[a-zA-Z]?(?:\s*[x*]\s*\d+[a-zA-Z]?)+)\b', value)
                if dimensions_match:
                    dimensions_str = dimensions_match.group(1)
                    if article_name not in encountered_values:
                        encountered_values.add(article_name)
                        print("Nom complet article:", article_name)
                        print("Dimension(s):", dimensions_str)
                        return article_found

                elif (len(value_str) > 1 and value_str[i] in ["mm", "cm", "m"]) and value_str[i - 2] != "x" and value_str[i - 1].isdigit():
                    dimensions = value_str[i - 1]
                    if article_name not in encountered_values:
                        encountered_values.add(article_name)
                        print("Nom complet article:", article_name)
                        print("Dimension(s):", dimensions + ' ' + value_str[i])
                        return article_found                    
                elif len(value_str[i]) != 1 and ("x" in value_str[i] or "*" in value_str[i]) and has_numbers(value_str[i]):
                    if article_name not in encountered_values:
                        encountered_values.add(article_name)
                        print("Nom complet article:", article_name)
                        if i + 1 < len(value_str) and value_str[i + 1] in ["mm", "cm", "m"]:
                            print("Dimension(s):", value_str[i] + ' ' + value_str[i + 1])
                        else:
                            print("Dimension(s):", value_str[i])
                    return article_found           
                elif (value_str[i] == "x" or value_str[i] == "*") and value_str[i + 2] == "x" and value_str[i - 1].isdigit() and value_str[i + 1].isdigit() and (value_str[i + 3].isdigit() or value_str[i + 3] in ["mm", "cm", "m"]):
                    if article_name not in encountered_values:
                        encountered_values.add(article_name)
                        print("Nom complet article:", article_name)
                        if value_str[i + 4] in ["mm", "cm", "m"]:
                            print("Dimension(s):", value_str[i - 1] + ' ' + value_str[i] + ' ' + value_str[i + 1] + ' ' + value_str[i + 2] + ' ' + value_str[i + 3] + ' ' + value_str[i + 4])
                        else:
                            print("Dimension(s):", value_str[i - 1] + ' ' + value_str[i] + ' ' + value_str[i + 1] + ' ' + value_str[i + 2] + ' ' + value_str[i + 3])
                    return article_found
                elif (value_str[i] == "x" or value_str[i] == "*") and value_str[i - 1].isdigit() and value_str[i + 1].isdigit():
                    if article_name not in encountered_values:
                        encountered_values.add(article_name)
                        print("Nom complet article:", article_name)
                        if value_str[i + 2] in ["mm", "cm", "m"]:
                            print("Dimension(s):", value_str[i - 1] + ' ' + value_str[i] + ' ' + value_str[i + 1] + ' ' + value_str[i + 2])
                        else:
                            print("Dimension(s):", value_str[i - 1] + ' ' + value_str[i] + ' ' + value_str[i + 1])
                    return article_found
                elif (value_str[i] == "x" or value_str[i] == "*") and value_str[i - 1].isdigit() and value_str[i + 1].isdigit():
                    if article_name not in encountered_values:
                        encountered_values.add(article_name)
                        print("Nom complet article:", article_name)
                        if value_str[i + 2] in ["mm", "cm", "m"]:
                            print("Dimension(s):", value_str[i - 1] + ' ' + value_str[i] + ' ' + value_str[i + 1] + ' ' + value_str[i + 2])
                        else:
                            print("Dimension(s):", value_str[i - 1] + ' ' + value_str[i] + ' ' + value_str[i + 1])
                    return article_found
                elif (value_str[i] == "x" or value_str[i] == "*") and value_str[i - 1].isdigit() and value_str[i + 1].isdigit():
                    if article_name not in encountered_values:
                        encountered_values.add(article_name)
                        print("Nom complet article:", article_name)
                        if value_str[i + 2] in ["mm", "cm", "m"]:
                            print("Dimension(s):", value_str[i - 1] + ' ' + value_str[i] + ' ' + value_str[i + 1] + ' ' + value_str[i + 2])
                        else:
                            print("Dimension(s):", value_str[i - 1] + ' ' + value_str[i] + ' ' + value_str[i + 1])
                    return article_found
                elif "mm" in value_str[i] or "cm" in value_str[i] or "m" in value_str[i] and has_numbers(value_str[i]):
                    if article_name not in encountered_values:
                        encountered_values.add(article_name)
                        print("Nom complet article:", article_name)
                        print("Dimension(s):", value_str[i])
                    return article_found
                    
                i = i + 1
    print("Dimension(s): No dimension(s) found.")
    if coloris_status != True:
            print("Coloris: No coloris found.")
    if not article_found:
        return article_found
    return article_found

def main():
    given_path = "data/test.xlsb"
    df = pd.read_excel(given_path, engine='pyxlsb')
    array = df.values.tolist()
    while (1):
        input_str = input("Entrez le début du nom de l'article souhaité pour obtenir ses dimensions et/ou son/ses coloris: ")
        if extract_infos(array, input_str) == 0:
            print("Article not found.")
            return 84
    print("Done!")
    return (0)

if __name__ == '__main__':
    main()
