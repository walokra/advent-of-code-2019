#!/usr/bin/python
#
# Day 01, part 1

import math

def main ():
    f = open("input.txt", "r")
    lines = f.readlines()

    fuel = 0
    for line in lines:
        fuel += math.floor(int(line) / 3) - 2

    print(int(fuel))

if __name__== "__main__":
  main()
