#!/usr/bin/python3

import curses
import time

class Anim:
    """
    animations are handled by using generators.
    each generator can handle one component of the animation
    which can be arbitrarily complex given its output only depends on
    the current (time) index of the animation
    """
    
    def __init__(self, scr):
        self.generators = []    # generators are stored in this list
        self.scr        = scr   # curses window on which to draw

    def add_generator(self, gen, update_rate=1):
        """ add 1 generator """
        self.generators.append((gen, update_rate))

    def start_anim(self):
        
        gen_indices    = [i for i in range(len(self.generators))]
        update_counter = [1 for i in range(len(self.generators))]

        while len(gen_indices) > 0:
        # there are still active generators left
            
            # decrease update counter for each active generator
            update_counter = [update_counter[i]-1 for i in range(len(self.generators))]

            for gen_index in gen_indices:
                # it's the generators turn to do SOMETHING
                if (update_counter[gen_index] == 0):
                    update_counter[gen_index] = self.generators[gen_index][1]   # reset refresh timer
                    status = self.generators[gen_index][0].step()  # draw next string on screen

                    if (not status):
                        # generator finished; don't call this generator anymore
                        gen_indices.remove(gen_index)

            self.scr.refresh()
            time.sleep(0.05)  # set for debugging

class Generator:
    """ 
    each generator is a self-managing component of the animation.
    state is managed via an index counter (i), which is increased at each step.
    func is a generating function that, given the current animation index,
    returns y,x coordinates and a string to be printed on screen.
    """

    def __init__(self, iters, func, scr):
        self.max_iters = iters  # max step index
        self.func      = func   # function that returns location and character to be printed
        self.i         = 0      # current step index
        self.scr       = scr    # screen on which to print
        (self.ymax, self.xmax) = scr.getmaxyx()  # get terminal dimensions

    def step(self):
        y, x, txt = self.func(self.i)    # fetch action for this step
        self.i += 1                 # increase step counter (update state)
        self.scr.addstr(y % self.ymax, x % self.xmax, txt)  # draw safely on screen

        return (self.i <= self.max_iters)  # generator not finished yet
