import random
"""3 digits long and limits number of guesses"""

NUM_DIGITS = 3
MAX_GUESS = 10

def getAnswerNum():
    """Returns the random unique digit numbers that are the answer"""
    number = list(range(10))
    random.shuffle(number)
    answerNum = ""
    for i in range(NUM_DIGITS):
        answerNum += str(number[i])
    return answerNum    

print(answerNum)
