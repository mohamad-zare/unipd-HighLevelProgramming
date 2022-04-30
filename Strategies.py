######   our 5 strategies   ######

import random


###### Nice guy strategy: He/She always cooperate.
def nice_guy(self):
    return True


###### Bad guy strategy: He/She always defect.
def bad_guy(self):
    return False


###### Mainly bad strategy: He/She defect 75% times. (K is equal to 75 in our case)
def mainly_bad():
    c = random.choices([True, False], [0.25, 0.75])
    return c


###### Mainly nice strategy: He/She cooperate 75% times. (K is equal to 25 in our case)
def mainly_nice():
    c = random.choices([True, False], [0.75, 0.25])
    return c


###### Tit for Tat strategy: He/She starts with cooperating then repeat what the opponent has done in the previous move.
def tit_for_tat(n_rounds, opponent_strategy):   
    if n_rounds == 1:
        c = True
    else:
        c = opponent_strategy
    return c
