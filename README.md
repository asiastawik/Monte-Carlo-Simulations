# Monte Carlo Simulations Project

This project implements several Monte Carlo simulations to estimate probabilities, analyze random processes, and estimate the value of π using geometrical interpretation. Each simulation explores different probability-based problems and compares results with theoretical expectations.

## Project Structure


## Simulations Overview

### 1. Estimating π Using Monte Carlo Method

A simulation based on the geometric probability of random points inside a circle is used to estimate the value of π. The program runs simulations with increasing sample sizes, `N = 10^k` (for `k = 1, 2, ..., 7`), and averages the result 100 times for each `N`. 

The accuracy of the estimate is evaluated by plotting the absolute error `|π - π'|` as a function of `N` in a double-logarithmic scale. A straight-line fit is applied to analyze the relationship between error and sample size.

### 2. Coin Toss Simulation

Simulates tossing a coin three times. The simulation is used to estimate the probability of getting exactly 3 heads when the result is an odd number of heads. The result is compared with the theoretical probability.

### 3. Card Shuffle Simulation

In this simulation, 100 numbered cards are shuffled, and the number of times a card matches its position (a "hit") is recorded. The program estimates the average number of hits and calculates the probability of getting exactly two hits in a shuffle.

### 4. Dice Roll Simulation

Simulates rolling a fair dice 5 and 10 times to estimate the probability that no number appears twice in a set of rolls. The results are compared with the analytical probability for validation.

## Plots & Analysis

For the π estimation simulation, a double-logarithmic plot of the absolute error versus the number of samples is generated to observe how accuracy improves with larger sample sizes.
