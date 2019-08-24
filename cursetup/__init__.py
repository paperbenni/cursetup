#!/usr/bin/env python3
import curses
import time


def setup():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    stdscr.keypad(True)
    return stdscr


def quit(stdscr):
    curses.echo()
    curses.nocbreak()
    stdscr.keypad(False)
    curses.endwin()


def centertext(text, window):
    textl = text.split('\n')
    height, width = window.getmaxyx()
    textcounter = 0
    for i in textl:
        window.addstr(height/2-len(textl) + textcounter,
                      width/2 - (len(i)/2), text)
        textcounter += 1
    window.refresh()


def animatetext(atext, window):
    btext = ''
    for i in range(len(atext)):
        btext += atext[i]
        centertext(btext, window)
        window.refresh()
        time.sleep(.05)


def setup_input(window):
    sub = window.subwin(1, 40, 3, 2)
    tb = curses.textpad.Textbox(sub)
    window.refresh()
    tb.edit()
