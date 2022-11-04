import random

feedback_data = []
feedback_list = [
    "Was this website efficient?",
    "Is the site aesthetically pleasing?",
    "Were you able to find your word?",
    "Are we better than our competitors?",
    "If this project were to be available on the market, would you use it?"
    
]

# Initialize feedback
def initFeedback():
    # setup feedback into a dictionary with id, feedback, yes, no
    item_id = 0
    for item in feedback_list:
        feedback_data.append({"id": item_id, "feedback": item, "yes": 0, "no": 0})
        item_id += 1
    """
    # prime some haha responses
    for i in range(10):
        id = getRandomFeedback()['id']
        addFeedbackHaHa(id)
    # prime some haha responses
    for i in range(5):
        id = getRandomFeedback()['id']
        addFeedbackBooHoo(id)
    """
        
# Return all feedback from feedback_data
def getFeedbacks():
    return(feedback_data)

# Feedback getter
def getFeedback(id):
    return(feedback_data[id])

# Return random feedback from feedback_data
def getRandomFeedback():
    return(random.choice(feedback_data))

# Yes feedback
def favoriteFeedback():
    best = 0
    bestID = -1
    for feedback in getFeedbacks():
        if feedback['yes'] > best:
            best = feedback['yes']
            bestID = feedback['id']
    return feedback_data[bestID]
    
# No feedback
def jeeredFeedback():
    worst = 0
    worstID = -1
    for feedback in getFeedbacks():
        if feedback['no'] > worst:
            worst = feedback['no']
            worstID = feedback['id']
    return feedback_data[worstID]

# Add to yes for requested id
def addFeedbackHaHa(id):
    #feedback_data[id]['yes'] = 0
    
    feedback_data[id]['yes'] = feedback_data[id]['yes'] + 1
    return feedback_data[id]['yes']

# Add to no for requested id
def addFeedbackBooHoo(id):
    #feedback_data[id]['no'] = 0
    
    feedback_data[id]['no'] = feedback_data[id]['no'] + 1
    return feedback_data[id]['no']

# Pretty Print feedback
def printFeedback(feedback):
    print(feedback['id'], feedback['feedback'], "\n", "yes:", feedback['yes'], "\n", "no:", feedback['no'], "\n")

# Number of feedback
def countFeedback():
    return len(feedback_data)

# Test Feedback Model
if __name__ == "__main__": 
    initFeedback()  # initialize feedback
    
    # Most yes and most no
    best = favoriteFeedback()
    print("Most yes", best['yes'])
    printFeedback(best)
    worst = jeeredFeedback()
    print("Most no", worst['no'])
    printFeedback(worst)
    
    # Random feedback
    print("Random feedback")
    printFeedback(getRandomFeedback())
    
    # Count of Feedback
    print("Feedbacks Count: " + str(countFeedback()))