 #!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
sys.path.append("..")

import re, pathlib, importlib


class Ontology():

    def __init__(self):


        self.uri = 'http://sparql.ilch.uminho.pt/minors'

        self.individuals = {#Placeholder for the individuals found in the text
        "animal":[],
        "city":[],
        "continent":[],
        "country":[],
        "otherPlace":[],
        "entity":[],
        "ethnicity":[],
        "keyword":[],
        "politicalParty":[],
        "religion":[],
        "weekday":[],
        "month":[],

        "job":[],
        "person":[],

        "minority":[],
        "tag":[],
        "priority":[],

        "comment":[],
        "image":[],
        }
        
        self.load()
        for i in self.individuals:
            if i == "job":
                print(i+":>>>>>>>>>>>>>>>>>>>>>>>>")
                print(self.individuals[i])
        
    def load(self):
        for individualType in self.individuals:
            #filePath = pathlib.Path.cwd().joinpath('ontology','data','individuals',individualType+'.txt')
            filePath = pathlib.Path.cwd().joinpath('data','individuals',individualType+'.txt')
            search = r'###  ' + self.uri+'#'
            if individualType not in ["tag", "job"]:
                with open(filePath, "r", encoding="utf-8") as file:
                    data = file.read()
                    get = data.split(search)
                    for e in get:
                        if individualType == "person":
                            job = re.match(r'.*:hasJob : ', e)[0]
                            if job:
                                self.individuals["job"].append(job.replace(" ;", "").strip())                        
                        id = re.match(r'.*\n', e)[0]
                        if id:
                            self.individuals[individualType].append(id.strip())
            """elif individualType == "tag":
                p = pathlib.Path.cwd().joinpath('data','individuals','article.txt')
                with open(p, "r", encoding="utf-8") as file:
                    data = file.read()
                    get = data.split(search)
                    for e in get:
                        id = re.match(r'.*:referesTag\n', e)[0].strip()
                        self.individuals[individualType].append(id)"""

                
                
                
a=Ontology()