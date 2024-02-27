import curses
import random
import time

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.nodelay(True)
stdscr.keypad(True)
max_line = curses.LINES - 1
max_cols = curses.COLS - 1

world = []
Player_line = random.randint(0,max_line)
Player_cols = random.randint(0,max_cols)
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
    for i in range(max_line) :
        for j in range(max_cols) :
            stdscr.addch(i , j,world[i][j])
    stdscr.addch(Pline,Pcols,'x')
    stdscr.refresh()  

init()
game = True
def move(key) :
    global Player_cols , Player_line
    if key == 'w' :
        Player_line -= 1
    if key == 's' :
        Player_line += 1
    if key == 'd' :
        Player_cols += 1
    if key == 'a' :
        Player_cols -= 1    
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
