# rosenbrock_driver.py
import numpy as np
import matplotlib.pyplot as plt
from rosenbrock import Optimizer


def main():
    # Setup
    opt = Optimizer()
    # Convert to integers
    ns = [int(n) for n in range(100, 2100, 100)]

    # Store
    fast_times = []
    slow_times = []
    dists = []
    mins = []

    # Get minimum
    true_x, true_y = opt.min_point()

    # Run optimization
    for n in ns:
        print(f"Grid size n={n}...")

        # Fast
        t1, min1, x1, y1 = opt.run_fast(n)
        fast_times.append(t1)

        # Slow
        t2, min2, x2, y2 = opt.run_slow(n)
        slow_times.append(t2)

        # Save results
        mins.append(min1)
        dist = np.sqrt((x1 - true_x)**2 + (y1 - true_y)**2)
        dists.append(dist)

    # Plot Time
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(ns, fast_times, 'b-', label='Fast')
    plt.plot(ns, slow_times, 'r-', label='Slow')
    plt.xlabel('Grid size (n)')
    plt.ylabel('Time (s)')
    plt.title('Time vs Grid Size')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(ns, np.array(slow_times)/np.array(fast_times), 'g-')
    plt.xlabel('Grid size (n)')
    plt.ylabel('Slow/Fast ratio')
    plt.title('Speed Ratio')

    plt.tight_layout()
    plt.savefig('timing.png')

    # Plot
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(ns, dists, 'b-')
    plt.xlabel('Grid size (n)')
    plt.ylabel('Distance to true min')
    plt.title('Accuracy vs Grid Size')

    plt.subplot(1, 2, 2)
    plt.plot(ns, mins, 'r-')
    plt.xlabel('Grid size (n)')
    plt.ylabel('Min value found')
    plt.title('Minimum vs Grid Size')

    plt.tight_layout()
    plt.savefig('accuracy.png')

    # Find accuracy < 0.05
    good_n = np.where(np.array(dists) < 0.05)[0]
    if len(good_n) > 0:
        n_needed = ns[good_n[0]]
        print(f"\nNeed n={n_needed} for <0.05 distance")
        print(
            f"Time difference:"
            f"{slow_times[good_n[0]] - fast_times[good_n[0]]:.3f}s"
            )


if __name__ == "__main__":
    main()
