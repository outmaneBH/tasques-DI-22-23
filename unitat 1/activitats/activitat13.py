from math import fabs
import random

rand =random.randint(0, 100)
done=False

import sys

while done==False:
    try:
        num=int(input('Write a number to start the game : '))
        if num > rand:   
            raise ValueError(str(num)+ "  ErrorEnterMassaGran !")
        elif num == rand:
            done=True
            print("Your input : ",num," and Random number :",rand," are equals 👌🎉")
        else:
            raise ValueError(str(num)+ "  ErrorEnterMassaMenut !")
    
    except ValueError as ve:
        print("Excepció capturada:", ve)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise