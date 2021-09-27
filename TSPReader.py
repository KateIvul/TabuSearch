from os import name
import numpy as np
import re
import math

from numpy.core.defchararray import index

class TSPReader :

    #open , read and extract information from the tsp file and the opt file

    def __init__(self , file , file_opt) :
        
        self.file = file
        self.file_opt = file_opt
        self.name = ""
        self.type = ""
        self.dimension = 0
        self.lenght_opt_tour = 0
        self.matrixDistance = None
        self.coords = list()
        self.opt_tour = list()
        self.opt_coords = list()

       #OPEN THE FILE

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

        #OPEN THE OPT FILE
        with open(file_opt) as tsp_opt_file :

            lines = tsp_opt_file.readlines()       #readlines() – read all the lines of the text file and return them as a list of strings.

          #PARSING THE FILE I

            self.name = lines[0][6:]   
            #self.lenght_opt_tour = int(lines[1][39:42])  #use regex
            self.lenght_opt_tour = int(re.search(".*\((\d+)\)",lines[1]).group(1))  #use regex
            self.type = lines[2][6:]     
            self.dimension = lines[3][11:]

          #PARSING THE FILE II

            for i,value in enumerate(lines[5: -1]) :                              #from line 5 to the EOF...

                 self.opt_tour.append(int(value))

            for tour in self.opt_tour :
                
                self.opt_coords.append(self.coords[tour-1])


            
    #2D TOTAL DISTANCE (UTILITY FUNCTION)

    @staticmethod
    def distance_total_2D(coords) :

        #PRE-ALLOCATION TEMP MATRIX

        matrixTemp = np.zeros( (int(len(coords)) , int( len(coords)) ) )                

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

    def get_lenght_opt_tour(self) :

        return self.lenght_opt_tour


class Coordinate :

    def __init__(self , x , y) :

        self.x = x
        self.y = y
    
    #2D DISTANCE

    @staticmethod
    def distance_2D( coord1 , coord2) :

        distance = math.sqrt( (coord1.x - coord2.x)**2 + (coord1.y - coord2.y)**2 )

        return distance

    def __str__(self) -> str:       #represent the class objects as a string to simplify visualization
        
        return "[{},{}]".format(self.x, self.y)
    
    def __repr__(self) -> str:      #represent the class objects as a string
        return str(self)

    def __eq__(self, o: object) -> bool:           #overloading operator "=="
        if isinstance(o, Coordinate):
            return self.x == o.x and self.y == o.y
        else:
            return False

#TESTING

if __name__=="__main__" :

    print("Demo TSPReader class...\n")
    #test = TSPReader(r"C:\Users\Cater\OneDrive\Desktop\UNIVERSITA\RO\ELABORATO 2.0\ISTANZE DI PROVA\eil51.tsp")
    test = TSPReader("eil51.tsp" , "eil51.opt.tour.txt")        #path locale

    print("Computing...\n")

    problem_name = test.get_name()
    problem_dimension = test.get_dimension()
    problem_type = test.get_type()
    test_coord = test.coords
    print("PROBLEM NAME = " , problem_name , "\n")
    print("PROBLEM DIMENSION = " , problem_dimension , "\n")
    print("COORDS = " ,  test_coord , "\n")

    opt_name = test.get_name()
    opt_dimension = test.get_dimension()
    opt_type = test.get_type()
    opt_lenght = test.get_lenght_opt_tour()
    opt_coords = test.opt_coords

    print("OPT NAME = " , opt_name , "\n")
    print("OPT DIMENSION = " , opt_dimension , "\n")
    print("OPT TYPE = " , opt_type , "\n")
    print("OPT LENGHT = " , opt_lenght , "\n")
    print("OPT TOUR =  " , opt_coords)

    #print("DEMO Coordinates class...\n")
    #test_coord = Coordinates( x_coordinate , y_coordinate)
    #print("DISTANCE MATRIX : \n" , test.matrixDistance)

    l1 = [Coordinate(1,2), Coordinate(2,1)]
    l2 = [Coordinate(1,2), Coordinate(2,1)]
    print(l1==l2)
    


