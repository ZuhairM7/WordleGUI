
import pygame
import time

pygame.init()

# defines the width and height of the display
display_width = 600
display_height = 680

# defines block width and height
block_height = 50 * 1.5
block_width = 50 * 1.5

factor = 25 * 1.5

# defines colours
white = (255, 255, 255)
d_white = (250, 250, 250)
black = (0, 0, 0)
teal = (0, 128, 128)
blue_black = (50, 50, 50)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.update()
clock = pygame.time.Clock()

selected_family = "black"


class piece:
    x = 0  # x coordinate
    y = 0  # y coordinate
    rank = ""  # rank of the piece
    life = True  # is the piece dead or alive
    family = ""  # colour of the piece (black or white)
    pic = ""  # photo of the piece

    def __init__(self, x_position, y_position, p_rank, p_family):
        self.x = x_position
        self.y = y_position
        self.rank = p_rank
        self.family = p_family


selected_piece = piece
end_piece = piece
pie = [piece(3, 7, "q", "black"), piece(0, 6, "p", "black"), piece(1, 6, "p", "black"), piece(2, 6, "p", "black"),
       piece(2, 0, "b", "white"), piece(5, 0, "b", "white"), piece(0, 0, "r", "white"), piece(7, 0, "r", "white"),
       piece(3, 6, "p", "black"), piece(4, 6, "p", "black"), piece(5, 6, "p", "black"), piece(6, 6, "p", "black"),
       piece(7, 6, "p", "black"), piece(1, 0, "k", "white"), piece(6, 0, "k", "white"), piece(4, 0, "king", "white"),
       piece(0, 1, "p", "white"), piece(1, 1, "p", "white"), piece(2, 1, "p", "white"), piece(3, 1, "p", "white"),
       piece(4, 1, "p", "white"), piece(5, 1, "p", "white"), piece(6, 1, "p", "white"), piece(7, 1, "p", "white"),
       piece(3, 0, "q", "white"), piece(2, 7, "b", "black"), piece(5, 7, "b", "black"), piece(0, 7, "r", "black"),
       piece(7, 7, "r", "black"), piece(1, 7, "k", "black"), piece(6, 7, "k", "black"), piece(4, 7, "king", "black") ]

print(pie[0].x, pie[0].y)


def initialize_piece():
    i = 0
    while i < len(pie):
        if pie[i].rank == "p" and pie[i].life:
            # pygame.draw.rect(game_display, teal, ((2 * pie[i].x + 1) * 25, ((2 * pie[i].y + 1) * 25), 12, 12))
            if pie[i].family == "white":
                img = pygame.image.load("pawn_white.png")
            else:
                img = pygame.image.load("pawn_black.png")
            game_display.blit(img, ((2 * pie[i].x) * factor, ((2 * pie[i].y) * factor)))

        elif pie[i].rank == "q" and pie[i].life:
            # pygame.draw.rect(game_display, black, ((2 * pie[i].x + 1) * 25, ((2 * pie[i].y + 1) * 25), 12, 12))
            if pie[i].family == "white":
                img = pygame.image.load("queen_white.png")
            else:
                img = pygame.image.load("queen_black.png")
            game_display.blit(img, ((2 * pie[i].x) * factor, ((2 * pie[i].y) * factor)))
        elif pie[i].rank == "b" and pie[i].life:
            # pygame.draw.rect(game_display, black, ((2 * pie[i].x + 1) * 25, ((2 * pie[i].y + 1) * 25), 12, 12))
            if pie[i].family == "white":
                img = pygame.image.load("bishop_white.png")
            else:
                img = pygame.image.load("bishop_black.png")
            game_display.blit(img, ((2 * pie[i].x) * factor, ((2 * pie[i].y) * factor)))
        elif pie[i].rank == "r" and pie[i].life:
            # pygame.draw.rect(game_display, black, ((2 * pie[i].x + 1) * 25, ((2 * pie[i].y + 1) * 25), 12, 12))
            if pie[i].family == "white":
                img = pygame.image.load("rook_white.png")
            else:
                img = pygame.image.load("rook_black.png")
            game_display.blit(img, ((2 * pie[i].x) * factor, ((2 * pie[i].y) * factor)))
        elif pie[i].rank == "k" and pie[i].life:
            # pygame.draw.rect(game_display, black, ((2 * pie[i].x + 1) * 25, ((2 * pie[i].y + 1) * 25), 12, 12))
            if pie[i].family == "white":
                img = pygame.image.load("knight_white.png")
            else:
                img = pygame.image.load("knight_black.png")
            game_display.blit(img, ((2 * pie[i].x) * factor, ((2 * pie[i].y) * factor)))
        elif pie[i].rank == "king" and pie[i].life:
            # pygame.draw.rect(game_display, black, ((2 * pie[i].x + 1) * 25, ((2 * pie[i].y + 1) * 25), 12, 12))
            if pie[i].family == "white":
                img = pygame.image.load("king_white.png")
            else:
                img = pygame.image.load("king_black.png")
            game_display.blit(img, ((2 * pie[i].x) * factor, ((2 * pie[i].y) * factor)))
        i += 1


def clear():
    i = 0
    while i < len(pie):
        if (pie[i].x + pie[i].y) % 2 == 0:
            pygame.draw.rect(game_display, d_white, ((2 * pie[i].x + 1) * 25, ((2 * pie[i].y + 1) * 25), 12, 12))
        else:
            pygame.draw.rect(game_display, blue_black, ((2 * pie[i].x + 1) * 25, ((2 * pie[i].y + 1) * 25), 12, 12))

        i += 1


def move(orignal_x, orignal_y, final_x, final_y):
    val = False
    t = 9
    final_pie = piece
    # print(final_x, "+", final_y)
    global selected_family
    fam = selected_family
    for i in range(len(pie)):
        final_pie = None
        if pie[i].x == orignal_x and pie[i].y == orignal_y and pie[i].life and pie[i].family == fam:
            for k in range(len(pie)):
                if pie[k].x == final_x and pie[k].y == final_y and pie[k].life:
                    final_pie = pie[k]
                    t = k
                    break
                    # If the pieces are not of same family then
            ############## For pawns  ###################
            if pie[i].rank == 'p' and final_pie != None:
                if final_pie.family != pie[i].family and orignal_x != final_x:
                    if orignal_x + 1 == final_x or orignal_x - 1 == final_x:
                        if pie[i].family == "black":
                            direction = -1
                        else:
                            direction = 1
                        if orignal_y + direction == final_y:
                            pie[t].life = False
                            pie[i].x = final_x
                            pie[i].y = final_y
                            if pie[i].family == "white":
                                selected_family = "black"
                            else:
                                selected_family = "white"
                                clear()
                            print(pie[t].x, final_pie.y, " <--")
                else:
                    val = True
                    ################# QUEEN #####################
            if pie[i].rank == 'q' and final_pie != None:
                if pie[t].family != pie[i].family:
                    if check_queen(orignal_x, orignal_y, final_x, final_y):
                        pie[t].life = False
                        pie[i].x = final_x
                        pie[i].y = final_y
                        if pie[i].family == "white":
                            selected_family = "black"
                        else:
                            selected_family = "white"
                        clear()
                        # print(pie[t].x, final_pie.y, " <--")
                        clear()
                else:
                    val = True
                    ###### bishop ##############
            if pie[i].rank == 'b' and final_pie != None:
                if pie[t].family != pie[i].family:
                    if diagonalcheck(orignal_x, orignal_y, final_x, final_y):
                        print("yaah")
                        pie[t].life = False
                        pie[i].x = final_x
                        pie[i].y = final_y
                        if pie[i].family == "white":
                            selected_family = "black"
                        else:
                            selected_family = "white"
                        clear()
                        # print(pie[t].x, final_pie.y, " <--")
                        clear()
                else:
                    val = True
                    ########## rook #############
            if pie[i].rank == 'r' and final_pie != None:
                if pie[t].family != pie[i].family:
                    if check_rook(orignal_x, orignal_y, final_x, final_y):
                        print("yaah")
                        pie[t].life = False
                        pie[i].x = final_x
                        pie[i].y = final_y
                        if pie[i].family == "white":
                            selected_family = "black"
                        else:
                            selected_family = "white"
                        clear()
                        # print(pie[t].x, final_pie.y, " <--")
                        clear()
                else:
                    val = True
                    ############# Knight #############
            if pie[i].rank == 'k' and final_pie != None:
                if pie[t].family != pie[i].family:
                    if knight_check(orignal_x, orignal_y, final_x, final_y):
                        print("yaah")
                        pie[t].life = False
                        pie[i].x = final_x
                        pie[i].y = final_y
                        if pie[i].family == "white":
                            selected_family = "black"
                        else:
                            selected_family = "white"
                        clear()
                        # print(pie[t].x, final_pie.y, " <--")
                        clear()
                else:
                    val = True
                    ######### kiNG #########################
            if pie[i].rank == 'king' and final_pie != None:
                if pie[t].family != pie[i].family:
                    if king_check(orignal_x, orignal_y, final_x, final_y):
                        pie[t].life = False
                        pie[i].x = final_x
                        pie[i].y = final_y
                        if pie[i].family == "white":
                            selected_family = "black"
                        else:
                            selected_family = "white"
                        clear()
                        # print(pie[t].x, final_pie.y, " <--")
                        clear()
                else:
                    val = True
    if val is False:

        for i in range(len(pie)):
            if pie[i].x == orignal_x and pie[i].y == orignal_y and pie[i].family == selected_family:
                clear()
                ####### pawn:  ###############
                if pie[i].rank == "p":
                    if pie[i].family == "black":
                        direction = -1
                    else:
                        direction = 1
                    if orignal_y == 6 or orignal_y == 1:
                        if final_y == orignal_y + (2 * direction) and final_x == orignal_x:
                            rigt_upfront = False
                            for k in range(len(pie)):
                                if pie[k].y == orignal_y + direction and pie[k].x == orignal_x:
                                    rigt_upfront = True
                            if not rigt_upfront:
                                pie[i].x = final_x
                                pie[i].y = final_y
                                if pie[i].family == "white":
                                    selected_family = "black"
                                else:
                                    selected_family = "white"
                    if final_y == orignal_y + direction and final_x == orignal_x:
                        pie[i].x = final_x
                        pie[i].y = final_y
                        if pie[i].family == "white":
                            selected_family = "black"
                        else:
                            selected_family = "white"
                ########## Queen ###############################
                if pie[i].rank == "q":
                    if check_queen(orignal_x, orignal_y, final_x, final_y):
                        pie[i].x = final_x
                        pie[i].y = final_y
                        if pie[i].family == "white":
                            selected_family = "black"
                        else:
                            selected_family = "white"
                ########## bishop ##########################'
                if pie[i].rank == "b":
                    if diagonalcheck(orignal_x, orignal_y, final_x, final_y):
                        if diagonal(orignal_x, orignal_y, final_x, final_y):
                            pie[i].x = final_x
                            pie[i].y = final_y
                            if pie[i].family == "white":
                                selected_family = "black"
                            else:
                                selected_family = "white"
                ############ rook #############
                if pie[i].rank == "r":
                    if check_rook(orignal_x, orignal_y, final_x, final_y):
                        pie[i].x = final_x
                        pie[i].y = final_y
                        if pie[i].family == "white":
                            selected_family = "black"
                        else:
                            selected_family = "white"
                ########## Knight ###########
                if pie[i].rank == "k":
                    if knight_check(orignal_x, orignal_y, final_x, final_y):
                        pie[i].x = final_x
                        pie[i].y = final_y
                        if pie[i].family == "white":
                            selected_family = "black"
                        else:
                            selected_family = "white"
                ######## KING ##################
                if pie[i].rank == "king":
                    if king_check(orignal_x, orignal_y, final_x, final_y):
                        pie[i].x = final_x
                        pie[i].y = final_y
                        if pie[i].family == "white":
                            selected_family = "black"
                        else:
                            selected_family = "white"


def check_queen(x_i, y_i, x_f, y_f):
    col = True

    if x_i == x_f and y_i != y_f:
        a = 0
        b = 0
        if y_i > y_f:
            a = y_i
            b = y_f
        else:
            a = y_f
            b = y_i

        for i in range(b, a):
            if i == b:
                col = True
            else:
                for k in range(len(pie)):
                    if pie[k].x == x_f and pie[k].y == i and pie[k].life:
                        col = False
    elif x_i != x_f and y_i == y_f:
        a = 0
        b = 0
        if x_i > x_f:
            a = x_i
            b = x_f
        else:
            a = x_f
            b = x_i

        for i in range(b, a):
            if i == b:
                col = True
            else:
                for k in range(len(pie)):
                    if pie[k].y == y_f and pie[k].x == i and pie[k].life:
                        col = False
    elif diagonalcheck(x_i, y_i, x_f, y_f):
        if diagonal(x_i, y_i, x_f, y_f):
            col = True
    else:
        col = False
    return col


def king_check(x_i, y_i, x_f, y_f):
    col = False

    if x_i+1 == x_f and y_i == y_f:
        col = True
    elif x_i + 1 == x_f and y_i +1 == y_f:
        col = True
    elif x_i + 1 == x_f and y_i -1 == y_f:
        col = True
    elif x_i-1 == x_f and y_i == y_f:
        col = True
    elif x_i - 1 == x_f and y_i +1 == y_f:
        col = True
    elif x_i - 1 == x_f and y_i -1 == y_f:
        col = True
    elif x_i  == x_f and y_i -1 == y_f:
        col = True
    elif x_i  == x_f and y_i -1 == y_f:
        col = True
    elif x_i  == x_f and y_i -1 == y_f:
        col = True
    return col

def check_rook(x_i, y_i, x_f, y_f):
    col = True

    if x_i == x_f and y_i != y_f:
        a = 0
        b = 0
        if y_i > y_f:
            a = y_i
            b = y_f
        else:
            a = y_f
            b = y_i

        for i in range(b, a):
            if i == b:
                col = True
            else:
                for k in range(len(pie)):
                    if pie[k].x == x_f and pie[k].y == i and pie[k].life:
                        col = False
    elif x_i != x_f and y_i == y_f:
        a = 0
        b = 0
        if x_i > x_f:
            a = x_i
            b = x_f
        else:
            a = x_f
            b = x_i

        for i in range(b, a):
            if i == b:
                col = True
            else:
                for k in range(len(pie)):
                    if pie[k].y == y_f and pie[k].x == i and pie[k].life:
                        col = False
    else:
        col = False
    return col

def knight_check(i_x, i_y, f_x, f_y):
    t = False
    if i_x+1 == f_x and i_y+2 == f_y:
        t = True
    elif i_x+1 == f_x and  i_y-2 == f_y:
        t = True
    elif i_x-1 == f_x and  i_y+2 == f_y:
        t = True
    elif i_x-1 == f_x and  i_y-2 == f_y:
        t = True
    elif i_x+2 == f_x and  i_y+1 == f_y:
        t = True
    elif i_x+2 == f_x and  i_y-1 == f_y:
        t = True
    elif i_x-2 == f_x and  i_y+1 == f_y:
        t = True
    elif i_x-2 == f_x and  i_y-1 == f_y:
        t = True
    return t

def diagonalcheck(i_x, i_y, f_x, f_y):
    dir_x = 0
    dir_y = 0
    th = False
    a = i_x
    b = i_y
    if i_x < f_x:
        dir_x = +1
    elif i_x > f_x:
        dir_x = -1
    if i_y < f_y:
        dir_y = 1
    elif i_y > f_y:
        dir_y = -1
    while a < 8 and a >= 0 and b < 8 and b >= 0 and dir_x != 0 and dir_y != 0:
        if a == f_x and b == f_y:
            print("yes")
            th = True
        a += dir_x
        b += dir_y
    return th


def diagonal(i_x, i_y, f_x, f_y):
    dir_x = 0
    dir_y = 0
    th = True
    a = i_x
    b = i_y

    if i_x < f_x:
        dir_x = +1
    elif i_x > f_x:
        dir_x = -1
    if i_y < f_y:
        dir_y = 1
    elif i_y > f_y:
        dir_y = -1
    print("a =", a, ",b =", b, ",dir x =", dir_x, ",dir y =", dir_y, ",final x =", f_x, "final y =", f_y)
    while a != f_x and b != f_y:
        for i in range(len(pie)):
            print("a =", a, ",b =", b)
            if pie[i].x == a + dir_x and pie[i].y == b + dir_y:
                th = False
                # print(pie[i].x ," ", pie[i].y)

        a = a + dir_x
        b = b + dir_y
    if i_x == f_x or i_y == f_y:
        th = False
    return th


def board_draw():
    x = 0
    y = 0
    game_display.fill(black)


    selected_family = "black"
    for i in range(8):
        if i % 2 == 0:
            j = 0
        else:
            j = 1
        while j < 8:
            pygame.draw.rect(game_display, d_white, (i * 50 * 1.5, j * 50 *1.5, block_width, block_height))
            j += 2

def select_block(x_cursor, y_cursor):
    selected_piece = None
    for i in range(len(pie)):
        if pie[i].x == x_cursor and pie[i].y == y_cursor:

            return pie[i]


def game():
    selec = False
    global selected_family
    while True:

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a = pos[0] // 75
                b = pos[1] // 75
                pygame.draw.rect(game_display, teal, (a * 50 * 1.5, b * 50 * 1.5, block_width, block_height))
                pygame.display.update()
                time.sleep(0.03)

                if not selec:
                    selected_piece = select_block(a, b)
                    selec = True
                    if selected_piece is not None:
                        print(selected_piece.x, " ", selected_piece.y)

                    else:
                        selec = False
                else:
                    if selected_piece is not None:
                        move(selected_piece.x, selected_piece.y, a, b)
                    selec = False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        board_draw()

        initialize_piece()
        myfont = pygame.font.Font("sans.ttf", 30)
        string = selected_family +"'s turn"
        label = myfont.render(string, 1, white)


        game_display.blit(label, (20, 620))
        pygame.display.update()

        clock.tick(20)


game()

if __name__ == '__main__':
    main()