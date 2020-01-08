#!/usr/bin/python
#
# Day 02, part 1

# 1 adds together numbers read from two positions and stores the result in a third position.
# 2 multiplies
# => move to the next one by stepping forward 4 positions
# 99 stop

def main ():
    for line in open('input.txt'):
        array = line.split(",")

    array = list(map(int, array))
    array[1] = 12
    array[2] = 2
    step = 0

    while array[step] != 99:
        val_1 = array[array[step+1]]
        val_2 = array[array[step+2]]
        if array[step] == 1:
            array[array[step+3]] = val_1 + val_2
            step = step+4
            continue
        elif array[step] == 2:
            array[array[step+3]] = val_1 * val_2
            step = step+4
            continue
        continue

    print(str(array))

if __name__== "__main__":
  main()
