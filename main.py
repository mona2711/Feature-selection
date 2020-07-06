import constant
from generation import next_generation
from generation import best_individual
from generation import average_fitness
def main():
    prev_gen=None
    average_file = open("average.txt", "a")
    best_file=open("best.txt","a")
    features_file=open("features.txt","a")
    for i in range(constant.num_iterations):
        next_gen=next_generation(prev_gen)
        print("best individual's fitness in "+str(i)+ "th generation : " + str(best_individual(next_gen).fitness))
        best_file.write(str(best_individual(next_gen).fitness)+"\n")
        print(str(best_individual(next_gen).features))
        features_file.write(str(best_individual(next_gen).features)+"\n")
        print("Average generation's fitness "+str(average_fitness(next_gen)))
        average_file.write(str(average_fitness(next_gen))+"\n")
        prev_gen=next_gen
    average_file.close()
    best_file.close()
    features_file.close()
if __name__ == "__main__":
    main()