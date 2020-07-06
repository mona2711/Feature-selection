import constant
import math
from individual import Individual
from classifier import classification_rate
from selector import select_individual
from crossover import crossover
from mutation import mutate
import random

def next_generation(previous_generation):
    next_generation=[]
    if(previous_generation==None):
        for _ in range(constant.mew):
            individual=Individual()
            #print(str(individual.features)+"  fitness: "+str(individual.fitness))
            next_generation.append(individual)
        return next_generation

    #individuls retained from previous population
    individuals_to_retain=best_individuals(previous_generation,constant.retain_previous)
    for individual in individuals_to_retain:
        #print("retained"+str(individual.features)+"  fitness: "+str(individual.fitness))
        next_generation.append(individual)
     
    #crossover population
    #mating_pool=[]
    #for _ in range(constant.mating_pool_size):
        #to_mate=select_individual(previous_generation)
        #mating_pool.append(to_mate)
        

    for _ in range(constant.mew- constant.retain_previous):
        male=select_individual(previous_generation)
        #print("male selected for mating"+str(male.features)+"  fitness: "+str(male.fitness))
        female=select_individual(previous_generation)
        #print("female selected for mating"+str(female.features)+"  fitness: "+str(female.fitness))
        child=crossover(male,female)
        #print("after crossover"+str(child.features)+"  fitness: "+str(child.fitness))
        mutated_child=mutate(child)
        #print("after mutation"+str(mutated_child.features)+"  fitness: "+str(mutated_child.fitness))
        next_generation.append(mutated_child)
    return next_generation

def best_individual(population):
    fitness=0
    best=None
    for individual in population:
        if individual.fitness>fitness:
            fitness=individual.fitness
            best=individual
    return best

def average_fitness(population):
    fitness=0
    for individual in population:
        fitness+=individual.fitness
    return fitness/len(population)

def best_individuals(initial_population,num):
    population=initial_population.copy()
    best_individuals=[]
    for _ in range(num):
        individual=best_individual(population)
        best_individuals.append(individual)
        population.remove(individual)
    return best_individuals