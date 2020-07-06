import classifier
import random

def select_individual(generation):
    wheel=make_wheel(generation)
    individual_selected=rotate_wheel(wheel)
    return generation[individual_selected]

def rotate_wheel(wheel):
    stop_point=random.randrange(wheel.circumference)
    wheel_covered=0
    final_partition=0
    for i in range(wheel.partitions):
        # adding partition of a wheel
        wheel_covered+=wheel[i]
        if(stop_point<=wheel_covered):
            final_partition=i
            break
    return final_partition

def make_wheel(generation):
    wheel=[]
    for individual in generation:
        wheel.append(individual.fitness)
    wheel.circumference=generation.fitness
    wheel.partitions=len(generation)
    return wheel