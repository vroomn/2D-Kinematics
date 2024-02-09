import pygame

class UI:
    def getAbsIntInput(msg: str) -> int:
        while True:
            try:
                usrInput = abs(int(input(msg + " > ")))
                break
            except:
                usrInput = abs(int(input("(Invalid Input) " + msg + " > ")))
        
        return usrInput
