#!./env/bin/python3

from bs4 import BeautifulSoup
import re
import requests
import fileinput
import os
import publico_scraper
from itertools import chain
#from selenium import webdriver

"""
ciganos = ["cigan"]
refugiados = ["refugiad", "cativeiro"]
mulheres = ["primeira mulher", "femininismo", "violência doméstica", "mulheres", "direitos das mulheres", "grupo de mulheres", "movimento de mulheres", "igualdade de direitos", "igualdade de salário", "igualdade de salarial", "menina"]
animais = ["tourada", "touro", " animal", " animais", " canil", " cão ", " cães", " zoo ", " zoológico", " vias de extinção", " espécie protegida", "tartarugas", "andorinhas", " circo ", "leões", "lince", "pesca", "elefantes", "abandono de animais", "matadouro", "girafa", "galgos"]
homosexualidade = ["lgbt", " gay", "homossexua", "homosexua" "lésbica", "sexualidade", "homofobia", "homofóbic", "transexual", "drag queen", "bicha", "pessoas do mesmo sexo", "sair do armario", "pride", "ILGA", "orientacao sexual"]
africanos = ["cor negra", "african", "racismo", "racista", "cor da pele", "comunidade negra", "afro"]
asiaticos = ["asiátic", "chines", "chinês", "xenofob"]
imigrantes = ["imigrante", "imigracao", "imigrar"]



def minoritiesFilter ():

    rootdir = '/Users/leandro/Desktop/paulo'

    for subdir, dirs, files in os.walk(rootdir):
        files = [f for f in files if not f[0] == '.']
        for file in files:

            #soup = BeautifulSoup(open(os.path.join(subdir, file)), "html.parser")
            '''
            [x.extract() for x in soup.find_all('script')]
            [x.extract() for x in soup.find_all('style')]
            [x.extract() for x in soup.find_all('meta')]
            [x.extract() for x in soup.find_all('noscript')]
            '''



            #soup = BeautifulSoup(open(os.path.join(subdir, file)), "html.parser")
            #print(os.path.join(subdir, file))
            HtmlFile = open(os.path.join(subdir, file), 'r', encoding='utf-8')
            html_text = HtmlFile.read()


            if isEligible(html_text) == False:
                os.remove(os.path.join(subdir, file))
                print("removed " + os.path.join(subdir, file))


def isEligible(text):

    #podia ter criado uma funcao para nao ter código repetido mas eu queria imprimir o nome da minoria e nao sei sé é possivel imprimir o nome do array xD

    if re.search(r'|'.join(ciganos), text, re.IGNORECASE):
        #if re.search(word, text, re.IGNORECASE):
        print("encontrei ciganos")
        #if word in text:
        return True

    if re.search(r'|'.join(mulheres), text, re.IGNORECASE):
        print("encontrei mulheres")
        return True

    if re.search(r'|'.join(refugiados), text, re.IGNORECASE):
        print("encontrei refugiados")
        return True

    if re.search(r'|'.join(animais), text, re.IGNORECASE):
        print("encontrei animais")
        return True

    if re.search(r'|'.join(africanos), text, re.IGNORECASE):
        print("encontrei africanos")
        return True

    if re.search(r'|'.join(asiaticos), text, re.IGNORECASE):
        print("encontrei asiaticos")
        return True

    if re.search(r'|'.join(imigrantes), text, re.IGNORECASE):
        print("encontrei imigrantes")
        return True

    if re.search(r'|'.join(homosexualidade), text, re.IGNORECASE):
        print("encontrei bichas")
        return True

    return False

"""

def scrap_news():

    rootdir = 'C:\\Repos\\MEI\\ARQUIVO-PT-FINAL\\raw'
    rootdir2 = 'C:\\Repos\\MEI\\crawler-2017-2\\output\\html\\publico\\misc'
    rootdir3 = 'C:\\Repos\\MEI\\crawler2018\\output\\html\\publico\\misc'
    rootdir4 = 'C:\\Repos\\MEI\\crawler2019\\output\\html\\publico\\misc'
    
    rootdir5 = 'C:\\Repos\\MEI\\antigo-lei-repo\\crawler\\output\\html\\publico\\misc'
    rootdir6 = 'C:\\Repos\\MEI\\antigo-lei-repo\\crawler\\output\\html\\publico\\sublinks\\.publico.clix.pt'
    rootdir7 = 'C:\\Repos\\MEI\\antigo-lei-repo\\crawler\\output\\html\\publico\\sublinks\\.publico.pt'
    rootdir8 = 'C:\\Repos\\MEI\\antigo-lei-repo\\crawler\\output\\html\\publico\\sublinks\\desporto.publico.clix.pt'
    rootdir9 = 'C:\\Repos\\MEI\\antigo-lei-repo\\crawler\\output\\html\\publico\\sublinks\\desporto.publico.pt'
    rootdir10 = 'C:\\Repos\\MEI\\antigo-lei-repo\\crawler\\output\\html\\publico\\sublinks\\economia.publico.pt'
    rootdir11 = 'C:\\Repos\\MEI\\antigo-lei-repo\\crawler\\output\\html\\publico\\sublinks\\economia.publico.clix.pt'
    rootdir12 = 'C:\\Repos\\MEI\\antigo-lei-repo\\crawler\\output\\html\\publico\\sublinks\\ecosfera.publico.clix.pt'
    rootdir13 = 'C:\\Repos\\MEI\\antigo-lei-repo\\crawler\\output\\html\\publico\\sublinks\\ecosfera.publico.pt'
    rootdir14 = 'C:\\Repos\\MEI\\antigo-lei-repo\\crawler\\output\\html\\publico\\sublinks\\jornal.publico.pt'
    rootdir15 = 'C:\\Repos\\MEI\\antigo-lei-repo\\crawler\\output\\html\\publico\\sublinks\\publico.pt'
    rootdir16 = 'C:\\Repos\\MEI\\ARQUIVO-PT-FINAL\\html-ja-limpo-pelo-scrapper-final-1a-fase'
    
    
    paths = (rootdir, rootdir2, rootdir3, rootdir4, rootdir5, rootdir6, rootdir7, rootdir8, rootdir9, rootdir10, rootdir11, rootdir12, rootdir13, rootdir14, rootdir15, rootdir16)
    c=1
    #for subdir, dirs, files in os.walk(rootdir):
    for subdir, dirs, files in chain.from_iterable(os.walk(path) for path in paths):
        
        files = [f for f in files if not f[0] == '.']
            
        for file in files:
            try:
                HtmlFile = open(os.path.join(subdir, file), 'r', encoding='utf-8')
                html_text = HtmlFile.read()
                HtmlFile.close()
                print('File #'+str(c)+': ')
                c+=1

                absolute_path = os.path.join(subdir, file)


                publico_scraper.scrap_publico(html_text, str(file), absolute_path)
            except:
                with open("log_scrap_failed.txt", "a+") as myfile:
                    myfile.write(absolute_path+'\n')

"""

def main():

    url = 'https://arquivo.pt/noFrame/replay/20020802154959/http://www.ultimahora.publico.pt:80/default.asp?c=171'

    res = requests.get(url)

    html_page = res.content

    soup = BeautifulSoup(html_page, 'lxml')

    [x.extract() for x in soup.find_all('script')]
    [x.extract() for x in soup.find_all('style')]
    [x.extract() for x in soup.find_all('meta')]
    [x.extract() for x in soup.find_all('noscript')]

    with open("output2.html", "w") as file:
        file.write(str(soup))

"""


#main()

#publico2001_2002("https://arquivo.pt/noFrame/replay/20020615215425/http://ultimahora.publico.pt:80/shownews.asp?id=148725&idCanal=63")
#publico2003_2004("https://arquivo.pt/noFrame/replay/20031201044357/http://ultimahora.publico.pt:80/shownews.asp?id=1158375&idCanal=12")
#publico2005_2006_2007_Jun("https://arquivo.pt/noFrame/replay/20060922030255/http://publico.clix.pt:80/shownews.asp?id=1268375&idCanal=90")
#publico2007Jun_Nov("https://arquivo.pt/noFrame/replay/20070607094029/http://ultimahora.publico.clix.pt/noticia.aspx?id=1296068")
#publico2007Nov_2008("https://arquivo.pt/noFrame/replay/20091001022453/http://ultimahora.publico.clix.pt/noticia.aspx?id=1388387&idCanal=61")
#publico2009Set_16Nov2012("https://arquivo.pt/noFrame/replay/20120303161950/http://www.publico.pt/Sociedade/especialistas-em-saude-publica-associam-excesso-de-mortalidade-a-crise-economica-1536215")
#publico16Nov2012_('https://arquivo.pt/noFrame/replay/20161002185315/https://www.publico.pt/sociedade/noticia/pcp-vai-perguntar-ao-governo-se-congelamento-de-despesa-dos-hospitais-afecta-prestacao-de-cuidados-1745906')
#minoritiesFilter()

scrap_news()


#HtmlFile = open("/Users/leandro/Desktop/publico/misc/1584921398.5500112.html", 'r', encoding='utf-8')
#html_text = HtmlFile.read()
#publico_scraper.getNewsDate(html_text)

#notNews("https://arquivo.pt/noFrame/replay/20040831085624/http://publico.pt/", ["feira"])
