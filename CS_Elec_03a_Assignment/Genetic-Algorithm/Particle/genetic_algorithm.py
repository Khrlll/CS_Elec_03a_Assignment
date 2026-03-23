import random

# Fitness function
def fitness(x):
    return x * x

# Create initial population
population = [random.randint(0, 31) for _ in range(6)]

for generation in range(10):
    # Sort by fitness (best first)
    population = sorted(population, key=fitness, reverse=True)

    print(f"Generation {generation}: {population}")

    # Select top 2
    parent1, parent2 = population[0], population[1]

    # Crossover (average)
    child = (parent1 + parent2) // 2

    # Mutation (random small change)
    if random.random() < 0.3:
        child += random.randint(-2, 2)

    # Replace worst individual
    population[-1] = child

print("Best solution:", population[0])