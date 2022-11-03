# import "packages" from flask
from random import Random
from flask import Flask, render_template, request, Response, redirect, url_for  # import render_template from "public" flask libraries
# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from api import app_api # Blueprint import api definition
from bp_projects.projects import app_projects # Blueprint directory import projects definition
#from random_word import RandomWords
import json
import random
import time
import itertools
from datetime import datetime


import requests

app.register_blueprint(app_api) # register api routes
app.register_blueprint(app_projects) # register api routes



@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    if request.headers.get('accept') == 'text/event-stream':
        def events():            
                
            for i, c in enumerate(itertools.cycle('abc')):
                ranWord = open('words.txt').read().splitlines()
                
                if time.strftime("%H:%M:%S") == "00:00:00":
                    wordOfTheDay = random.choice(ranWord)
                    print(wordOfTheDay)
                    
                    with open('actualWordOfTheDay.txt', 'w') as f:
                        pass
                    with open('actualWordOfTheDay.txt', 'a') as f:
                        f.write(wordOfTheDay)

             
    
                
                #yield "data: %s %d\n\n" % (wordOfTheDayPrinted)
              
                
                    
        return Response(events(), content_type='text/event-stream')
    wordOfTheDayFile = open('actualWordOfTheDay.txt')
    wordOfTheDayPInFile = wordOfTheDayFile.readlines()
    wordOfTheDayPrinted = wordOfTheDayPInFile[0]
    
    url = "https://dictionary-by-api-ninjas.p.rapidapi.com/v1/dictionary"

    querystring = {"word":wordOfTheDayPrinted}

    headers = {
        "X-RapidAPI-Key": "cc6d770f58msh120c53d95d27c68p1d2955jsn1898ff4fa031",
        "X-RapidAPI-Host": "dictionary-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    wordDefinition = response.json().get('definition')
    word = response.json().get('word')

    print("Word: ")
    print(word)
    print()
    print("Definition: ")
    print(wordDefinition)
    
    newDef = json.dumps(wordDefinition)
    
    for ele in newDef:
        if ele.isdigit():
            newDef = newDef.replace(ele, '\n')
    print(newDef)
    

    newDef = newDef.split('\n')
    
    return render_template("index.html", wordOfTheDayPrinted=wordOfTheDayPrinted, newDef=newDef)
    
    
        
    
    


@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.route('/dictionaryInput/')  
def dictionaryInput():
    return render_template("dictionaryInput.html")



@app.route('/apitesting/', methods=['GET', 'POST'])
def apitest(): 
    import requests
    
    inputWord = request.form.get("inputWord")

    url = "https://dictionary-by-api-ninjas.p.rapidapi.com/v1/dictionary"

    querystring = {"word":inputWord}

    headers = {
        "X-RapidAPI-Key": "cc6d770f58msh120c53d95d27c68p1d2955jsn1898ff4fa031",
        "X-RapidAPI-Host": "dictionary-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    wordDefinition = response.json().get('definition')
    word = response.json().get('word')

    print("Word: ")
    print(word)
    print()
    print("Definition: ")
    print(wordDefinition)
    
    newDef = json.dumps(wordDefinition)
    
    for ele in newDef:
        if ele.isdigit():
            newDef = newDef.replace(ele, '\n')
    print(newDef)

    newDef = newDef.split('\n')

   
    
    return render_template("api.html", word=word, wordDefinition=wordDefinition, newDef=newDef)


# this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
