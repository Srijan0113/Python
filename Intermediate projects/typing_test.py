import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear() #clear the entire screen
    stdscr.addstr(" Welcome to the Typing Speed Test !")
    stdscr.addstr("Press any key to continue!")
    stdscr.refresh()
    stdscr.getkey()
    
def display_text(stdscr, target , current,wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(3,0,f"WPM : {wpm}")
    for i,char in enumerate(current):
        correct_char=target[i]
        color=curses.color_pair(1)
        if char!= correct_char:
            color=curses.color_pair(2)
        stdscr.addstr(0,i,char,color)

def load_text():
    with open("paragraphs.txt", "r") as f:
      paragraphs = f.read().split("\n\n") #split by blank lines
      return random.choice(paragraphs)

def wpm_test(stdscr):
    target_text = load_text()
    current_text=[]
    wpm = 0
    start_time=time.time()
    stdscr.nodelay(True)
    
    while True:
        time_elapsed=max(time.time()-start_time,1)
        wpm = round((len(current_text)/(time_elapsed/60))/5)
        stdscr.clear() #clear the entire screen
        display_text(stdscr,target_text,current_text,wpm)
        stdscr.refresh()

        if "".join(current_text)==target_text:
            stdscr.nodelay(False)
            break
        try:
          key=stdscr.getkey() # it is blocking the wpm 
        except:
            continue

        if ord(key)==27:    #ascii value for esc button 
            break

        if key in ("KEY_BACKSPACE",'\b',"\x7f"):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text)<len(target_text):
            current_text.append(key)

def main(stdscr): #standard output ........ screen
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    start_screen(stdscr)
    while True:
     wpm_test(stdscr)
     stdscr.addstr(2,0,"You completed the text ! Press any key to continue")
     key=stdscr.getkey()
     if ord(key)==27:
         break

wrapper(main)