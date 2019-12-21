# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 10:26:46 2019

@author: USER
"""
#Stone Paper Scissors script in Python.

import random
import sys
 
if __name__ == "__main__":
    turn = 0    #To count the number of turns of the game.
    machine_score = 0
    user_score = 0
    
    while(1):
        print('''\n\nWinning Rules of the stone paper scissors game are as follows: \n
                          stone vs paper -> paper wins \n
                          stone vs scissors -> stone wins \n
                          paper vs scissors -> scissors wins \n''') 
        print('''
        
        Enter your choice:\n

        1. Stone
        2. Paper
        3. Scissors
        
              ''')
        user_guess = int(input())       
        machine_guess = random.randint(1,3)
        
        if(user_guess == 1 or user_guess == 2 or user_guess == 3):
            if(user_guess == 1):
                if(machine_guess == 1):
                    machine_score += 0
                    user_score += 0
                    turn+=1
                    print("Machine Guess: stone")
                    print("User's Score: ",user_score)
                    print("Machine's Score: ",machine_score)
                    print("Turn: ",turn)
                        
                elif(machine_guess == 2):
                    machine_score += 1
                    user_score += 0
                    turn+=1
                    print("Machine Guess: paper")
                    print("User's Score: ",user_score)
                    print("Machine's Score: ",machine_score)
                    print("Turn: ",turn)
                
                elif(machine_guess == 3):
                    machine_score += 0
                    user_score += 1
                    turn+=1
                    print("Machine Guess: scissors")
                    print("User's Score: ",user_score)
                    print("Machine's Score: ",machine_score)
                    print("Turn: ",turn)
                    
            elif(user_guess == 2):
                if(machine_guess == 1):
                    machine_score += 0
                    user_score += 0
                    turn+=1
                    print("Machine Guess: stone")
                    print("User's Score: ",user_score)
                    print("Machine's Score: ",machine_score)
                    print("Turn: ",turn)
                        
                elif(machine_guess == 2):
                    machine_score += 1
                    user_score += 0
                    turn+=1
                    print("Machine Guess: paper")
                    print("User's Score: ",user_score)
                    print("Machine's Score: ",machine_score)
                    print("Turn: ",turn)
                
                elif(machine_guess == 3):
                    machine_score += 0
                    user_score += 1
                    turn+=1
                    print("Machine Guess: scissors")
                    print("User's Score: ",user_score)
                    print("Machine's Score: ",machine_score)
                    print("Turn: ",turn)
                
            elif(user_guess == 3):
                if(machine_guess == 1):
                    machine_score += 0
                    user_score += 0
                    turn+=1
                    print("Machine Guess: stone")
                    print("User's Score: ",user_score)
                    print("Machine's Score: ",machine_score)
                    print("Turn: ",turn)
                        
                elif(machine_guess == 2):
                    machine_score += 1
                    user_score += 0
                    turn+=1
                    print("Machine Guess: paper")
                    print("User's Score: ",user_score)
                    print("Machine's Score: ",machine_score)
                    print("Turn: ",turn)
                
                elif(machine_guess == 3):
                    machine_score += 0
                    user_score += 1
                    turn+=1
                    print("Machine Guess: scissors")
                    print("User's Score: ",user_score)
                    print("Machine's Score: ",machine_score)
                    print("Turn: ",turn)
            
        else:
            while(1):
                print("\nYou have entered an invalid option.\nDo you want to quit?\n\nPress 1 to quit.\nPress 2 to continue playing.")
                x = int(input())
                if(x == 1):
                    sys.exit()
                elif(x == 2):
                    break
                elif(x != 1 or x != 2):
                    print("Invalid input. Please enter again.")
                    