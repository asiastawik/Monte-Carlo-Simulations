import random

num_simulations = 100000
num_successes = 0
num_successes_10 = 0

for i in range(num_simulations):
    rolls_5 = [random.randint(1, 6) for i in range(5)]
    if len(set(rolls_5)) == 5:
        num_successes += 1

    rolls_10 = [random.randint(1, 6) for i in range(10)]
    if len(set(rolls_10)) == 10:
        num_successes_10 += 1

print("Probability of no number appearing twice in 10 rolls:", num_successes_10 / num_simulations)
print("Probability of no number appearing twice in 5 rolls:", num_successes / num_simulations)
