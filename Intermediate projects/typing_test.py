import curses #lets us build text-based UIs inside the terminal.
from curses import wrapper 
# wrapper a helper that safely initializes and cleans up curses so the terminal doesn’t get messed up after the program exits.
import time
import random

import curses

def display_text(stdscr, target, current, wpm=0):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # Draw WPM at the bottom
    stdscr.addstr(height - 2, 0, f"WPM: {wpm}")

    # --- Draw the target text with wrapping ---
    row, col = 0, 0
    for ch in target:
        if ch == "\n" or col >= width:  # wrap on newline or screen edge
            row += 1
            col = 0
        if row >= height - 3:  # leave space for WPM
            break
        stdscr.addstr(row, col, ch, curses.color_pair(3))
        col += 1

    # --- Overlay typed characters at same positions ---
    row, col = 0, 0
    for i, ch in enumerate(current):
        if col >= width:
            row += 1
            col = 0
        if row >= height - 3:
            break

        # Determine color based on correctness
        correct_ch = target[i]
        color = curses.color_pair(1) if ch == correct_ch else curses.color_pair(2)

        stdscr.addstr(row, col, ch, color)
        col += 1

    stdscr.refresh()



def start_screen(stdscr): 
#stdscr is a window object provided by curses that represents the entire terminal screen.
    stdscr.clear() #clear the entire screen
    stdscr.addstr("Welcome to the Typing Speed Test !")
    stdscr.addstr("Press any key to continue!")
    stdscr.refresh()
    stdscr.getkey()


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
    # makes input non-blocking (program continues running even if user doesn’t press a key).  

    while True:
        time_elapsed=max(time.time()-start_time,1)
        #how many seconds passed since start (at least 1 second to avoid division by zero).
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
     stdscr.addstr(2,0,"You completed the text ! Press Esc to escape or press any key to continue")
     key=stdscr.getch() #safer than getkey
     if key==27:
         break

wrapper(main)