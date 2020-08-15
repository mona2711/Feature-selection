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
    
    def remove_random_feature(self):
        index=random.randrange(constant.d)
        del self.features[index]

    def add_feature(self,feature):
        self.features.append(feature)

    def get_missing_features(self):
        missing_features=[]
        for feature in range(constant.D):
            if(feature in self.features):
                pass
            else:
                missing_features.append(feature)
        return missing_features