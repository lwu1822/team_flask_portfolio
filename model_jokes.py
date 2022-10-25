import random

feedback_data = []
feedback_list = [
    "Was this website efficient?",
    "Is the site aesthetically pleasing?",
    "Were you able to find your word?",
    "Are we better than our competitors?",
    "If this project were to be available on the market, would you use it?"
    
]

# Initialize jokes
def initFeedback():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in feedback_list:
        feedback_data.append({"id": item_id, "feedback": item, "yes": 0, "no": 0})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomFeedback()['id']
        addFeedbackHaHa(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomFeedback()['id']
        addFeedbackBooHoo(id)
        
# Return all jokes from jokes_data
def getFeedbacks():
    return(feedback_data)

# Joke getter
def getFeedback(id):
    return(feedback_data[id])

# Return random joke from jokes_data
def getRandomFeedback():
    return(random.choice(feedback_data))

# Liked joke
def favoriteFeedback():
    best = 0
    bestID = -1
    for feedback in getFeedbacks():
        if feedback['yes'] > best:
            best = feedback['yes']
            bestID = feedback['id']
    return feedback_data[bestID]
    
# Jeered joke
def jeeredFeedback():
    worst = 0
    worstID = -1
    for feedback in getFeedbacks():
        if feedback['no'] > worst:
            worst = feedback['no']
            worstID = feedback['id']
    return feedback_data[worstID]

# Add to haha for requested id
def addFeedbackHaHa(id):
    feedback_data[id]['yes'] = feedback_data[id]['yes'] + 1
    return feedback_data[id]['yes']

# Add to boohoo for requested id
def addFeedbackBooHoo(id):
    feedback_data[id]['no'] = feedback_data[id]['no'] + 1
    return feedback_data[id]['no']

# Pretty Print joke
def printFeedback(joke):
    print(joke['id'], joke['feedback'], "\n", "yes:", joke['yes'], "\n", "no:", joke['no'], "\n")

# Number of jokes
def countFeedback():
    return len(feedback_data)

# Test Joke Model
if __name__ == "__main__": 
    initFeedback()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteFeedback()
    print("Most liked", best['yes'])
    printFeedback(best)
    worst = jeeredFeedback()
    print("Most jeered", worst['no'])
    printFeedback(worst)
    
    # Random joke
    print("Random joke")
    printFeedback(getRandomFeedback())
    
    # Count of Jokes
    print("Jokes Count: " + str(countFeedback()))