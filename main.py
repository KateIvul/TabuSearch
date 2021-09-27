from TSPReader import *
from TabuSearch import *
from matplotlib import pyplot as plt
from Plotter import Plotter

if __name__=="__main__" :

    #MAIN DI PROVA DATA-SET eil51

    
    #Costruzione oggetti classe TSPReader e TabuSearch
    test_Reader = TSPReader("eil51.tsp" , "eil51.opt.tour.txt")

    #Lista coordinate e matrice delle coordinate
    test_coordinate = test_Reader.coords
    test_matrix = test_Reader.matrixDistance

    n_iteration = 100

    test_TabuSearch = TabuSearch(test_matrix , test_coordinate ,n_iteration)

    test_s0 = test_TabuSearch.initial_solution
    print("Random initial solution = " , test_s0 , "\n\n")
    test_s0.append(test_s0[0])
    s0, best_fitness = test_TabuSearch.tabu_search()
    gap = test_TabuSearch.gap(best_fitness , test_Reader.get_lenght_opt_tour())
    print("\n\n GAP = " , gap , "\n\n")

    #Visualizzazione risultati mediante animazione
    plotter = Plotter(s0)
    plotter.plot()

