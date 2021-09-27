import random
import math
from TSPReader import Coordinate
from TSPReader import*

class TabuSearch :

    def __init__( self , MatDist , Coords, max_iteration = 1000) :
        self.max_iteration = max_iteration
        self.MatDist = MatDist
        self.Coords = Coords
        self.initial_solution = None

    #-----ALGORITHM-----

    #1) Individuazione di una soluzione iniziale di innesco del processo di ricerca

    
        self.initial_solution = random.sample(self.Coords , len(self.Coords))

    
    #2) Costruzione intorno

    def get_neighborhood(self , current_solution) :

        return self.two_opt_move(current_solution)

    #DEFINITION OF THE 2-OPT SWAP

    def two_opt_move(self , current_solution) :

        list_of_solution = list()

        for i in range(0, len(current_solution)) :
            for j  in range(i+2, len(current_solution)-2) :
                solution = current_solution.copy()
                solution[i] , solution[j] = solution[j] , solution[i]
                list_of_solution.append(solution)
        
        return list_of_solution

    def two_opt_move_1(self , current_solution) :

        #Randomnly select 2 non-adjacient arch and swap

        neighborhood = current_solution.copy()
        index1 = 0
        index2 = 0

        while ( (index1 == index2) or ( abs(index1 - index2) == 1) ) :

            index1 = random.randint(0 , len(current_solution))
            index2 = random.randint(0 , len(current_solution))
            city1 = current_solution[index1]
            city2 = current_solution[index2]
            print("CITY1 = " , city1 , "INDEX1 = " , index1 , "\n")
            print("CITY2 = " , city2 , "INDEX2 = " , index2 , "\n")

            swap = neighborhood[index1]
            neighborhood[index1] = neighborhood[index2]
            neighborhood[index2] = swap

        return neighborhood

    #DEFINITION OF THE OBJECTIVE FUNCTION
    @staticmethod
    def fitness(current_solution) :

        total_path_lenght = 0

        for i in range(0 , len(current_solution) - 1) :
            distance = Coordinate.distance_2D(current_solution[i] , current_solution[i+1])
            total_path_lenght = total_path_lenght + distance

        total_path_lenght += Coordinate.distance_2D(current_solution[0], current_solution[-1])
        return total_path_lenght
            
    def get_best_candidate(self, neighborhood , tabu_list, current_solution) :

        optSol = current_solution.copy()
        newSol = neighborhood[0]        #could be worse
        for s in neighborhood:
            if (TabuSearch.fitness(s) < TabuSearch.fitness(optSol)) and (s not in tabu_list):   
                optSol = s
            elif TabuSearch.fitness(s) < TabuSearch.fitness(newSol) and (s not in tabu_list):
                newSol = s
            else:
                pass
        if optSol != current_solution:
            return optSol
        else:
            return newSol

    def stop(self, iteration):
        if iteration == self.max_iteration:
            return True
        else:
            return False

    def tabu_search(self) :

        print("TABU SEARCH ALGORITHM....\n\n")

        #1) INIZIALIZZAZIONE: Individuazione di una soluzione di innesco del processo di ricerca
        best_solution = self.initial_solution
        best_candidate = self.initial_solution
        best_fitness = TabuSearch.fitness(best_solution)
        
        #----TABU LIST MECHANISM----
        tabu_list = list()
        tabu_list.append(best_solution)
        
        iteration = 0

        while not self.stop(iteration) :
            print(iteration)
            iteration = iteration + 1

            #2) COSTRUZIONE INTORNO
            my_neighborhood = self.get_neighborhood(best_candidate)
           
           #3) DETERMINAZIONE DI UNA NUOVA SOLUZIONE: Si individua una nuova soluzione appartenente all'intorno... 
            best_candidate = self.get_best_candidate(my_neighborhood, tabu_list, best_candidate)

            #CHECK THE FITNESS

            #3)...che sia migliore della soluzione precedente sulla base di un certo stimatore dopodichè si sostituisce tale soluzione trovata
            #     con la precedente

            if ( TabuSearch.fitness(best_candidate) < TabuSearch.fitness(best_solution)) :
                print("NEW SOLUTION FOUND")
                best_solution = best_candidate                      #sostituzione
                best_fitness = TabuSearch.fitness(best_solution)    #aggiornamento fitness
            else:
                print("NO NEW SOLUTION FOUND")

            #UPDATE TABU LIST
            tabu_list.append(best_candidate)
        
        return best_solution , best_fitness
           
    def gap(self , best_solution , opt_solution) :

        gap = ( abs((opt_solution - best_solution)/(opt_solution)) )*100 
        return gap

            
#TESTING

if __name__=="__main__" :

    test = TSPReader("eil51.tsp" , "eil51.opt.tour.txt")
    test1 = TabuSearch(test.matrixDistance , test.coords, 100)

    #best_solution , best_fitness = test1.tabu_search()
    
    print("\n\n COORDS READ FROM THE TSP FILE : " , test.coords , "\n\n")
    print(" RANDOM INITIAL SOLUTION = " , test1.initial_solution , "\n\n")

    #list_of_solution = test1.two_opt_move(test1.initial_solution)
    #print("TWO OPT MOVE RESULTS : " , list_of_solution , "\n\n")

    neighborhood = test1.get_neighborhood(test1.initial_solution)
    print("NEIGHBORHOOD = " , neighborhood , "\n\n")
    #print("BEST_SOLUTION = " , best_solution , "\n\n")
    #print("BEST_FITNESS = " , best_fitness , "\n\n")
    #print("INIT_FITNESS = " , test1.fitness(test1.initial_solution) , "\n\n")



    
    
