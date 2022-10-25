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
def initJokes():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    item_id = 0
    for item in feedback_list:
        feedback_data.append({"id": item_id, "feedback": item, "yes": 0, "no": 0})
        item_id += 1
    # prime some haha responses
    for i in range(10):
        id = getRandomJoke()['id']
        addJokeHaHa(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomJoke()['id']
        addJokeBooHoo(id)
        
# Return all jokes from jokes_data
def getJokes():
    return(feedback_data)

# Joke getter
def getJoke(id):
    return(feedback_data[id])

# Return random joke from jokes_data
def getRandomJoke():
    return(random.choice(feedback_data))

# Liked joke
def favoriteJoke():
    best = 0
    bestID = -1
    for joke in getJokes():
        if joke['yes'] > best:
            best = joke['yes']
            bestID = joke['id']
    return feedback_data[bestID]
    
# Jeered joke
def jeeredJoke():
    worst = 0
    worstID = -1
    for joke in getJokes():
        if joke['no'] > worst:
            worst = joke['no']
            worstID = joke['id']
    return feedback_data[worstID]

# Add to haha for requested id
def addJokeHaHa(id):
    feedback_data[id]['yes'] = feedback_data[id]['yes'] + 1
    return feedback_data[id]['yes']

# Add to boohoo for requested id
def addJokeBooHoo(id):
    feedback_data[id]['no'] = feedback_data[id]['no'] + 1
    return feedback_data[id]['no']

# Pretty Print joke
def printJoke(joke):
    print(joke['id'], joke['feedback'], "\n", "yes:", joke['yes'], "\n", "no:", joke['no'], "\n")

# Number of jokes
def countJokes():
    return len(feedback_data)

# Test Joke Model
if __name__ == "__main__": 
    initJokes()  # initialize jokes
    
    # Most likes and most jeered
    best = favoriteJoke()
    print("Most liked", best['yes'])
    printJoke(best)
    worst = jeeredJoke()
    print("Most jeered", worst['no'])
    printJoke(worst)
    
    # Random joke
    print("Random joke")
    printJoke(getRandomJoke())
    
    # Count of Jokes
    print("Jokes Count: " + str(countJokes()))