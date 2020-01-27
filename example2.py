#!/usr/bin/python3

from curses_anim import *
import math

# this is a minimal example

def test(stdscr):

    # define three generators (functions that spit out coordinates and printable chars)
    def gen1(i):
        return [(round(math.sin(0.5 * i) * 5) + 50, i, '.')]

    def gen2(i):
        return [(round(math.sin(.4 * i) * 10) + 30, i+50, '#')]

    def gen3(i):
        return [(round(math.sin(0.5 * i) * 2) + i // 20, 2 * i, '*')]

    # define main animation object
    anim = Anim(stdscr, 0.05)

    # define generator objects
    generator1 = Generator(1000, gen1, stdscr)
    generator2 = Generator(2000, gen2, stdscr)
    generator3 = Generator(2000, gen3, stdscr)

    # add generators to animation loop with desired refresh rates (default is 1)
    anim.add_generator(generator1, 2)
    anim.add_generator(generator2)
    anim.add_generator(generator3)

    # start animation loop
    anim.start_anim()

# handle terminal settings (echo off, etc.) in case our program crashes
curses.wrapper(test)

