#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:00:43 2020

@author: chrislovejoy
"""

def calculate_SIRS():
    print('Welcome to the SIRS Criteria Calculator!\n')
    SIRS_score = 0
    
    # TEMPERATURE
    #While True means to keep running the script in the loop until it's finished
    while True:
        temp = input("What is the patient's temperature? ")
        try:
            #Tries to convert the string to a float, and sees if any errors occur (see below) 
            temp = float(temp)
        except ValueError:
            #If an error occurs, then it prompts the user to input a number
            print("You did not enter a number. Please enter a number.")
            continue
        else:
            #break - breaks the loop, saying that it's finished
            break
    
    print("Temperature: ", temp)
    if(temp > 38.0 or temp < 36.0):
        SIRS_score += 1
        print("Points: ", SIRS_score)
    else:
        print("Temperature is normal.")
        print("Points: ", SIRS_score)

    
    # HEART RATE
    while True:
        heartRate = input("What is the patient's heart rate per minute? ")
        try:
            heartRate = int(heartRate)
        except:
            print("You did not enter a number. Please enter an integer.")
            continue
        else:
            break
    
    print("Heart rate: ", heartRate)
    if(heartRate > 90):
        #adds 1 to the points variable
        SIRS_score += 1
        print("Points: ", SIRS_score)
    else:
        print("Heart rate is normal.")
        print("Points: ", SIRS_score)
    
    # RESPIRATORY RATE and PaCO2
    while True:
        respRate = input("What is the patient's respiratory rate per minute? ")
        try:
            respRate = int(respRate)
        except:
            print("You did not enter a number. Please enter an integer.")
            continue
        else:
            break

    print("Respiratory rate: ", respRate)

    while True:
        paCO2 = input("What is the patient's PaCO2 in mmHg? ")
        try:
            paCO2 = float(paCO2)
        except:
            print("You did not enter a number. Please enter a number")
            continue
        else:
            break
    
    print("PaCO2: ", paCO2)
        
    if(respRate > 20 or paCO2 < 32):
        SIRS_score += 1
        print("Points: ", SIRS_score)
    else:
        print("Respiratory rate and PaCO2 are both normal.")
        print("Points: ", SIRS_score)
    
    
    # WHITE CELL COUNT
    while True:
        wbc = input("What is the patient's White Blood Cell count (x10^9/L)?")
        try:
            wbc = int(wbc)
        except:
            print("You did not enter a number. Please enter an integer.")
            continue
        else:
            break
    print("White Blood Cell count: ", wbc, "x10^9/L")
    
    if(wbc > 12 or wbc < 4):
        SIRS_score += 1
        print("Points: ", SIRS_score)
    else:
        print("WBC is normal.")
        print("Points: ", SIRS_score)
    
    # TOTAL SCORE
    print("Total score: ", SIRS_score)
    if(SIRS_score >=2):
        print("The patient has met the criteria for SIRS.")
    else:
        print("Your patient has NOT met the criteria for SIRS.")
    
