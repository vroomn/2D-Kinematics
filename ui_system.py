import pygame

# Holds UI system functions, purely aesthetic
class UI:
     # Prompts the user through the STDIN for a number, takes the absolue value, checks if it's valid, and if not loops until valid input
    def getAbsIntInput(msg: str) -> int:
        while True:
            try:
                usrInput = abs(int(input(msg + " > ")))
                break
            except:
                usrInput = abs(int(input("(Invalid Input) " + msg + " > ")))
        
        return usrInput
