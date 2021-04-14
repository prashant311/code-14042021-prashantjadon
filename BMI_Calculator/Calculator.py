"""
This package is BMI(Body Mass Index) Calculator
Developed by - Prashant Jadon
Date - 14 April 2021
"""


class BMICalculator:

    def __init__(self):
        self.bmi = 0
        self.bmi_cat = ""
        self.risk = ""
        self.data = ""

    def calculator(self, data):
        self.data = data
        for i in self.data:

            # formula of calculating BMI
            self.bmi = round((i["WeightKg"] / ((i["HeightCm"] / 100.00) ** 2)), 2)

            # now we have BMI and find BMI Category and Health Risk
            if self.bmi <= 18.4:
                self.bmi_cat = "Underweight"
                self.risk = "Malnutrition Risk"

            elif self.bmi <= 24.9:
                self.bmi_cat = "Normal weight"
                self.risk = "Low Risk"

            elif self.bmi <= 29.9:
                self.bmi_cat = "Overweight"
                self.risk = "Enhanced Risk"

            elif self.bmi <= 34.9:
                self.bmi_cat = "Moderately obese"
                self.risk = "Medium Risk"

            elif self.bmi <= 39.9:
                self.bmi_cat = "Severely obese"
                self.risk = "High Risk"

            else:
                self.bmi_cat = "Very Severely obese"
                self.risk = " Very High Risk"

            # add three new key and value in dictionary with BMI, BMI Category and Health Risk data of a person.
            i["BMI"] = self.bmi
            i["BMI Category"] = self.bmi_cat
            i["Health Risk "] = self.risk
        return self.data
