from geometry import *


a = input("Choose oprration: 1 - square of round \n"
        "2 - square of area\n 3 - square of triangle\n"
        "4 - vol of sphere\n 5 - vol of conus\n"
        "6 - vol of cube\n 7 - vol of parallepiped"
        "8 - for exit\n")
if a == 1:
    r = input("Enter radius: ")
    print(geometry.square_round(r))
    #elif a == 2:



