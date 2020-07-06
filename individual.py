import constant
class Individual:
    def __init__(self, features,fitness):
        self.features=features
        self.fitness=fitness

    def mutate(self,features,fitness):
        self.features=features
        self.fitness=fitness

    def get_missing_features(self):
        missing_features=[]
        for i in range(constant.D):
            if(i in self.features):
                pass
            else:
                missing_features.append[i]
        return missing_features