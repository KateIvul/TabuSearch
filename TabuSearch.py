import random
import math
from TSPReader import Coordinate
from TSPReader import*

class TabuSearch :

    def __init__( self , MatDist , Coords) :

        self.MatDist = MatDist
        self.Coords = Coords
        self.initial_solution = None

    #-----ALGORITHM-----

    #1) Random initial solution


        self.initial_solution = random.sample(self.Coords , len(self.Coords))

    
    #DEFINITION OF THE 2-OPT SWAP

    def two_opt_move(self , initial_solution) :

        #Randomnly select 2 non-adjacient arch and swap

        neighborhood = self.initial_solution.copy()
        index1 = 0
        index2 = 0

        while ( (index1 == index2) or ( abs(index1 - index2) == 1) ) :

            index1 = random.randint(0 , len(self.initial_solution))
            index2 = random.randint(0 , len(self.initial_solution))
            city1 = self.initial_solution[index1]
            city2 = self.initial_solution[index2]
            print("CITY1 = " , city1 , "INDEX1 = " , index1 , "\n")
            print("CITY2 = " , city2 , "INDEX2 = " , index2 , "\n")

            swap = neighborhood[index1]
            neighborhood[index1] = neighborhood[index2]
            neighborhood[index2] = swap

        return neighborhood

    #DEFINITION OF THE OBJECTIVE FUNCTION

    def fitness(self , initial_solution) :

        total_path_lenght = 0

        for i in range(0 , len(self.initial_solution) - 1) :

            distance = Coordinate.distance_2D(self.initial_solution[i] , self.initial_solution[i+1])
            total_path_lenght = total_path_lenght + distance

        return total_path_lenght
            
    def tabu_search(self , initial_solution) :

        print("TABU SEARCH ALGORITHM....\n\n")

        best_solution = self.initial_solution
        best_candidate = self.initial_solution
        best_fitness = self.fitness(best_solution)
        
        print("BEST SOLUTION = " , best_solution , "\n\n")
        print("BEST FITNESS = " , best_fitness , "\n\n")

        #----TABU LIST MECHANISM----
        tabu_list = list()
        tabu_list.append(best_solution)
        print("TABU LIST = " , tabu_list , "\n\n")

        stopping_criterion = False

        #while  not stopping_criterion :

        #2) Creation of the neighborhood 
        my_neighborhood = self.two_opt_move(best_candidate)
        print("MY NEIGHBORHOOD = " , my_neighborhood)
        best_candidate = my_neighborhood[0]
        print("BEST CANDIDATE = " , best_candidate , "\n\n")

        #SEARCHING A NEW BEST SOLUTION (ITERATE OVER A LIST)
        for new_candidate in my_neighborhood :

            if( new_candidate not in tabu_list) and ( self.fitness(new_candidate) < self.fitness(best_candidate)) :

                #SWAP
                best_candidate = new_candidate

        #CHECK THE FITNESS

        if ( self.fitness(new_candidate) < self.fitness(best_candidate)) :

            best_solution = new_candidate
            best_fitness = self.fitness(best_solution)

        #UPDATE TABU LIST
        tabu_list.append(best_candidate)
        print("UPDATED TABU LIST = " , tabu_list , "\n\n")
        
        return best_solution , best_fitness
           
            








#TESTING

if __name__=="__main__" :

    test = TSPReader(r"C:\Users\Cater\OneDrive\Desktop\UNIVERSITA\RO\ELABORATO 2.0\ISTANZE DI PROVA\eil51.tsp")
    test1 = TabuSearch(test.matrixDistance , test.coords)

    print("INITIAL SOLUTION = " , test1.initial_solution , "\n\n")

    #print("FITNESS = " , test1.fitness())

    #print(len(test1.initial_solution))

    #test1.two_opt_move()
    #print(test1.two_opt_move(test1.initial_solution))
    best_solution = test1.tabu_search(test1.initial_solution)
    best_fitness = test1.tabu_search(test1.initial_solution)
    print("FINAL BEST SOLUTION = " , best_solution , "\n")
    
    
