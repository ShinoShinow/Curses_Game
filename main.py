import curses
import random
# import time

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.nodelay(True)
stdscr.keypad(True)
max_line = curses.LINES - 1
max_cols = curses.COLS - 1

world = []
food_cols = []
food_lines = []
Player_line = random.randint(0,max_line)
Player_cols = random.randint(0,max_cols)

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
    
def draw(Pline,Pcols) :
    global i , j
    for i in range(max_line) :
        for j in range(max_cols) :
            stdscr.addch(i , j,world[i][j])
    stdscr.addch(Pline,Pcols,'x')
    food()
    stdscr.refresh() 

init()

def food() :
    global food_lines,food_cols
    for i in range(20) :    
        food_cols_rand = random.randint(1,max_cols -2)
        food_lines_rand = random.randint(1,max_line -2)
        while world[food_lines_rand][food_cols_rand] == '.' :
            food_cols_rand = random.randint(1,max_cols -2)
            food_lines_rand = random.randint(1,max_line -2)            
        food_cols.append(food_cols_rand)
        food_lines.append(food_lines_rand)
    for i in range(20) :    
        world[food_lines[i]][food_cols[i]] = '*'    


food()
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
while game :
    try  :
        ch = stdscr.getkey()
    except :
        ch = ' '
    if ch in "asdw" :
        move(ch)
    if ch == 'q' :
        game = False
    draw(Player_line,Player_cols)
