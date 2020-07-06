# path to training data file
train_data_path = 'isolet1+2+3+4.data'
# path to test data file
test_data_path = 'isolet5.data'
# total number of extracted features
D=617
# size of feature subset (according to research paper)
d=20
# population size (represented by mew in research paper)
mew=10
# number of individuals selected from any generation for mating
#mating_pool_size=5
# number of individuals to retain from previous generation
retain_previous=2
# number of genes changes per mutation
num_features_mutated=1
# number of iterations
num_iterations=10

scale_fitness=1