import random
import constant
import classifier
from individual import Individual
def crossover(male,female):
    #single point crossover used for reproduction
    crossover_point=random.randrange(constant.d)
    child_features=[]
    child_features.extend(male.features[:crossover_point])
    child_features.extend(female.features[crossover_point:])
    child=Individual(child_features)
    return child