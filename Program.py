import sys
from BMI import *

def main(argv):
    cont = True
    while (cont):
        Weight = input("Please input your weight in kilogram: ")
        Height = input ("Please input your height in meter: ")
        #print(int(Weight), float(Height))
        bmi = BodyMassIndex(float(Weight), float(Height))
        bmi.Result()
        cont = (input("One more (y/n)?") == "y")

if __name__ == "__main__":
    main(sys.argv[1:])