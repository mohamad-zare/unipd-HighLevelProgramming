# TASK 1	

from pickle import FALSE
from pickle import TRUE


###### Nice guy strategy which is without processing the opponent's result since he/she always cooperate
class nice_guy():

    def __init__(self):
        pass

    def nice_guy(self):
        return True

    def process_results(self, my_strategy, other_strategy):
        pass


###### Bad guy strategy which is without processing the opponent's result since he/she always defect
class bad_guy():

    def __init__(self):
        pass

    def bad_guy(self):
        return False

    def process_results(self, my_strategy, other_strategy):
        pass


###### calculating the scores
def score(strategy1, strategy2):

    if strategy1 and strategy2:
      return (3, 3)
    elif not strategy1 and strategy2:
      return (5, 0)
    elif strategy1 and not strategy2:
      return (0, 5)
    else:
      return (1, 1)


   ###### Play a 5 rounds match between a Nice guy and a Bad guy
def play_match(prisoner1, prisoner2):

    p1 = prisoner1()
    p2 = prisoner2()

    score1 = 0
    score2 = 0
    n_rounds = 5

    for n in range(n_rounds):
      
      strategy1 = p1.nice_guy()
      strategy2 = p2.bad_guy()
      scores = score(strategy1, strategy2)
      score1 += scores[0]
      score2 += scores[1]
      p1.process_results(strategy1, strategy2)
      p2.process_results(strategy2, strategy1)

    return (f"Game is over...\nThe winner is player two!\nPlayer two is an absolute lashi:D Never cooperated! while player one always cooperated! a naive guy. !!!AVOID THEM BOTH!!!\nSo the first player's score is {score1} and The second player's score is {score2}")

print(play_match(nice_guy, bad_guy))
