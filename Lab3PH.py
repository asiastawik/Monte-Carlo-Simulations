import random
import matplotlib.pyplot as plt
import numpy as np

#TASK1 1
def estimate_pi(N):
    count = 0
    for i in range(N):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            count += 1
    return 4 * count / N

N_range = [10**k for k in range(1,8)]
estimates = []

for N in N_range:
    pi_estimates = []
    for i in range(100):
        pi_estimate = estimate_pi(N)
        #print(pi_estimate)
        pi_estimates.append(pi_estimate)
        pi = np.pi
        errors = [abs(pi_est - pi) for pi_est in pi_estimates]

    estimates.append(np.mean(errors))

print(N_range)
print(estimates)
plt.loglog(N_range, estimates)
plt.xlabel('N')
plt.ylabel('|pi - pi_est|')
plt.title('Error in Monte Carlo estimation of pi')
plt.show()