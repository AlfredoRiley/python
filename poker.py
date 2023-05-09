import random
from itertools import groupby

nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6

names = {nine: "9",ten: "10", jack: "J", queen: "Q", king: "A", ace: "A"}

pj_score = 0
pc_score = 0

def start():
    print("")