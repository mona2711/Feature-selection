import random
import constant
from classifier import classification_rate
def mutate(individual):
    # enforced mutation, as described by the research paper is used
    # mutation with probability as specified in constant file

    for _ in range(constant.num_features_mutated):
        individual.remove_random_feature()
        missing_features=individual.get_missing_features()
        index=random.randrange(len(missing_features))
        individual.add_feature(missing_features[index])

    return individual