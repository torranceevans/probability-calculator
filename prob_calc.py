import copy
import random
#Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        contents = []
        ball_count = dict(**kwargs)
        for color in list(ball_count.keys()):
            for _ in range(ball_count[color]):
                contents.append(color)
        
        self.contents = contents

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        
        results = []
        for _ in range(num_balls):
            num = random.randint(0, len(self.contents) -1)
            results.append(self.contents.pop(num))
        
        return results
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    original_hat = copy.copy(hat)
    success = 0
    for _ in range(num_experiments):
        balls = copy.deepcopy(original_hat).draw(num_balls_drawn)
        print(balls)
        for color in list(expected_balls.keys()):
            actual = balls.count(color)
            expected = expected_balls[color]
            if actual < expected:
                break
        else:
            success += 1

    return success / num_experiments