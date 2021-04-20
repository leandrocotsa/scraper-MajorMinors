#!./env/bin/python3

from bs4 import BeautifulSoup
import re
import requests
import fileinput
import os
import datetime
import news
#from selenium import webdriver

IGNORE_MINORITIES = True

minorities_dictionary = {
"ciganos" : ["cigan", " romani ", " romanho"],
"refugiados" : ["refugiad"],
"mulheres" : ["primeira mulher", "feminismo", "violência doméstica", "mulheres", "direitos das mulheres", "grupo de mulheres", "movimento de mulheres", "igualdade de direitos", "igualdade de salário", "igualdade salarial", "menina", "prostituta", "prostituição", "rainha", "princesa", " moça ", "rapariga", " cantora ", "donzela", " mulherio", "estudos de género", "questões de género", "estudos de gênero", "questões de gênero", "violência de género", "violência de gênero", "igualdade de género", "igualdade de gênero", "abuso sexual"],
"animais" : ["tourada", " vias de extinção", "abandono de animais", "touro", " animal", " animais", " canil", " cão", " cães", " zoo ", " zoológico", " espécie protegida", "tartarugas", "andorinhas", " circo ", "lince", "pesca", "elefantes", "matadouro", "girafa", "galgos", "toureiro", "vegano", "vegetariano", "pássaros", " aves ", " marfim", "cavalo", " suíno", "galinha", " vaca", "ovelha", "consumo de carne", " carne de "],
"homossexuais" : ["lgbt", " gay", "homofobia", "homossexua", "homosexua" "lésbica", "sexualidade", "homofóbic", "transexual", "drag queen", "bicha", "pessoas do mesmo sexo", "sair do armário", "pride", "ILGA", "orientação sexual", "efeminado", "afeminado", "bissexual", "andrógeno", "discriminação sexual"],
"africanos" : ["população negra", "comunidade negra", "racismo", "pele negra", "cor negra", "african", "racista", "cor da pele", "afro-americano", "cabo verdiano", "Somália", "Nigéria", "angolanos"],
"asiáticos" : ["asiátic", "trabalhadores chineses", "crianças chinesas", "chines", "chinês"],
"migrantes" : ["imigrante", "imigração", "imigrar", "trabalhador ilegal", " deportado", " deportação", "emigrante", "emigração", "emigrar"]
}

priority_words = {
"ciganos" : ["cigan"],
"refugiados" : ["refugiad"],
"mulheres" : ["primeira mulher", "feminismo", "violência doméstica", "direitos das mulheres", "movimento de mulheres", "igualdade de salário", "igualdade salarial", "questões de género", "igualdade de género"],
"animais" : ["tourada", " vias de extinção", "abandono de animais", "matadouro", "consumo de carne", "maus tratos aos animais", "abuso de animais"],
"homossexuais" : ["lgbt", " gay", "homofobia", "homossexua", "homofóbic", "transexual", "pessoas do mesmo sexo", "ILGA", "orientação sexual", "discriminação sexual"],
"africanos" : ["população negra", "comunidade negra", "pele negra", "cor negra"],
"asiáticos" : ["asiátic", "trabalhadores chineses", "crianças chinesas"],
"migrantes" : ["imigrante", "imigração", "imigrar", "trabalhador ilegal", "emigrante", "emigração", "emigrar"]
}


end_date_publico2001_2002 = datetime.datetime(2003, 2, 14)
end_date_publico2003_2004 = datetime.datetime(2005, 2, 22)
end_date_publico2005_2006_2007_Jun = datetime.datetime(2007, 5, 18)
end_date_publico2007Jun_Nov = datetime.datetime(2007, 11, 30)
end_date_publico2007Nov_2008_2009Set = datetime.datetime(2009, 9, 30)
end_date_publico2009Set_16Nov2012 = datetime.datetime(2012, 11, 17)
end_date_publico16Nov2012_Out2016 = datetime.datetime(2016, 11, 21)

all_noticias = []


def publico2001_2002(html, filename, strDate, url, absolute_path):

    soup = requestBeautifulSoup(html)

    full_texto = ""

    dic_minorias = {}

    title = soup.find('span', {'class': 'ultnottit'})
    texto = soup.find('span', {'class': 'ultnottxt'})

    try:
        paragraphs = texto.find_all('aux')
        title_text = title.text.strip()
    except:
        os.remove(absolute_path)
        print("removed NOT NEWS => " + absolute_path)
        return

    #autor = soup.find('a', {'class': 'supenviadoslinks'})


    #print("TÍTULO: \n")
    #print(title_text + "\n")

    if paragraphs:
        #print("TEXTO: \n")
        for paragraph in paragraphs:
            clean_paragraph = paragraph.text.strip()
            full_texto += clean_paragraph
        full_texto = re.sub(r'(?<=[.,])(?=[^\s])', r' ', full_texto)
        #print(full_texto + "\n")

        #print("AUTOR: \n")
        #print(autor.text + "\n")

        addPriority(whichMinorities(title_text), dic_minorias, 7)
        addPriority(whichMinorities(full_texto), dic_minorias, 2)

        addPriority(mentionsMinorityName(full_texto, dic_minorias), dic_minorias, 4)

        if dic_minorias or IGNORE_MINORITIES==True:
            aNoticia = news.Noticia(full_texto, title_text, filename, strDate, url)
            aNoticia.setPrioridade(dic_minorias)
            #aNoticia.printNews()
            print("FOUND => " + absolute_path)
        else:
            #os.remove(absolute_path)
            print("removed NOT MENTION MINORITIES => " + absolute_path)

    else:
        os.remove(absolute_path)
        print("removed NOT NEWS => " + absolute_path)





def publico2003_2004(html, filename, strDate, url, absolute_path):

    soup = requestBeautifulSoup(html)

    full_texto = ""

    dic_minorias = {}

    comments_text = []

    ante_titulo = soup.find('span', {'class': 'textoAntetitulo'})
    title = soup.find('span', {'class': 'textoTitulo'})
    texto = soup.find('div', {'class': 'texto'})

    try:
        paragraphs = texto.find_all('aux')
        ante_titulo_text = ante_titulo.text.strip()
        title_text = title.text.strip()
    except:
        os.remove(absolute_path)
        print("removed NOT NEWS => " + absolute_path)
        return



    try:

        comments = soup.select('td > span.ultnottxt')

        if comments:

            #print("COMENTÁRIOS: \n")
            for comment in comments:
                if(len(comment.text) > 40):
                    comment_clean = re.sub(r'(?<=[.,])(?=[^\s])', r' ', comment.text)
                    comment_clean = re.sub(r'[\n]', r' ', comment.text)
                    comments_text.append(comment_clean.strip())

            #for comment in comments_text:
                #print(comment + "\n")

    except:
        pass

    #print("ANTE-TÍTULO: \n")
    #print(ante_titulo_text + "\n")

    #print("TÍTULO: \n")
    #print(title_text + "\n")
    if paragraphs:

        #print("TEXTO: \n")
        for paragraph in paragraphs:
            clean_paragraph = paragraph.text.strip()
            full_texto += clean_paragraph
        full_texto = re.sub(r'(?<=[.,])(?=[^\s])', r' ', full_texto)
        #print(full_texto + "\n")




        addPriority(whichMinorities(ante_titulo_text), dic_minorias, 3)
        addPriority(whichMinorities(title_text), dic_minorias, 7)
        addPriority(whichMinorities(full_texto), dic_minorias, 2)

        addPriority(mentionsMinorityName(full_texto, dic_minorias), dic_minorias, 4)

        if dic_minorias or IGNORE_MINORITIES==True:
            aNoticia = news.Noticia(full_texto, title_text, filename, strDate, url)
            aNoticia.setAnteTitulo(ante_titulo_text)
            aNoticia.setComentarios(comments_text)

            aNoticia.setPrioridade(dic_minorias)
            #aNoticia.printNews()
            print("FOUND => " + absolute_path)
        else:
            #os.remove(absolute_path)
            print("removed NOT MENTION MINORITIES => " + absolute_path)

    else:
        os.remove(absolute_path)
        print("removed NOT NEWS => " + absolute_path)





def publico2005_2006_2007_Jun(html, filename, strDate, url, absolute_path):

    soup = requestBeautifulSoup(html)

    full_texto = ""

    dic_minorias = {}

    noticia = soup.find('div', {'id': 'caixasNoticias'})



    try:
        texto = noticia.find('div', {'id': 'texto'})
        title = noticia.find('span', {'class': 'manchete'})
        paragraphs = texto.find_all('aux')
        title_text = title.text.strip()
    except:
        os.remove(absolute_path)
        print("removed NOT NEWS => " + absolute_path)
        return


    #print("TÍTULO: \n")
    #print(title_text + "\n")

    #print("TEXTO: \n")

    if paragraphs:

        for paragraph in paragraphs:
            clean_paragraph = paragraph.text.strip()
            full_texto += clean_paragraph
        full_texto = re.sub(r'(?<=[.,])(?=[^\s])', r' ', full_texto)
        #print(full_texto + "\n")

        addPriority(whichMinorities(title_text), dic_minorias, 7)
        addPriority(whichMinorities(full_texto), dic_minorias, 2)

        addPriority(mentionsMinorityName(full_texto, dic_minorias), dic_minorias, 4)


        if dic_minorias or IGNORE_MINORITIES==True:
            aNoticia = news.Noticia(full_texto, title_text, filename, strDate, url)
            aNoticia.setPrioridade(dic_minorias)
            #aNoticia.printNews()
            print("FOUND => " + absolute_path)

        else:
            #os.remove(absolute_path)
            print("removed NOT MENTION MINORITIES => " + absolute_path)

    else:
        os.remove(absolute_path)
        print("removed NOT NEWS => " + absolute_path)


def publico2007Jun_Nov(html, filename, strDate, url, absolute_path):

    soup = requestBeautifulSoup(html)

    full_texto = ""

    dic_minorias = {}

    noticia = soup.find('div', {'id': 'caixasNoticias'})



    try:
        title = noticia.find('span', {'class': 'manchete'})
        textDiv = noticia.find('div', {'id': 'texto'})
        paragraphs = textDiv.find_all('p')
        title_text = title.text.strip()
    except:
        os.remove(absolute_path)
        print("removed NOT NEWS => " + absolute_path)
        return



        #print("TÍTULO: \n")
        #print(title_text + "\n")

    if paragraphs:
        #print("TEXTO: \n")
        for paragraph in paragraphs:
            clean_paragraph = paragraph.text.strip()
            full_texto += clean_paragraph
        full_texto = re.sub(r'(?<=[.,])(?=[^\s])', r' ', full_texto)
        #print(full_texto + "\n")

        addPriority(whichMinorities(title_text), dic_minorias, 7)
        addPriority(whichMinorities(full_texto), dic_minorias, 2)

        addPriority(mentionsMinorityName(full_texto, dic_minorias), dic_minorias, 4)

        if dic_minorias or IGNORE_MINORITIES==True:
            aNoticia = news.Noticia(full_texto, title_text, filename, strDate, url)
            aNoticia.setPrioridade(dic_minorias)
            #aNoticia.printNews()
            print("FOUND => " + absolute_path)
        else:
            #os.remove(absolute_path)
            print("removed NOT MENTION MINORITIES => " + absolute_path)

    else:
        os.remove(absolute_path)
        print("removed NOT NEWS => " + absolute_path)





def publico2007Nov_2008_2009Set(html, filename, strDate, url, absolute_path):

    soup = requestBeautifulSoup(html)

    dic_minorias = {}
    comments_text = []

    img_full_url = ""

    noticia = soup.find('div', {'id': 'ctl00_ContentPlaceHolder1_DivNoticia'})
    anteTitulo = soup.find('span', {'id': 'ctl00_ContentPlaceHolder1_txtAnteTitulo'})



    try:
        title = noticia.find('span', {'id': 'ctl00_ContentPlaceHolder1_txtTitulo'})
        textDiv = noticia.find('span', {'id': 'ctl00_ContentPlaceHolder1_txtTextos'})
        ante_titulo_text = anteTitulo.text.strip()
        title_text = title.text.strip()
        clean_text = textDiv.text.strip()
        clean_text = re.sub(r'(?<=[.,])(?=[^\s])', r' ', clean_text)
    except:
        os.remove(absolute_path)
        print("removed NOT NEWS => " + absolute_path)
        return

        #print("ANTE-TÍTULO: \n")
        #print(ante_titulo_text + "\n")

        #print("TÍTULO: \n")
        #print(title_text + "\n")

        #clean_text = re.sub(r'\s+', ' ', textDiv.text)

        #print("TEXTO: \n")
        #print(clean_text)

    if soup.find('div', {'id': 'TextoComentario'}):

        comments = soup.find_all('div', {'id': 'TextoComentario'})

        if comments:

            #print("COMENTÁRIOS: \n")
            for comment in comments:

                try:
                    if comment.text:
                        if comment.text[0].isalpha():
                            comment_clean = re.sub(r'(?<=[.,])(?=[^\s])', r' ', comment.text)
                            comment_clean = re.sub(r'[\n]', r' ', comment.text)
                            comments_text.append(comment_clean.strip())
                except:
                    pass


            #for comment in comments_text:
                #print(comment.text + "\n")

    try:
        img = soup.find('img', {'id': 'ctl00_ContentPlaceHolder1_imagemNoticia'})
        img_url = img['src']
        img_full_url = "https://arquivo.pt" + img_url
    except:
        pass


    addPriority(whichMinorities(ante_titulo_text), dic_minorias, 3)
    addPriority(whichMinorities(title_text), dic_minorias, 7)
    addPriority(whichMinorities(clean_text), dic_minorias, 2)

    addPriority(mentionsMinorityName(clean_text, dic_minorias), dic_minorias, 4)


    if dic_minorias or IGNORE_MINORITIES==True:
        aNoticia = news.Noticia(clean_text, title_text, filename, strDate, url)
        aNoticia.setAnteTitulo(ante_titulo_text)
        aNoticia.setComentarios(comments_text)
        aNoticia.setImageURL(img_full_url)
        aNoticia.setPrioridade(dic_minorias)
        #aNoticia.printNews()
        print("FOUND => " + absolute_path)
    else:
        #os.remove(absolute_path)
        print("removed NOT MENTION MINORITIES => " + absolute_path)






def publico2009Set_16Nov2012(html, filename, strDate, url, absolute_path):


    soup = requestBeautifulSoup(html)

    dic_minorias = {}

    comments_text = []

    img_full_url = ""

    noticia = soup.find('div', {'class': 'content-noticia'})
    introNoticia = soup.find('div', {'class': 'noticia-intro'})


    try:
        textDiv = noticia.find('div', {'class': 'noticia'})
        paragraphs = textDiv.p
        introNoticia_text = re.sub(r'\s+', ' ', introNoticia.text)
        introNoticia_text = introNoticia_text.strip()
        clean_text = re.sub(r'\s+', ' ', paragraphs.text)
        clean_text = paragraphs.text.strip()
        clean_text = re.sub(r'(?<=[.,])(?=[^\s])', r' ', clean_text)
    except:
        os.remove(absolute_path)
        print("removed NOT NEWS => " + absolute_path)
        return

    if noticia.find('div', {'class': 'content-noticia-title'}).h2:

        title = noticia.find('div', {'class': 'content-noticia-title'}).h2

    elif noticia.find('div', {'class': 'content-noticia-title'}).h1:

        title = noticia.find('div', {'class': 'content-noticia-title'}).h1

    else:
        os.remove(absolute_path)
        print("removed NOT NEWS => " + absolute_path)
        return

    #comments = soup.find_all('div', {'class': 'comentario-entry-content'})


    #print("INTRO-NOTICIA: \n")
    #print(introNoticia_text + "\n")


    title_text = re.sub(r'\s+', ' ', title.text)
    title_text = title_text.strip()
    #print("TÍTULO: \n")
    #print(title_text + "\n")


    #print("TEXTO: \n")
    #print(clean_text)

    try:
        imgDiv = soup.find('div', {'class': 'noticia-img'})
        img_full_url = imgDiv.find('img')['src']
    except:
        pass


    try:
        top_comment = soup.find('div', {'class': 'comentariotop'}).p

        if top_comment:

            if len(top_comment.text) > 1:

                comment_clean = re.sub(r'(?<=[.,])(?=[^\s])', r' ', top_comment.text)
                comment_clean = re.sub(r'[\n]', r' ', top_comment.text)
                comments_text.append(comment_clean.strip())

                #for comment in comments_text:
                    #print(comment.text + "\n")
    except:
        pass





    addPriority(whichMinorities(introNoticia_text), dic_minorias, 3)
    addPriority(whichMinorities(title_text), dic_minorias, 7)
    addPriority(whichMinorities(clean_text), dic_minorias, 2)

    addPriority(mentionsMinorityName(clean_text, dic_minorias), dic_minorias, 4)

    if dic_minorias or IGNORE_MINORITIES==True:
        aNoticia = news.Noticia(clean_text, title_text, filename, strDate, url)
        aNoticia.setIntroNoticia(introNoticia_text)
        aNoticia.setComentarios(comments_text)
        aNoticia.setImageURL(img_full_url)
        aNoticia.setPrioridade(dic_minorias)
        #aNoticia.printNews()
        print("FOUND => " + absolute_path)
    else:
        #os.remove(absolute_path)
        print("removed NOT MENTION MINORITIES => " + absolute_path)




def publico16Nov2012_Out2016(html, filename, strDate, url, absolute_path):   #so far october 2016

    soup = requestBeautifulSoup(html)

    dic_minorias = {}

    full_texto = ""

    tags_array = []

    img_full_url = ""


    introNoticia = soup.find('div', {'class': 'entry-blurb'})
    noticia = soup.find('div', {'class': 'entry-body'})


    try:
        paragraphs = noticia.find_all('p')
        introNoticia_text = introNoticia.text.strip()
        title = soup.find('header', {'class': 'entry-header single-header'}).h1
        title_text = title.text.strip()
    except:
        os.remove(absolute_path)
        print("removed NOT NEWS => " + absolute_path)
        return

        #print("INTRO-NOTICIA: \n")
        #print(introNoticia_text)

        #print("TITLE: \n")
        #print(title_text)

    try:

        tags_ol = soup.find('ol', {'itemprop': 'keywords'})

        if tags_ol:

            tags = tags_ol.find_all("li")

            #print("TAGS: \n")
            for tag in tags:
                tags_array.append(tag.find("a").text)
                #print(tags_array)

    except:
        pass

    try :
        article = soup.find('article', {'class': 'article'})
        imgDiv = article.find('figure')
        img_full_url = imgDiv.find('img')['src']
        if not img_full_url.startswith('http'):
            img_full_url = "https:" + img_full_url
    except:
        pass


    if paragraphs:
        #print("TEXTO: \n")
        for paragraph in paragraphs:
                clean_paragraph = paragraph.text.strip()
                full_texto += clean_paragraph
        full_texto = re.sub(r'(?<=[.,])(?=[^\s])', r' ', full_texto)

        #print(full_texto)

        addPriority(whichMinorities(introNoticia_text), dic_minorias, 3)
        addPriority(whichMinorities(title_text), dic_minorias, 7)
        addPriority(whichMinorities(full_texto), dic_minorias, 2)
        aux = "  "
        topicsToString = aux.join(tags_array)
        addPriority(whichMinorities(topicsToString), dic_minorias, 5)

        addPriority(mentionsMinorityName(full_texto, dic_minorias), dic_minorias, 4)

        if dic_minorias or IGNORE_MINORITIES==True:
            aNoticia = news.Noticia(full_texto, title_text, filename, strDate, url)
            aNoticia.setIntroNoticia(introNoticia_text)
            aNoticia.setImageURL(img_full_url)
            aNoticia.setPrioridade(dic_minorias)
            aNoticia.setTags(tags_array)
            #aNoticia.printNews()
            print("FOUND => " + absolute_path)
        else:
            #os.remove(absolute_path)
            print("removed NOT MENTION MINORITIES => " + absolute_path)

    else:
        os.remove(absolute_path)
        print("removed NOT NEWS => " + absolute_path)


def publico2017_2018(html, filename, strDate, url, absolute_path):

    soup = requestBeautifulSoup(html)

    dic_minorias = {}

    full_texto = ""

    img_full_url = ""

    tags_array = []

    header = soup.find('header', {'id': 'story-header'})
    noticia = soup.find('div', {'id': 'story-body'})

    try:
        title = header.h1
        introNoticia = header.find('div', {'class': 'story__blurb'}).p
        paragraphs = noticia.find_all('p')
        introNoticia_text = introNoticia.text.strip()
        title_text = title.text.strip()
    except:
        os.remove(absolute_path)
        print("removed NOT NEWS => " + absolute_path)
        return


    try:
        imgDiv = soup.find('div', {'class': 'camera'})
        img_full_url = imgDiv.find('img')['data-media-viewer']
    except:
        pass


    try:
        tagsul = soup.find('ul', {'class': 'menu--tag'})
        tags = tagsul.find_all("li")
        for tag in tags:
            tags_array.append(tag.find("a").text)
    except:
        pass


        #print("INTRO-NOTICIA: \n")
        #print(introNoticia_text)


        #print("TITLE: \n")
        #print(title_text)

        #print("TEXTO: \n")
    if paragraphs:
        for paragraph in paragraphs:
                clean_paragraph = paragraph.text.strip()
                full_texto += clean_paragraph
        full_texto = re.sub(r'(?<=[.,])(?=[^\s])', r' ', full_texto)

        #print(full_texto)

        addPriority(whichMinorities(introNoticia_text), dic_minorias, 3)
        addPriority(whichMinorities(title_text), dic_minorias, 7)
        addPriority(whichMinorities(full_texto), dic_minorias, 2)
        aux = "  "
        topicsToString = aux.join(tags_array)
        addPriority(whichMinorities(topicsToString), dic_minorias, 5)

        addPriority(mentionsMinorityName(full_texto, dic_minorias), dic_minorias, 4)

        if dic_minorias or IGNORE_MINORITIES==True:
            aNoticia = news.Noticia(full_texto, title_text, filename, strDate, url)
            aNoticia.setIntroNoticia(introNoticia_text)
            aNoticia.setTags(tags_array)
            aNoticia.setImageURL(img_full_url)
            aNoticia.setPrioridade(dic_minorias)
            #aNoticia.printNews()
            print("FOUND => " + absolute_path)
        else:
            #os.remove(absolute_path)
            print("removed NOT MENTION MINORITIES => " + absolute_path)

    else:
        os.remove(absolute_path)
        print("removed NOT NEWS => " + absolute_path)




def notNews(html):

    frases = []


    for minority in minorities_dictionary:
        for word in minorities_dictionary[minority]:
            matches = re.findall(r"(?<=[.?\s!>=])[^.?!<>\/=&]*" + word + r"[^.?!<>\/]*(?=[\s.?!<])[.?!]?", html,  re.IGNORECASE)
            for match in matches:
                if len(match)>35:
                    frases.append(match)

    print(frases)


def whichMinorities(text):

    minorias = []

    for minority in minorities_dictionary:
        if(re.search(r'|'.join(minorities_dictionary[minority]), text, re.IGNORECASE)):
            minorias.append(minority)

    return minorias

def addPriority(array, dic_minorias, priority_value):


    for minority in array:
        if minority in dic_minorias:
            dic_minorias[minority] += priority_value
        else:
            dic_minorias[minority] = priority_value


def mentionsMinorityName(text, dic_minorias):
    minorias = []

    for minority in dic_minorias:
        if(re.search(r'|'.join(priority_words[minority]), text, re.IGNORECASE)):
            minorias.append(minority)

    return minorias



def requestBeautifulSoup(html):

    soup = BeautifulSoup(html, "lxml")


    [x.extract() for x in soup.find_all('script')]
    [x.extract() for x in soup.find_all('style')]
    [x.extract() for x in soup.find_all('meta')]
    [x.extract() for x in soup.find_all('noscript')]

    return soup


def getNewsDate(html):

    date_html = re.findall(r'<!--https://arquivo.pt/noFrame/replay/(\d*)/', html)

    date_str = date_html[0]

    year = int(date_str[0:4])

    month = int(date_str[4:6])

    day = int(date_str[6:8])

    date = datetime.datetime(year, month, day)

    return date



def scrap_publico(html_text, filename, absolute_path):

    html_date = getNewsDate(html_text)

    urlOrginal = re.findall(r'<!--(.*)-->', html_text)

    url = urlOrginal[0]

    strDate = html_date.strftime("%Y-%m-%d")



    if html_date<end_date_publico2001_2002:

        publico2001_2002(html_text, filename, strDate, url, absolute_path)

    elif end_date_publico2001_2002<html_date<end_date_publico2003_2004:

        publico2003_2004(html_text, filename, strDate, url, absolute_path)

    elif end_date_publico2003_2004<html_date<end_date_publico2005_2006_2007_Jun:

        publico2005_2006_2007_Jun(html_text, filename, strDate, url, absolute_path)

    elif end_date_publico2005_2006_2007_Jun<html_date<end_date_publico2007Jun_Nov:

        publico2007Jun_Nov(html_text, filename, strDate, url, absolute_path)

    elif end_date_publico2007Jun_Nov<html_date<end_date_publico2007Nov_2008_2009Set:

        publico2007Nov_2008_2009Set(html_text, filename, strDate, url, absolute_path)

    elif end_date_publico2007Nov_2008_2009Set<html_date<end_date_publico2009Set_16Nov2012:

        publico2009Set_16Nov2012(html_text, filename, strDate, url, absolute_path)

    elif end_date_publico2009Set_16Nov2012<html_date<end_date_publico16Nov2012_Out2016:

        publico16Nov2012_Out2016(html_text, filename, strDate, url, absolute_path)

    elif end_date_publico16Nov2012_Out2016<html_date:

        publico2017_2018(html_text, filename, strDate, url, absolute_path)

    else:
        #notNews(html_text)
        os.remove(absolute_path)
        print("NO DATE")
        with open("log_publico_scrapper_NO_DATE.txt", "a+") as myfile:
            myfile.write(absolute_path+'\n')








#res = requests.get("https://arquivo.pt/noFrame/replay/20070514150251/http://ultimahora.publico.clix.pt/noticia.aspx?id=1292561&idCanal=18")

#html_page = res.content

#publico2001_2002(html_page, "lol", "lol", "lol", "lol")
#publico2003_2004(html_page, "lol", "lol", "lol", "lol")
#publico2005_2006_2007_Jun(html_page, "lol", "lol", "lol", "lol")
#publico2007Jun_Nov(html_page, "lol", "lol", "lol", "lol")
#publico2007Nov_2008_2009Set(html_page, "lol", "lol", "lol", "lol")
#publico2009Set_16Nov2012(html_page, "lol", "lol", "lol", "lol")

#publico16Nov2012_Out2016(html_page, "lol", "lol", "lol", "lol")

#publico2017_2018(html_page, "lol", "lol", "lol", "lol")



#HtmlFile = open("/Users/leandro/Desktop/publico/misc/1584921037.8813236.html", 'r', encoding='utf-8')
#html_text = HtmlFile.read()

#publico2009Set_16Nov2012(html_text)

#getNewsDate(html_text)
