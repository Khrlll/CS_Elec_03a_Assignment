import random

# Fitness function
def fitness(x):
    return x * x

# Initialize particles
particles = [random.uniform(-10, 10) for _ in range(5)]
velocities = [0 for _ in range(5)]

personal_best = particles[:]
global_best = min(particles, key=fitness)

for iteration in range(10):
    for i in range(len(particles)):
        # Update velocity
        velocities[i] = (
            0.5 * velocities[i]
            + 0.5 * (personal_best[i] - particles[i])
            + 0.5 * (global_best - particles[i])
        )

        # Update position
        particles[i] += velocities[i]

        # Update personal best
        if fitness(particles[i]) < fitness(personal_best[i]):
            personal_best[i] = particles[i]

    # Update global best
    global_best = min(personal_best, key=fitness)

    print(f"Iteration {iteration}: Best = {global_best:.4f}")

print("Optimal solution:", global_best)