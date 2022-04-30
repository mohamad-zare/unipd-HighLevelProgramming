######   our 5 strategies   ######

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
