import random
import time

rock = 1
paper = 2
scissors = 3

names = { rock: "rock", paper: "paper", scissors: "Scissors" }
rules = { rock: scissors, paper: rock, scissors: paper }

player_score = 0
computer_score = 0

def start():
    print("¡¡¡lvamo a jugar chavales!!!")
    while game():
        pass
    scores()

def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()

def move():
    while True:
        print
        player = input("rock = 1\npaper = 2\nscissors = 3\nMake a move: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print ("Que dijiste flaco, yo pendejades no hablo.")

def result(player, computer):
    print ("1...")
    time.sleep(1)
    print ("2...")
    time.sleep(1)
    print("3!")
    time.sleep(0.5)
    print ("Computer threw!")
    global player_score, computer_score
    if player == computer:
        print("Tie game.")
    else:
        if rules[player] == computer:
            print("haz ganado una nalgada,Felicidades")
            player_score += 1
        else:
            print("tremendo bolacero aprende a jugar flaco")
            computer_score += 1
    
def play_again():
    answer = input("¿Queres pasar otro mal rato? y/n: ")
    if answer in ("y","Y", "yes", "bueno"):
        return answer
    else:
        print("Nos vemos la procima cagon")


def scores():
    global player_score, computer_score
    print("total scores")
    print("Jugador:", player_score)
    print("Computadora", computer_score)

if __name__ == "__main__":
    start()