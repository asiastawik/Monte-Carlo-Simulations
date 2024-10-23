import random

#TASK 2
num_experiments = 1000000
odd_heads = 0 #l.nieparzysta
three_heads = 0

for i in range(num_experiments):
    tosses = [random.randint(0, 1) for i in range(3)]
    num_heads = sum(tosses)
    if num_heads % 2 == 1:
        odd_heads += 1
        if num_heads == 3:
            three_heads += 1

probability_three_heads = three_heads / odd_heads

print("Probability of three heads given an odd number of heads: {:.2f}%".format(probability_three_heads * 100))

#TASK 3
num_cards = 100
num_trials = 100
total_hits = 0
num_two_hits = 0

for i in range(num_trials):
    cards = list(range(1, num_cards + 1))
    random.shuffle(cards)
    hits = sum([1 for i, card in enumerate(cards) if card == i+1])
    total_hits += hits
    if hits == 2:
        num_two_hits += 1

average_hits = total_hits / num_trials
prob_two_hits = num_two_hits / num_trials

print("Average number of hits:", average_hits)
print("Probability of having exactly two hits:", prob_two_hits)

#TASK 4
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
