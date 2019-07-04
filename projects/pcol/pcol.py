#! /usr/bin/env python3

import argparse
import sys

# Setting up argument parser
parser = argparse.ArgumentParser(prog='pcol', usage='pcol <number/s>',
                                 description='''This script is used to display
                                 columns onto standard output from the table
                                 which shall be fed from standard input.''')
parser.add_argument('integer', nargs='+', type=int, help='''Enter the column
                    number you wish to display''', choices=range(1, 11))
args = parser.parse_args()


# Objects to store the input
store = []
big_store = []


def get_data():
    """
    This function reads the data from standard input and puts it into store
    and big_store which act as buffers.
    """
    for line in sys.stdin:
        store.append(line)
    for line in store:
        big_store.append(line.split())


# Calling the function to store the data
get_data()


def width_return(column):
    """
    This function reads the data in each column and determines the optimal
    width required to print the data in the column.
    """
    # Set the width to zero as default
    width = 0
    # Go through each line
    for line_list in big_store:
        # Check the width of respective column for maximum value
        if len(line_list[column]) > width:
            width = len(line_list[column])
    # Return the maximum value
    return width


def pcol():
    """
    This function is main function. It reads the arguments from the argument
    parser, and prints out the data in each column number given as argument.
    """
    for row in range(len(store)):
        for column in args.integer:
            # Printing the data with right alignment. Noted that column-1 is
            # for human based arguments, where when user wants 1st column,
            # he will put 1 as argument. However, as python indexes work
            # 1st column will be represented by 0.
            print("{0:>{width}}".format(big_store[row][column-1],
                                        width=width_return(column-1)),
                  end="  ", sep="  ")
        # Moving to new line after each row is finished.
        print()


# Calling pcol main function
if __name__ == "__main__":
    pcol()
