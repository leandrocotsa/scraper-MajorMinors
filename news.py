#!./env/bin/python3

from ontology import ontology

class Noticia:

    def __init__(self, body, title, filename, html_date, url):
        self._body = body
        self._title = title
        self._fileName = filename
        self._date = html_date#p.e.2019-01-15
        self._url = url

        self._prioridade = {}#p.e.{"Asiático", "12"}
        self._minorias = []
        self._tags = []
        self._anteTitulo = ""
        self._introNoticia = ""
        self._comentarios = []
        self._imageURL = ""

    def setMinorias(self, minorias):
        self._minorias = minorias

    def setAnteTitulo(self, anteTitulo):
        self._anteTitulo = anteTitulo

    def setIntroNoticia(self, introNoticia):
        self._introNoticia = introNoticia

    def setTags(self, tags):
        self._tags = tags

    def setPrioridade(self, prioridade):
        self._prioridade = prioridade
        self.addMinorias()
        ###ENVIA PARA O GERADOR DE ONTOLOGIA:
        ontologia = ontology.Ontology(self)
        #try:
        #    ontologia = ontology.Ontology(self)
        #except:
        #    with open("log_news_py_ontology_failed.txt", "a+") as myfile:
        #        myfile.write(filename+'\n')

    def setEntities(self, entities):
        self._entities = entities

    def setComentarios(self, comentarios):
        self._comentarios = comentarios

    def setImageURL(self, imageURL):
        self._imageURL = imageURL

    def setDate(self, date):
        self._date = date

    def setFileName(self, date):
        self._date = date

    def __str__(self):
        return ("\nANTE-TITulo: \n"
        + self._anteTitulo
        + "\nINTRO-NOTICIA: \n"
        + self._introNoticia
        + "\nTAGS: \n"
        + self._tags
        + "\nTITULO: \n"
        + self._title
        + "\nBODY: \n"
        + self._body
        + "\nMINORIAS: \n"
        + self._minorias
        + "\nPRIORIDADE: \n"
        + self._prioridade)

    def printNews(self):
        print("\nANTE-TITULO: \n")
        print(self._anteTitulo)
        print("\nINTRO-NOTICIA: \n")
        print(self._introNoticia)
        print("\nTAGS: \n")
        print(self._tags)
        print("\nTITULO: \n")
        print(self._title)
        print("\nBODY: \n")
        print(self._body)
        print("\nMINORIAS: \n")
        print(self._minorias)
        print("\nPRIORIDADE: \n")
        print(self._prioridade)
        print("\nCOMENTÁRIOS: \n")
        print(self._comentarios)
        print("\nIMAGE URL: \n")
        print(self._imageURL)
        print("\nDATE: \n")
        print(self._date)


    def addMinorias(self):
        minorias = []
        for minority in self._prioridade.keys():
            minorias.append(minority)

        self.setMinorias(minorias)
