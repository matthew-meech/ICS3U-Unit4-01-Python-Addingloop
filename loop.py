#!/usr/bin/env python3

# Created by: Matthew Meech
# Created on: Sep 2021
# This program uses a while loop


def main():
    # this function uses a while loop

    # this is to keep track of hw many times you go through the loop
    loop_counter = 0

    # input
    print("\n", end="")
    positive_integer = int(input("enter a postive inetger: "))

    # process & output
    print("\n", end="")
    while loop_counter < positive_integer:
        print("{0} time through loop.".format(loop_counter))
        loop_counter = loop_counter + 1


if __name__ == "__main__":
    main()
