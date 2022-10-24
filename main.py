# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from api import app_api # Blueprint import api definition
from bp_projects.projects import app_projects # Blueprint directory import projects definition

import requests

app.register_blueprint(app_api) # register api routes
app.register_blueprint(app_projects) # register api routes

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.route('/apitesting/', methods=['GET'])
def apitest(): 
    import requests

    url = "https://dictionary-by-api-ninjas.p.rapidapi.com/v1/dictionary"

    querystring = {"word":"bright"}

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

    return render_template("api.html", word=word, wordDefinition=wordDefinition)


# this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True, port=8056)
