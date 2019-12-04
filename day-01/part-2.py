#!/usr/bin/python
#
# Day 01, part 2

import math

def fuel_req(mass, fuel):
    mass = int(math.floor(int(mass) / 3) - 2)
    if mass <= 0:
        return fuel
    else:
        return fuel_req(mass, fuel+mass)

def main ():
    f = open("input.txt", "r")
    lines = f.readlines()

    fuel = 0
    for line in lines:
        # print(int(line))
        fuel += fuel_req(line, fuel)

    print(int(fuel))

if __name__== "__main__":
  main()
