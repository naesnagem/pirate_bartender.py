#!/usr/bin/env python3

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}
import sys
import random

taste = {}

def preferences():
    """Asks what their taste preferences are and then sets the values to True or False based on the users answer"""
    for k, v in questions.items():
        print(v)
        taste[k] = input()
        for k, v in taste.items():
            if v == "y":
                taste[k] = True
            elif v == "yes":
                taste[k] = True
            elif v == "n":
                taste[k] = False


def mixrobot(taste):
    """According to the user's tastes the mixrobot creates a drink using one ingredient from each enjoyed taste category"""
    print("\nI believe your ideal drink should have the following:\n")
    for ingredient in ingredients:
        if taste[ingredient] == True:
            print(random.choice(ingredients.get(ingredient)))  


if __name__ == '__main__':
    while input("\nWould you like a drink matey?\n") == "yes" or "y":
        print("\nLet me make you the perfect cocktail.\n\nI have just a few questions in order to find you your perfect drink...\n")
        preferences()
        mixrobot(taste)