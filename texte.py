#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from ontology import ontology

class Teste:
    def __init__(self):
        self.title = "O Paulo tem um cão chamado gato em Braga."
        self.body = "O Paulo tem um cão chamado gato em Braga, filho do António Costa e Cavaco Silva."
        self.prioridade = {"Asiático", "12"}
        self.minorias = ["Asiático"]
        self.tags = ["Tag-teste"]
        self.fileName = "9988.html"
        self.date = "2019-01-15"
        self.url = "http://google.pt"
        self.anteTitulo = ""
        self.introNoticia = ""


temp = Teste()

teste = ontology.Ontology(temp)

input("Resultou?")
