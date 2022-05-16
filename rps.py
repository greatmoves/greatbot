import random

#0 = rock
#1 = paper
#2 = scissors

def res(play):
    i = random.randint(0, 2)
    if play.lower() == "rock":
        play = 0
    elif play.lower() == "paper":
        play = 1
    elif play.lower() == "scissors":
        play = 2
    else:
        return -1

    if i == 0:
        str = "I played rock."
    elif i == 1:
        str = "I played paper."
    elif i == 2:
        str = "I played scissors."
    else:
        str = "Something went wrong."

    if play == 0:
        str+= " And you played rock."
    elif play == 1:
        str+= " And you played paper."
    elif play == 2:
        str+= " And you played scissors"
    else:
        str+= " And something went wrong."

    if play == i:
        str+= " So we tied!"
    elif (i == 0 and play == 1) or (i == 1 and play == 2) or (i == 2 and play == 0):
        str+= " So you won!"
    elif (i == 0 and play == 2) or (i == 1 and play == 0) or (i == 2 and play == 1):
        str += " So I won!"

    return str

