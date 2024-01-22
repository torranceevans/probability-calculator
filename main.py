#This entry point file to be used in development. Start by reading README.md
import prob_calc
from unittest import main

prob_calc.random.seed(95)
hat = prob_calc.Hat(blue=4, red=2, green=6)
probability = prob_calc.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)

#Run unit tests automatically
main(module='test_module', exit=False)