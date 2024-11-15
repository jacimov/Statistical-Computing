import matplotlib.pyplot as plt
from random_walker_module import RandomWalker, ModifiedRandomWalker


def simulate_and_plot(walkers, steps, title, filename):
    """Simulate the walkers and plot their trajectories."""
    plt.figure(figsize=(10, 8))
    colors = ['r', 'g', 'b', 'y']
    # Initialize position lists
    x_positions = [[] for _ in walkers]
    y_positions = [[] for _ in walkers]
    # Record initial positions
    for i, walker in enumerate(walkers):
        x_positions[i].append(walker.get_x_pos())
        y_positions[i].append(walker.get_y_pos())
    # Simulate steps
    for _ in range(steps):
        for i, walker in enumerate(walkers):
            if isinstance(walker, ModifiedRandomWalker):
                walker.step(walkers[:3])  # Pass the other walkers
            else:
                walker.step()
            x_positions[i].append(walker.get_x_pos())
            y_positions[i].append(walker.get_y_pos())

    # Plot trajectories
    for i, walker in enumerate(walkers):
        label = f'Walker {i}' if isinstance(
            walker,
            RandomWalker) else 'Modified Walker'
        plt.plot(x_positions[i], y_positions[i], color=colors[i], label=label)

    plt.title(title)
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.show()
    plt.close()

# Simulation 1: Four RandomWalkers


rw0 = RandomWalker()
rw1 = RandomWalker()
rw2 = RandomWalker()
rw3 = RandomWalker()

walkers_regular = [rw0, rw1, rw2, rw3]
simulate_and_plot(walkers_regular,
                  1000,
                  'Random Walkers - 1000 Steps',
                  'random_walkers.png')

print("First simulation complete. Plot saved as 'random_walkers.png'.")

# Simulation 2: Three RandomWalkers and one ModifiedRandomWalker
rw0 = RandomWalker()
rw1 = RandomWalker()
rw2 = RandomWalker()
mrw = ModifiedRandomWalker()

walkers_mixed = [rw0, rw1, rw2, mrw]
simulate_and_plot(walkers_mixed, 1000,
                  'Mixed Random Walkers - 1000 Steps',
                  'mixed_random_walkers.png')

print("Second simulation complete. Plot saved as 'mixed_random_walkers.png'.")
