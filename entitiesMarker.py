#!./env/bin/python3

from bs4 import BeautifulSoup
import re
import requests
import fileinput
import os
import datetime
#from selenium import webdriver

entities_toSearch_dictionary = {
"politicos" : [],
"famosos_geral" : [],
"animais" : [],
"religioes" : [],
"etnias" : [],
"cidades" : [],
"paises" : [],
"keywords" : []
}



entities_found_dictionary = {
"politicos" : [],
"famosos_geral" : [],
"animais" : [],
"religioes" : [],
"etnias" : [],
"cidades" : [],
"paises" : [],
"keywords" : []
}


def intialize_dictionary(text):

    for entity in entities_toSearch_dictionary:
        for word in entities_toSearch_dictionary[entity]:
            if word in text:
                entities_found_dictionary[entity].append(word)

                
