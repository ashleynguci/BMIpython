import sys

class BodyMassIndex(object):
        """docstring for BodyMassIndex"""
        def __init__(self, Weight, Height):
            self.Weight = Weight
            self.Height = Height

        def CountingBMI(self, Weight, Height):
            bmi = (Weight / (Height * Height))
            return round(bmi,2)
            
        def Result(self):
            
            newBMI = self.CountingBMI(self.Weight, self.Height)
            #print(str(newBMI))
            if (newBMI < 16.0):
                print("Hi, your BMI index is " + str(newBMI) + " and you are severe underweight");
            
            elif (newBMI >= 16.0 and newBMI <= 16.99):
                print("Hi, your BMI index is " + str(newBMI) + " and you are underweight");
            
            elif (newBMI >= 17 and newBMI <= 18.49):
                print("Hi, your BMI index is " + str(newBMI) + " and you are mild underweight");
            
            elif (newBMI >= 18.5 and newBMI <= 24.99):
                print("Hi, your BMI index is " + str(newBMI) + " and you are normal");
            
            elif (newBMI >= 25 and newBMI <= 29.99):
                print("Hi, your BMI index is " + str(newBMI) + " and you are mild overweight");
            
            elif (newBMI >= 30.0 and newBMI <= 34.99):
                print("Hi, your BMI index is " + str(newBMI) + " and you are overweight");
            
            elif (newBMI >= 35.0 and newBMI <= 39.99):
                print("Hi, your BMI index is " + str(newBMI) + " and you are severe overweight");
            
            elif (newBMI >= 40.0):
                print("Hi, your BMI index is " + str(newBMI) + " and you are severe obesity");



