"""
This module estimates pi using Monte Carlo methods.
"""

import numpy as np
import matplotlib.pyplot as plt


def estimate_pi(n):
    # Generate n pairs of random points
    points = np.random.rand(n, 2) * 2 - 1

    # Calculate distances
    distances = np.sqrt(points[:, 0]**2 + points[:, 1]**2)

    # Count points inside the unit circle
    inside_circle = np.sum(distances <= 1)

    # Estimate pi
    pi_estimate = 4 * inside_circle / n

    return pi_estimate

# Test with different values of n


test_values = [100, 1000, 10000]
for n in test_values:
    pi_est = estimate_pi(n)
    print(f"n = {n}: π ≈ {pi_est:.6f}")

# Generate data for plotting
n_values = [10, 100, 1000, 10000, 100000, 1000000]
pi_estimates = [estimate_pi(n) for n in n_values]

# Plotting
plt.figure(figsize=(10, 6))
plt.semilogx(n_values, pi_estimates, 'bo-', label='Estimated π')
plt.axhline(y=np.pi, color='r', linestyle='--', label='Actual π')
plt.xlabel('Number of points (n)')
plt.ylabel('Estimated π')
plt.title('Monte Carlo Estimation of π')
plt.legend()
plt.grid(True)
plt.savefig('monte_carlo_pi.png')
plt.show()
