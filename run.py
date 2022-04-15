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

print(getAnswerNum)

def getHints(guess, answerNum):
    """Returns a string of hints with Hot, Warm, Cold"""
    if guess == answerNum:
        return "Correct! Right on the money!"

    hints = []
    for i in range(len(guess)):
        if guess[i] == answerNum[i]:
            hints.append("Hot")
        elif guess[i] in answerNum:
            hints.append("Warm")
    if len(hints) == 0:
                return "Cold"

    hints.sort()
    return " ".join(hints)

print(getHints)
 

def dataTypeNums(num):
    if num == "":
        return False   

    for i in num:
        if i not in "0, 1, 2, 3, 4, 5, 6, 7, 8, 9".split():
            return False

    return True    

print("The number I am thinking of has 3 digits. Can you guess what the number is?")
print("Here are the hints that I will give...")
print("When you see:    It means:")
print("Cold            None of the digits are correct")
print("Warm            One digit is correct but not in the right place")
print("Hot             One digit is correct and in the right place")