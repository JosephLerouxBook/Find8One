from importa import *

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
                print(str(car), end=' ')
                #print("\033[38;5;239m" + str(car) + "\033[0m", end=' ')
            elif (car == 1):
                print("\033[38;5;41m" + str(car) + "\033[0m", end=' ')
            else:
                print("\033[38;5;243m" + car + "\033[0m", end=' ')
        print("\r")


def check_user_coord(arr_p, coord):
    if coord == "" or coord == " ":
        print("\033[38;5;166mVous n'avez rien rentrez.\033[0m")
        return 0
    if len(coord) <= 2 or len(coord) > 3:
        print("\033[38;5;166mCe n'est pas le bon format.\nRessayez avec ce format : 1;1.\033[0m")
        return 0
    if coord[0].isdigit() == False or coord[2].isdigit() == False:
        print("\033[38;5;166mVous avez rentrer un caractere qui n'est pas un nombre.\033[0m")
        return 0
    x = int(coord[0])
    y = int(coord[2])
    if x < 1 or y < 1 or x > 9 or y >= 9:
        print("\033[38;5;166mVos nombre est trop petit, ou trop grand. \nRéessayer avec des valeurs comprises entre 1 et 8\033[0m")
        return 0

    if is_already_done(arr_p, x, y) == 1:
        print("\033[38;5;166mDeja choisit. voir le plateau :\n\033[0m")
        print_arr2D(arr_p)
        return 0
    return 1


def get_user_coord(arr_p):
    coord = input("Rentrez vos coordonnées de type \"x;x\" où x est un chiffre allant de 1 à 8\n")
    while (check_user_coord(arr_p, coord) == 0):
        coord = input("\033[38;5;166mRéessayer\033[0m\n")
    return coord


def get_bot_coord(notdoneliste):
    ind = random.randint(0, (len(notdoneliste)-1))
    coord = notdoneliste[ind]
    notdoneliste.remove(coord)
    return coord


def delete_player_cord_from_not_done(notdoneliste, p_coordX, p_coordY):
    coord = str(p_coordX-1) + str(p_coordY-1)
    notdoneliste.remove(coord)
    return notdoneliste