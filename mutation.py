import random
import constant
from classifier import classification_rate
def mutate(individual):
    # enforced mutation, as described by the research paper is used
    features=individual.features
    missing_features=individual.missing_features
    # mutation with probability as specified in constant file
    if(random.random()<constant.mutation_prob):
        index=random.randrange(constant.d)
        #deleting by index
        features.del(index)

        index=random.randrange(constant.D-constant.d)
        features.append(missing_features[index])

        individual.mutate(features,classification_rate(features))

    else:
        pass

    return