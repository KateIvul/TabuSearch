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

    #2) Creation of the neighborhood 

      



#TESTING

if __name__=="__main__" :

    test = TSPReader(r"C:\Users\Cater\OneDrive\Desktop\UNIVERSITA\RO\ELABORATO 2.0\ISTANZE DI PROVA\eil51.tsp")
    test1 = TabuSearch(test.matrixDistance , test.coords)

    print(test1.initial_solution)
