import copy
import random
from collections import Counter

class Hat:
    def __init__(self, **kwargs):
        self.contents = [
            value
            for value in
            Counter(kwargs).elements()
        ]
    
    def draw(self, num_of_balls):
        removed = []
        if num_of_balls > len(self.contents):
            return self.contents
        
        for removal_step in range(num_of_balls):
            removed_ball = self.contents.pop(int(random.random() * len(self.contents)))
            removed.append(removed_ball)
        
        return removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for experiment in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        
        for color in balls_drawn:
            if color in expected_copy:
                expected_copy[color] -= 1

        if(all(x <= 0 for x in expected_copy.values())):
            count += 1
    return count / num_experiments

random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)