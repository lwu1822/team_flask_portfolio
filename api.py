from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_feedback import *

app_api = Blueprint('api', __name__,
                   url_prefix='/api/feedback')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api)

class JokesAPI:
    # not implemented
    class _Create(Resource):
        def post(self, feedback):
            pass
            
    # getFeedbacks()
    class _Read(Resource):
        def get(self):
            return jsonify(getFeedbacks())

    # getFeedback(id)
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getFeedback(id))

    # getRandomFeedback()
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomFeedback())
    
    # getRandomFeedback()
    class _ReadCount(Resource):
        def get(self):
            count = countFeedback()
            countMsg = {'count': count}
            return jsonify(countMsg)

    # put method: addFeedbackHaHa
    class _UpdateYes(Resource):
        def put(self, id):
            addFeedbackHaHa(id)
            return jsonify(getFeedback(id))

    # put method: addFeedbackBooHoo
    class _UpdateNo(Resource):
        def put(self, id):
            addFeedbackBooHoo(id)
            return jsonify(getFeedback(id))

    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Create, '/create/<string:feedback>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_ReadCount, '/count')
    api.add_resource(_UpdateYes, '/yes/<int:id>')
    api.add_resource(_UpdateNo, '/no/<int:id>')
    
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://teamberries.tk' # run from web
    url = server + "/api/feedback"
    responses = []  # responses list

    # get count of feedback on server
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    # update yes/no test sequence
    num = str(random.randint(0, count-1)) # test a random record
    responses.append(
        requests.get(url+"/"+num)  # read feedback by id
        ) 
    responses.append(
        requests.put(url+"/yes/"+num) # add to yes count
        ) 
    responses.append(
        requests.put(url+"/no/"+num) # add to no count
        ) 

    # obtain a random joke
    responses.append(
        requests.get(url+"/random")  # read a random feedback
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")