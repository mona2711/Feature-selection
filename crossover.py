import random
import constant
import classifier
def crossover(male,female):
    #single point crossover used for reproduction
    crossover_point=random.randrange(constant.d)
    child_features=[]
    child_features.append(male.features[:crossover_point])
    child_features.append(female.features[crossover_point:])
    child=Individual(child_features,classifier.classification_rate(child_features))
    return child