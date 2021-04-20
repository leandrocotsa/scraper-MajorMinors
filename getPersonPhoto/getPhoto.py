#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}

paths = response.download(arguments)

print(paths)


"""
import urllib.parse
from requests_html import HTMLSession
from data import person


session = HTMLSession()

def main():
    for p in person.data:
        print(p)
        photo = searchPhoto(p)

def searchPhoto(search):
    fullUrl = makeUrl(search)

    respHTML = getHtml(fullUrl, render=True)
    photo = getFirstImage(respHTML)
    return photo

def makeUrl(search):
    urlEncode = search.replace(' ', '+')
    searchUrl = "https://duckduckgo.com/?q="+urlEncode+"&t=h_&iax=images&ia=images"
    print(searchUrl)
    return searchUrl

def getHtml(link, render=False):
    resp = session.get(link)
    if render == True:
        resp.html.render()
    #html = resp.text
    return resp

def getFirstImage(resp):
    firstImg = resp.html.xpath('//*[@id="zci-images"]/div/div[2]/div/div[1]/div[1]/span/img')
    print(firstImg)
"""

















### https://stackoverflow.com/questions/56132631/how-to-scrape-images-from-duckduckgos-image-search-results-in-python
"""import requests
import re
import json
import os


def search(keywords, max_results=None):
    url = 'https://duckduckgo.com/'
    params = {
        'q': keywords
    }

    print("Hitting DuckDuckGo for Token")

    #   First make a request to above URL, and parse out the 'vqd'
    #   This is a special token, which should be used in the subsequent request
    res = requests.post(url, data=params)
    searchObj = re.search(r'vqd=([\d-]+)\&', res.text, re.M | re.I)

    if not searchObj:
        print("Token Parsing Failed !")
        return -1

    print("Obtained Token")

    headers = {
        'dnt': '1',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'x-requested-with': 'XMLHttpRequest',
        'accept-language': 'en-GB,en-US;q=0.8,en;q=0.6,ms;q=0.4',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'referer': 'https://duckduckgo.com/',
        'authority': 'duckduckgo.com',
    }

    params = (
        ('l', 'wt-wt'),
        ('o', 'json'),
        ('q', keywords),
        ('vqd', searchObj.group(1)),
        ('f', ',,,'),
        ('p', '2')
    )

    requestUrl = url + "i.js"

    try:
        res = requests.get(requestUrl, headers=headers, params=params)
        data = json.loads(res.text)
        saveImage(data["results"], keywords)
    except ValueError as e:
        print('Please try later.')

def saveImage(objs, keyword):
    for obj in objs:
        img_link = obj['image']
        img_data = requests.get(img_link).content

        # os.mkdir('downloads')
        filename = "downloads/" + keyword + ".png"
        with open(filename, 'wb+') as f:
            f.write(img_data)

        print("File " + keyword + ".png successfully downloaded.")
        break


while True:
    keyword = input('Enter the search keyword : ')

    search(keyword)
"""





if __name__ == '__main__':
    pass#main = main()
