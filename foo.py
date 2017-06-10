# -*- coding: utf-8 -*-
# Pip install the client:
# pip install clarifai
# issue was I named my file clarifai.py
#use python3 & pip3
#'hQQoE0oimPuorCFnkSn82ew8xBr31KI6oyitdO3r', 'OcPC7RzhING8omYUKcXqBcBAfNWGXwfUwqlw2AZi'
import cgi
from clarifai.rest import ClarifaiApp
app = ClarifaiApp()
form = cgi.FieldStorage()
searchterm =  form.getvalue('searchbox')

def search():
    with open('/home/jhilene/Searcher/clarimages.txt') as f:
        # below function creates list of urls and removes new line character
        content = f.read().splitlines()
        return content

def match(x):
    user = input("A url please: ")
    #searches list for match
    for i in x:
        if user == i:
            return user


def team(x):
    result = app.tag_urls(urls=[x])
    # Api is a very nested tree, so I keep indexing to get to target data
    # pprint is best to visualize tree structure in Python terminal
    #Also returns first ten results since API already has highest liklihood sorted first.
    r = result['outputs'][0]['data']['concepts'][:10]
    for result in r:
        #returns name and value
        print (result['name'],result['value'])


content= search()
user = match(content)
team(user)










"""

def read_file():
    with open('/home/jhilene/Searcher/clarimages.txt', 'r') as f:
        for line in f:
            return app.tag_urls()
            #choose randomly

print read_file()
"""
