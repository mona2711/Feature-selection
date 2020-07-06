import constant
import random
from selector import select_random_features
from classifier import classification_rate
class Individual:

    def __init__(self, features=None):
        if features:
            self.features=features
        else:
            self.features=select_random_features()
        self.update_fitness()

    def update_fitness(self):
        self.fitness=pow(classification_rate(self.features)*constant.scale_fitness,2)

    def remove_random_feature(self):
        index=random.randrange(constant.d)
        del self.features[index]
        self.update_fitness()

    def add_feature(self,feature):
        self.features.append(feature)
        self.update_fitness()

    def get_missing_features(self):
        missing_features=[]
        for feature in range(constant.D):
            if(feature in self.features):
                pass
            else:
                missing_features.append(feature)
        return missing_features 