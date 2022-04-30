# TASK 1	

import random


###### Nice guy strategy: He/She always cooperate.
def nice_guy():
    return True


###### Bad guy strategy: He/She always defect.
def bad_guy():
    return False


###### Mainly bad strategy: He/She defect 75% times. (K is equal to 75 in our case)
def mainly_bad():
    return random.choices([True, False], [0.25, 0.75])[0]


###### Mainly nice strategy: He/She cooperate 75% times. (K is equal to 25 in our case)
def mainly_nice():
    return random.choices([True, False], [0.75, 0.25])[0]


###### Tit for Tat strategy: He/She starts with cooperating then repeat what the opponent has done in the previous move.
def tit_for_tat(n_rounds, strategy2):   
    if n_rounds == 0:
        c = True
    else:
        c = strategy2
    return c


###### calculating the scores
def score(strategy1, strategy2):

    if strategy1 and strategy2:
      return (3, 3)
    elif not strategy1 and strategy2:
      return (5, 0)
    elif strategy1 and not strategy2:
      return (0, 5)
    else:
      return (2, 2)


   ###### a 5 rounds match between a player with "tit for tat" strategy and a player with "mainly bad" strategy
def play_match(strategy1 = tit_for_tat, strategy2 = mainly_bad):

    score1 = 0
    score2 = 0
    n_rounds = 5

    for n in range(n_rounds):
      
      strategy1 = tit_for_tat(n, strategy2)
      strategy2 = mainly_bad()
      scores = score(strategy1, strategy2)
      score1 += scores[0]
      score2 += scores[1]
      print(f"Round {n+1} is over. Scores: {score1, score2}")

    return ("Game is over...")

print(play_match())