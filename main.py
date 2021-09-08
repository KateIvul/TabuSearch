from TSPReader import *
from TabuSearch import *

if __name__=="__main__" :

    test = TSPReader(r"C:\Users\Cater\OneDrive\Desktop\UNIVERSITA\RO\ELABORATO 2.0\ISTANZE DI PROVA\eil51.tsp")
    test1 = TabuSearch(test.matrixDistance , test.coords)

    test_coordinate = test.coords
    test_matrix = test.matrixDistance
    
    test1_s0 = test1.initial_solution
    print("Random initial solution = " , test1_s0)