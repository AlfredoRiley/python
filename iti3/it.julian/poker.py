from dataclasses import replace
import random
from itertools import groupby
from select import select

nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6

names = {nine: "9",ten: "10", jack: "J", queen: "Q", king: "K", ace: "A"}

pj_score = 0
pc_score = 0
scores = 0
def start():
    print("--------------------------------------------------------------")
    print("Vamos jugaar cagon")
    while game():
        pass
    scores()

def game():
    print("Vamo a tirar los 5 dados")
    throws()
    return pj_again()

def throws(): 
    roll_number = 5
    dice = roll(roll_number)
    dice.sort()
    for i in range(len(dice)):
        print("Dado",i + 1,":",names[dice[i]])

    result = hand(dice)
    print("por ahora tenes:",result)

    while true:
        rerolls = input("¿cuanto dados va a tirar CAGON?")
        try:
            if rerolls in (1,2,3,4,5):
                break
        except ValueError:
            pass
        print("NO SEAS TONTO, pone un numero de 1 al 5 BOBO")
    if rerolls == 0:
        print("SE TERMINO EL JUEGO CAGON",result)
    else:
        roll_number = rerolls
        dice_rerolls = roll(roll_number)
        dice_changes = range(rerolls)
        print("introduci un numero del dado:")
        iterations = 0
        while iterations < rerolls:
            iterations = iterations + 1
            while true:
                selection = input("")
                try:
                    if selection in (1,2,3,4,5):
                        break
                except ValueError:
                    pass
                print("TARADO, DEL 1 AL 5")
            dice_changes[iterations-1] = selection -1
            print("te camviaste de dado",selection)
            iterations = 0
            while iterations < rerolls:
                iterations = dice_rerolls[iterations-1]
                dice[dice_changes[iterations-1]] = replacement
                 