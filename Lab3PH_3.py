import random

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
