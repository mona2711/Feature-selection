import classifier
import random
import constant
import math

def select_individual(generation):
    wheel_partitions,circumference=make_wheel(generation)
    individual_selected=rotate_wheel(wheel_partitions,circumference)
    return generation[individual_selected]

def rotate_wheel(wheel_partitions,circumference):
    stop_point=random.random()*circumference
    #print("stop"+str(stop_point))
    circumference_covered=0
    for partition in range(len(wheel_partitions)):
        circumference_covered+=wheel_partitions[partition]
        if(stop_point<=circumference_covered):
            return partition
    return None

def make_wheel(generation):
    wheel_partitions=[]
    circumference=0
    for individual in generation:
        wheel_partitions.append(individual.fitness)
        circumference+=individual.fitness
    return wheel_partitions,circumference

def select_random_features():
    all_features=[]
    features=[]
    # for random permutation
    for i in range(constant.D):
        all_features.append(i)

    for i in range(constant.d):
        index=math.floor(random.random()*len(all_features))
        feature=all_features[index]
        features.append(feature)
        all_features.remove(feature)

    return features 