import random

def distance(p1, p2):
    return ((p1[0] - p2[0])*(p1[0]-p2[0]) + (p1[1] - p2[1]) * (p1[1] -p2[1]))**(1/2)

def path_distance(path, cities):
    dist = 0
    for i in range(1, len(path)):
        dist += distance(cities[path[i-1]], cities[path[i]])
    return dist

def reproduce(population, cities):
    fitnesses = [1/path_distance(path, cities) for path in population]
    fitness_sum = sum(fitnesses)
    size = len(population)    
    next_population = []
    probability = [fitnesses[0]/fitness_sum]
    for i in range(1, size):
        probability.append(((fitnesses[i]) / fitness_sum) + probability[i-1])
    probability[-1] = 1.0
    for i in range(size):
        chance = random.random()
        j = 0
        while (chance > probability[j]):
            j += 1
        next_population.append(population[j])
    return next_population

def cross(population):
    if len(population) <= 1:
        return population
    pairs = []
    #population = list(population.copy())

    while len(population) > 1:
        r1 = population.pop(random.randrange(0, len(population)))
        r2 = population.pop(random.randrange(0, len(population)))
        pairs.append((r1, r2))
    
    for p1, p2  in pairs:
        const_positions, i, stop, item = [], 0, p1[0], None
        while item != stop:
             const_positions.append(i)
             item = p2[i]
             i = p1.index(item)
        
        population.append(''.join([p1[i] if i in const_positions else p2[i] for i in range(len(p1))]))
        population.append(''.join([p2[i] if i in const_positions else p1[i] for i in range(len(p2))]))

    return population


def mutate(population, mutation_prob=0.01):
    size = len(population)
    cities_length = len(population[0])
    for i in range(size):
        for j in range(cities_length):
            chance = random.random()
            if chance >= 1 - mutation_prob:
                randj = random.randint(0, cities_length -1)
                path = list(population[i])
                path[j], path[randj] = path[randj], path[j]

                population[i] = ''.join(path) 
    return population

def find_path_statistics(population, cities):
    best = (path_distance(population[0], cities), population[0])
    worst = (path_distance(population[0], cities), population[0])
    average = 0
    
    for path in population:
        dist = path_distance(path, cities)
        if dist < best[0]: best = (dist, path)
        if dist > worst[0]: worst = (dist, path)
        average += dist
    average = average / len(population)
    
    return best, average, worst

    
    
