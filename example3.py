#!/usr/bin/python3

from curses_anim import *
import math

# this is a minimal example

def test(stdscr):

    # define two generators (functions that spit out coordinates and printable chars)
    def gen1(i):
        return [(round(0.1*i*j),j,'*') for j in range(80)]

    def gen2(i):
        return [(round(0.1*i*j),j+100,'*') for j in range(80)]

    # define main animation object
    anim = Anim(stdscr, 0.05)

    # define generator objects
    generator1 = Generator(1000, gen1, stdscr)
    generator2 = Generator(2000, gen2, stdscr)

    # add generators to animation loop with desired refresh rates (default is 1)
    anim.add_generator(generator1, 2)
    anim.add_generator(generator2)

    # start animation loop
    anim.start_anim()

# handle terminal settings (echo off, etc.) in case our program crashes
curses.wrapper(test)

