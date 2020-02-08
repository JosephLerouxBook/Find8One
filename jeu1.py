import math
import random
import time
import os

def is_already_done(arr, x, y):
    if arr[y-1][x-1] == 1 or arr[y-1][x-1] == 0:
        return 1
    return 0


def is_already_done_b(arr, x, y):
    if arr[y-1][x-1] == 1 or arr[y-1][x-1] == 0:
        print ("Mince... l'ordinateur c'est trompé...")


def print_arr2D(arr):
    for line in arr:
        for car in line:
            if (car == 0):
                print("\033[38;5;239m" + str(car) + "\033[0m", end=' ')
            elif (car == 1 ):
                print("\033[38;5;41m" + str(car) + "\033[0m", end=' ')
            else:
                print("\033[38;5;243m" + car + "\033[0m", end=' ')
        print("\r")
        #print(*line)


def check_user_coord(arr_p, coord):
    if coord == "" or coord == " ":
        print("Vous n'avez rien rentrez. ")
        return 0
    if len(coord) <= 2 or len(coord) > 3:
        print("Ce n'est pas le bon format.\nRessayez avec ce format : 1;1.")
        return 0
    if coord[0].isdigit() == False or coord[2].isdigit() == False:
        print("Vous avez rentrer un caractere qui n'est pas un nombre.")
        return 0
    x = int(coord[0])
    y = int(coord[2])
    if x < 1 or y < 1 or x > 9 or y >= 9:
        print("Vos nombre est trop petit, ou trop grand. \nRéessayer avec des valeurs comprises entre 1 et 8")
        return 0

    if is_already_done(arr_p, x, y) == 1:
        print("Deja choisit. voir le plateau :\n")
        print_arr2D(arr_p)
        return 0
    return 1


def get_user_coord(arr_p):
    coord = input("Rentrez vos coordonnées de type \"x;x\" où x est un chiffre allant de 1 à 8\n")
    while (check_user_coord(arr_p, coord) == 0):
        coord = input("Réessayer\n")
    return coord


def get_bot_coord(arr_p):
    coord = [random.randint(1, 8), random.randint(1, 8)]
    x = int(coord[0])
    y = int(coord[1])
    while (is_already_done(arr_p, x, y) == 1):
        print("Hmmm... Laisse moi réfléchir...")
        coord = [random.randint(1, 8), random.randint(1, 8)]
    return coord
#
# Déclaration
#
arr = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
arr_p = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
score_j = 0
score_b = 0
p_coord = 0
b_coord = 0
p_x = 0
p_y = 0
b_x = 0
b_y = 0

#
# Traitement
#

# Création de la map 0-1
for i in range(0, 8):
    j = random.randint(0, 7)
    arr[i][j] = 1

#Intro
print("\033[38;5;38mBienvenue !\nLes regles sont simples : Un tableau de 8x8 cache des 1 et des 0. Il n'y as qu'un 1 par ligne.\nVotre but? Trouvez tout les 1 avant votre adversaire.\nBonne chance\033[0m")

while(score_b + score_j != 8 or score_b > 5 or score_j > 5):
    #Tour du joueur
    print("\nvotre tour...")
    #print("\033[38;5;240m     #That is, \033[38;5;<FG COLOR>m")
    p_coord = get_user_coord(arr_p)
    p_x = int(p_coord[0]) #- 1
    p_y = int(p_coord[2]) #- 1
    print("Vous avez choisit: ", p_x, p_y)
    if arr[p_y - 1][p_x - 1] == 1:
        arr_p[p_y - 1][p_x - 1] = 1
        print("yay")
        score_j += 1
    else:
        arr_p[p_y - 1][p_x - 1] = 0
        print("Presque")
    time.sleep(1)
    print_arr2D(arr_p)

    #Tour du BOT
    print("\nAu tour de l'ordinateur....")
    time.sleep(1)
    b_coord = get_bot_coord(arr_p)
    b_x = int(b_coord[0])
    b_y = int(b_coord[1])
    print("L'ordinateur a choisit: ", b_x, b_y)
    time.sleep(1)
    if arr[b_y-1][b_x-1] == 1:
        arr_p[b_y-1][b_x-1] = 1
        print("bot:Yay")
        score_b +=1
    else:
        arr_p[b_y-1][b_x-1] = 0
        print("bot:presque")
    time.sleep(1)
    print_arr2D(arr_p)

    print("\n\033[38;5;23m#############Fin du tour#############\nLes scores sont :\033[0m\n\033[38;5;22mJoueur:\033[0m", "\033[38;5;28m", score_j,"\033[0m", "\n\033[38;5;52mBot:\033[0m", "\033[38;5;88m", score_b,"\033[0m", "\n\033[38;5;23m#####################################\033[0m")
