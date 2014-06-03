__author__ = 'jgreiner'
# Jonathon Greiner
# jgreiner@ucsc.edu
# Assignment 8

import random

SPACE = '  '
EMPTY = '.'
HEALTHY = 0  # Occupied
ZOMBIE = 1  # Infected


def createEmptyGrid(cell_dim):
    """ Creates an empty grid. """

    grid = dict()
    for x in range(0, cell_dim):
        for y in range(0, cell_dim):
            grid[(x,y)] = EMPTY
    return grid


def checkProbability(value):
    if random.random() < value:
        return True
    else:
        False


def printGrid(cell_dim, grid, day):
    """ Prints current grid line by line to standard out. """
    print '\nDay: ' + str(day) + '\n'
    for x in range(cell_dim):
        grid_for_print = ''
        for y in range(cell_dim):
            grid_for_print += str(grid[(x, y)])
            grid_for_print += ' '
        print grid_for_print


def initGrid(cell_dim, density, disease):
    emptyGrid = createEmptyGrid(cell_dim)
    for x in range(cell_dim):
        for y in range(cell_dim):
            if checkProbability(density) == True:
                if checkProbability(disease) == True:
                    emptyGrid[(x, y)] = ZOMBIE
                else:
                    emptyGrid[(x, y)] = HEALTHY
            else:
                emptyGrid[(x, y)] = EMPTY
    printGrid(cell_dim, emptyGrid, 0)


def sim(grid_size, pop_density, disease, birth, spread, duration, mortality, days):
    initGrid(grid_size, pop_density, disease)


def main():
    sim(20, 0.15, 0.1, 0.1, 0.1, 3, 0.5, 500)

if __name__ == '__main__':
    main()