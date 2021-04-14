"""
This is a Runner of BMI calculator package.
Developed by - Prashant Jadon
Date - 14 April 2021
"""

from BMI_Calculator.Calculator import BMICalculator
import json
import os
import defaultData


class Runner(BMICalculator):

    def __init__(self):
        super().__init__()
        self.data = ""

    def runner(self, input_option):
        if input_option is "1":
            self.data = defaultData.default_dta
        elif input_option is "2":
            file_name = input("Please Enter file name with path")
            file = open(os.path.abspath(file_name))
            self.data = json.load(file)
        else:
            print("You Enter Invalid Option. Please Rerun App")
        result = self.calculator(self.data)
        file = open("NewData.json", "w")
        file.write(str(result))
        file.close()
        print("Data stored in NewData.json file")


if __name__ == '__main__':
    obj = Runner()
    print("Choose one Option for entering data")
    option = input("1. Go with Default Data \n2. Enter JSON file name with path\n")
    obj.runner(option)




