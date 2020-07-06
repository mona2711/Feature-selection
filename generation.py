
import constant
import math
from individual import Individual
from classifer import classification_rate
from selector import select_individual
from crossover import crossover
from mutation import mutate

def next_generation(previous_generation):
    next_generation=[]
    if(previous_generation==None):
        next_generation.fitness=0
        for i in range(constant.mew):
            individual=random_individual()
            next_generation.append(individual)
            next_generation.fitness+=individual.fitness
        return next_generation

    # assuming that the size of population stays same after every generation
    mating_pool=[]
    for i in range(constant.pooling_mate_size):
        mating_pool.append(select_individual(previous_generation))
        # best individuals from previous generation are passed on the next generateion
        next_generation.append(mating_pool[i])

    for i in range(constant.D-constant.pooling_mate_size):
        male=select_individual(previous_generation)
        female=select_individual(previous_generation)
        child=crossover(male,female)
        mutated_child=mutate(child)
        next_generation.append(mutated_child)

    return next_generation

def random_individual():
    all_features=[]
    features=[]
    # for random permutation
    for i in range(constant.D):
        all_features.append(i)
    for i in range(constant.d):
        index=math.floor(random.random()*len(all_features))
        feature=all_features[index]
        individual.append(feature)
        all_features.remove(feature)

    individual=Individual(features,classification_rate(features))
    return individual