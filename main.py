import curses
import random
from time import sleep

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.nodelay(True)
stdscr.keypad(True)
max_line = curses.LINES - 1
max_cols = curses.COLS - 1

enemy_lines = []
enemy_cols  = []


world = []
score = 0

def init() :
    for i in range(max_line) :
        world.append([])
        for j in range(max_cols) :
            world[i].append(' ' if random.random() > 0.05 else '.')

def rang(value,min,max) :
    if value > max :
        return max
    elif value < min : 
        return min
    else :
        return value
init()
for i in range(3) :
    rand_line = random.randint(0,max_line-2)
    rand_cols = random.randint(0,max_cols-2)
    while world[rand_line][rand_cols] == '.' :
        rand_line = random.randint(0,max_line-2)
        rand_cols = random.randint(0,max_cols-2)
    enemy_lines.append(rand_line)
    enemy_cols.append(rand_cols)

def draw(Pline,Pcols) :
    global i , j , score
    for i in range(max_line) :
        for j in range(max_cols) :
            stdscr.addch(i , j,world[i][j])
    stdscr.addstr(1,1,f"Score: {score}")
    for i in range(3) :
        stdscr.addch(enemy_lines[i],enemy_cols[i],'E')
    stdscr.addch(Pline,Pcols,'x')
    stdscr.refresh() 

def random_gen() :
    a = random.randint(0,max_line - 2)
    b = random.randint(0,max_cols - 2)
    while world[a][b] == '.' :
        a = random.randint(0,max_line - 2)
        b = random.randint(0,max_cols - 2)
    return a , b

Player_line , Player_cols = random_gen()

for item in range(20) :
    foodline , foodclos = random_gen() 
    world[foodline][foodclos] = '*'

def check_food() :
    global score
    if world[Player_line][Player_cols] == '*' :
        world[Player_line][Player_cols]  = ' '
        food_line_r , food_clos_r = random_gen()
        world[food_line_r][food_clos_r] = '*'
        score += 10

def check_Die() :
    global game
    for i in range(3) :
        if Player_line == enemy_lines[i] and Player_cols == enemy_cols[i] :
            stdscr.addstr(max_line // 2, max_cols // 2,"You Losed!!")
            stdscr.refresh()
            sleep(3)
            stdscr.clear()
            stdscr.refresh()
            game = False

game = True
def move(key) :
    global Player_cols , Player_line
    try :
        if key == 'w' and world[Player_line -1][Player_cols] != '.'  :
            Player_line -= 1
        if key == 's' and world[Player_line +1][Player_cols] != '.' :
            Player_line += 1
        if key == 'd' and world[Player_line][Player_cols + 1] != '.':
            Player_cols += 1
        if key == 'a' and world[Player_line][Player_cols - 1] != '.' :
            Player_cols -= 1
    except:
        pass
    Player_cols = rang(Player_cols,0,max_cols - 1)
    Player_line = rang(Player_line,0,max_line - 1)

def enemy_move() :
    if random.random() < 0.005 :
        if enemy_lines[0] > Player_line :
            enemy_lines[0] -= 1
        if enemy_lines[0] < Player_line :
            enemy_lines[0] += 1
        if enemy_cols[0] > Player_cols :
            enemy_cols[0] -= 1
        if enemy_cols[0] < Player_cols :
            enemy_cols[0] += 1
    if random.random() > 0.995 :
        if enemy_lines[1] > Player_line :
            enemy_lines[1] -= 1
        if enemy_lines[1] < Player_line :
            enemy_lines[1] += 1
        if enemy_cols[1] > Player_cols :
            enemy_cols[1] -= 1
        if enemy_cols[1] < Player_cols :
            enemy_cols[1] += 1
    if 0.600 > random.random() > 0.595 :
        if enemy_lines[2] > Player_line :
            enemy_lines[2] -= 1
        if enemy_lines[2] < Player_line :
            enemy_lines[2] += 1
        if enemy_cols[2] > Player_cols :
            enemy_cols[2] -= 1
        if enemy_cols[2] < Player_cols :
            enemy_cols[2] += 1

while game :
    try  :
        ch = stdscr.getkey()
    except :
        ch = ' '
    if ch in "asdw" :
        move(ch)
    if ch == 'q' :
        game = False
    check_food()
    draw(Player_line,Player_cols)
    enemy_move()
    check_Die()

