from Fonctions import *
from importa import *

#
# Déclaration
#
arr = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
arr_p = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
not_done = ['00', '10', '20', '30', '40', '50', '60', '70', '01', '11', '21', '31', '41', '51', '61', '71', '02', '12', '22', '32', '42', '52', '62', '72', '03', '13', '23', '33', '43', '53', '63', '73', '04', '14', '24', '34', '44', '54', '64', '74', '05', '15', '25', '35', '45', '55', '65', '75', '06', '16', '26', '36', '46', '56', '66', '76', '07', '17', '27', '37', '47', '57', '67', '77']
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

while(score_b != 5 and score_j != 5):
    #Tour du joueur
    print("\nvotre tour...")
    #print("\033[38;5;240m     #That is, \033[38;5;<FG COLOR>m")
    p_coord = get_user_coord(arr_p)
    p_x = int(p_coord[0]) #- 1
    p_y = int(p_coord[2]) #- 1
    print("Vous avez choisit: ", p_x, p_y)
    if arr[p_y - 1][p_x - 1] == 1:
        arr_p[p_y - 1][p_x - 1] = 1
        print("Bien joué !")
        score_j += 1
    else:
        arr_p[p_y - 1][p_x - 1] = 0
        print("Dommage, Presque!")
    not_done = delete_player_cord_from_not_done(not_done, p_x, p_y)
    time.sleep(1)
    print_arr2D(arr_p)

    #Tour du BOT
    print("\nAu tour de l'ordinateur....")
    time.sleep(1)
    b_coord = get_bot_coord(not_done)
    b_x = int(b_coord[0])
    b_y = int(b_coord[1])
    print("L'ordinateur a choisit: ", b_x+1, b_y+1)
    time.sleep(1)
    #print("b_x : ",b_x)
    #print("b_y : ", b_y)
    if arr[b_y][b_x] == 1:
        arr_p[b_y][b_x] = 1
        print("Bot: \'Yay\'")
        score_b +=1
    else:
        arr_p[b_y][b_x] = 0
        print("Bot:\'Presque!\'")
    time.sleep(1)
    print_arr2D(arr_p)

    print("\n\033[38;5;23m#############Fin du tour#############\nLes scores sont :\033[0m\n\033[38;5;22mJoueur:\033[0m", "\033[38;5;28m", score_j,"\033[0m", "\n\033[38;5;52mBot:\033[0m", "\033[38;5;88m", score_b,"\033[0m", "\n\033[38;5;23m#####################################\033[0m")

if (score_j < score_b):
    print("\n\033[38;5;52mDommage ! Une prochaine fois peu etre !\033[0m")
else:
    print("\n\033[38;5;160mB\033[38;5;89mi\033[38;5;17m\033[38;5;26me\033[38;5;70mn \033[38;5;154mj\033[38;5;214mo\033[38;5;160mu\033[38;5;89mé\033[0m ! \033[38;5;34mChampion !")