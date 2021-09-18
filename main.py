from TSPReader import *
from TabuSearch import *

if __name__=="__main__" :

    #test = TSPReader(r"C:\Users\Cater\OneDrive\Desktop\UNIVERSITA\RO\ELABORATO 2.0\ISTANZE DI PROVA\eil51.tsp")
    #test1 = TabuSearch(test.matrixDistance , test.coords)
    test_Reader = TSPReader("eil51.tsp" , "eil51.opt.tour.txt")
    test_TabuSearch = TabuSearch(test_Reader.matrixDistance , test_Reader.coords)

    test_coordinate = test_Reader.coords
    test_matrix = test_Reader.matrixDistance
    
    test1_s0 = test_TabuSearch.initial_solution
    print("Random initial solution = " , test1_s0 , "\n")