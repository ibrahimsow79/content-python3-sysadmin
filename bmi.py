#!/usr/bin/env python3.8

# BMI = (Weight in kg / height in meters squared)
# Imperail version: BMI * 703

def gather_info():
    height = float (input("What is your height ? "))
    weight = float (input("What is your weight ? "))
    system = input("Are your measurement in metric or imperial units ? ").lower().strip()
    return (height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    """
    Return the Body Mass  Index (BMI) for 
    the given weight, height and measurment system.
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while  True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calculate_bmi(weight,system=system,height=height)
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = calculate_bmi(weight,height)
        print(f"Your BMI is{bmi} ")
        break
    else:
        print("Error: Uknown measurement system. Please use imperial or metric")