from TSPReader import *
from TabuSearch import *
from matplotlib import pyplot as plt
from Plotter import Plotter

if __name__=="__main__" :

    test = TSPReader("eil51.tsp", "eil51.opt.tour.txt")
    test1 = TabuSearch(test.matrixDistance , test.coords, 100)

    test_coordinate = test.coords
    test_matrix = test.matrixDistance
    
    test1_s0 = test1.initial_solution
    print("Random initial solution = " , test1_s0)
    test1_s0.append(test1_s0[0])
    s0, best_fitness = test1.tabu_search()
    plotter = Plotter(s0)
    plotter.plot()

