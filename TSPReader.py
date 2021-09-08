from os import name
import numpy as np
import pandas as pd
import math

from numpy.core.defchararray import index

class TSPReader :

    #open , read and extract information from the tsp file

    def __init__(self , file) :
        
        self.file = file
        self.name = ""
        self.type = ""
        self.dimension = 0
        self.matrixDistance = None
        self.coords = list()

       #OPENING THE FILE

        with open(file) as tspfile :        #with open(...) as ... automatically close the file "

            lines = tspfile.readlines()       #readlines() – read all the lines of the text file and return them as a list of strings.

          #PARSING THE FILE I

            self.name = lines[0][6:]     
            self.type = lines[2][6:]     
            self.dimension = lines[3][11:]

          #PARSING THE FILE II

            for i,value in enumerate(lines[6: -1]) :                              #from line 6 to the EOF...

                linesplit = value.split()     #split() -split a string into a list where each word is a list item, in this case: 3 items

                self.coords.append(Coordinate(int(linesplit[1]) ,int(linesplit[2]) ))   

            #DISTANCE MATRIX

            self.matrixDistance = TSPReader.distance_total_2D(self.coords)

            #2D TOTAL DISTANCE (UTILITY FUNCTION)

    @staticmethod
    def distance_total_2D(coords) :

        #PRE-ALLOCATION TEMP MATRIX

        matrixTemp = np.zeros( (int(len(coords)) , int( len(coords)) ) )                # (51 x 51)

        #COMPUTING TOTAL DISTANCE

        for i in range( 0 , len(coords)) :

            for j in range( 0 , len(coords) ) :

                matrixTemp[i][j] = Coordinate.distance_2D(coords[i] ,coords[j] )

        return matrixTemp

    def get_name(self) :

        return self.name

    def get_dimension(self) :

        return self.dimension

    def get_type(self) :

        return self.type


class Coordinate :

    def __init__(self , x , y) :

        self.x = x
        self.y = y
    
    #2D DISTANCE

    @staticmethod
    def distance_2D( coord1 , coord2) :

        distance = math.sqrt( (coord1.x - coord2.x)**2 + (coord1.y - coord2.y)**2 )

        return distance

    def __str__(self) -> str:
        
        return "[{},{}]".format(self.x, self.y)
    
    def __repr__(self) -> str:
        return str(self)
#TESTING

if __name__=="__main__" :

    print("Demo TSPReader class...\n")
    test = TSPReader(r"C:\Users\Cater\OneDrive\Desktop\UNIVERSITA\RO\ELABORATO 2.0\ISTANZE DI PROVA\eil51.tsp")

    print("Computing...\n")

    problem_name = test.get_name()
    problem_dimension = test.get_dimension()
    problem_type = test.get_type()
    test_coord = test.coords
    print("COORDS = " ,  test_coord)


    #print("PROBLEM NAME = " , problem_name , "\n")
    #print("PROBLEM DIMENSION = " , problem_dimension , "\n")
    #print("PROBLEM TYPE = " , problem_type , "\n\n")

    #ARRAY CHECK
    #print("X COORDINATE : \n" , x_coordinate , "\n" )
    #print("Y COORDINATE : \n" , y_coordinate , "\n" )

    #print(x_coordinate[3] , "\n")
    #print(y_coordinate[1] , "\n")

    #ARRAY DIMENSION
    #print("ARRAY X DIMENSION : " , len(x_coordinate) , "\n")
    #print("ARRAY Y DIMENSION : " , len(y_coordinate) , "\n")
    #print("\n\n")

    #print("DEMO Coordinates class...\n")
    #test_coord = Coordinates( x_coordinate , y_coordinate)
    print("DISTANCE MATRIX : \n" , test.matrixDistance)
    


