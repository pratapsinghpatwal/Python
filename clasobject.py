import datetime
virat ={
        'firstname':'virat',
        'lastname':'kohli',
        'birthyear':1988,
        'scores':[]
}

virat['scores'].append(80)
virat['scores'].append(100)
virat['scores'].append(0)

def get_average_score(player) :
    return sum(player['scores'])/len(player['scores'])

def get_age(player):
    now=datetime.datetime.now()
    return now.year - player['birthyear']

age=get_age(virat)
score=get_average_score(virat)
print('The birth score of virate kohali is  ',score)
print('The birth age of virate kohali is  ',age)