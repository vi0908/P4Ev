import copy

import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **balls):
        
        self.balls = balls
        self.contents = []
        self.contents_copy = copy.deepcopy(self.contents)

        for b, c in balls.items():
           count = 0
           while count < c:
               self.contents.append(b)
               count += 1


    def draw(self, number):

        if number < len(self.contents):
            draw_balls = []
            for x in range (number):
                draw_balls.append(self.contents.pop(random.randrange(len(self.contents))))
            return draw_balls

        else:
            return self.contents





def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    copy_contents = copy.deepcopy(hat.contents)
    expected_list = []

    for b, c in expected_balls.items():
           count = 0
           while count < c:
               expected_list.append(b)
               count += 1

    expected_copy = copy.deepcopy(expected_list)

    for experiment in range(num_experiments):

        draw_ball = hat.draw(num_balls_drawn)

        hat.contents = copy.deepcopy(copy_contents)

        expected_list = copy.deepcopy(expected_copy)

        for color_obtained in draw_ball:
            if color_obtained in expected_list:
                expected_list.remove(color_obtained)
            
        if expected_list == []:
            M+=1
            

    probability = M / num_experiments

    return probability
        
hat = Hat(blue=3,red=2,green=6)
print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments = 1000))

#https://replit.com/@EyckVanJan/probability-calculator?v=1




