__author__ = 'jgreiner'
# Jonathon Greiner
# jgreiner@ucsc.edu
# Assignment 8

import random

SPACE = '  '
EMPTY = '.'
HEALTHY = 0  # Occupied
ZOMBIE = 1  # Infected


def create_empty_grid(cell_dim):
    """ Creates an empty grid. """

    grid = dict()
    for x in range(0, cell_dim):
        for y in range(0, cell_dim):
            grid[(x,y)] = EMPTY
    return grid


def check_probability(value):
    if random.random() < value:
        return True
    else:
        False


def print_grid(cell_dim, grid, day):
    """ Prints current grid line by line to standard out. """
    print '\nDay: ' + str(day) + '\n'
    for x in range(cell_dim):
        grid_for_print = ''
        for y in range(cell_dim):
            grid_for_print += str(grid[(x, y)])
            grid_for_print += ' '
        print grid_for_print


def init_grid(cell_dim, density, disease):
    empty_grid = create_empty_grid(cell_dim)
    for x in range(cell_dim):
        for y in range(cell_dim):
            if check_probability(density) == True:
                if check_probability(disease) == True:
                    empty_grid[(x, y)] = ZOMBIE
                else:
                    empty_grid[(x, y)] = HEALTHY
            else:
                empty_grid[(x, y)] = EMPTY
    print_grid(cell_dim, empty_grid, 0)


def compute3x3(loc, grid, new_grid, birth_chance, spread_chance, disease_duration, mortality_rate):
    """ Births and Disease Spread """
    #  Birth Chance
    for x in range(loc[0]-1, loc[0]+2):
        for y in range(loc[1]-1, loc[1]+2):
            if (x, y) != loc:  # Look only at cells around center cell
                print loc
                # try:
print compute3x3()


def sim(grid_size, pop_density, disease, birth, spread, duration, mortality, days):
    init_grid(grid_size, pop_density, disease)


def main():
    sim(20, 0.15, 0.1, 0.1, 0.1, 3, 0.5, 500)

if __name__ == '__main__':
    main()