# West_lab6
# 25 / Apr 2022

def bmi_intro():
    print("Welcome to my BMI calculator!")
    print("If you can tell me your weight and height")
    print("I can tell you your Body Mass Index")
    print("Let's Go!\n")

def main():
    bmi_intro()    
    get_height = 0.0
    get_weight = 0.0
    body_mass_index = 0.0
    get_height = float(input("Please enter your height in meters. "))
    get_weight = float(input("Please enter your weight in kilograms. "))
    body_mass_index = (get_weight) / (get_height ** 2)
    if body_mass_index < 18.5:
        print("A person with a BMI of " + str(body_mass_index ) + " is underwieght ")
    elif body_mass_index < 24.9:
        print("A person with a BMI of " + str(body_mass_index ) + " is healthy weight ")
    else:
        print("A person with a BMI of " + str(body_mass_index ) + " is overweight ")

main()