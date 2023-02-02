import os
import random

n = int(input("Enter a number: "))
array = []
summ = 0

try:
    for i in range(n):
        array.append(random.randint(-n, n))
        print(array[i], end=" ")

    print("\n")

    file = open('Numbers.txt', 'r')

    while True:
        line = file.readline()
        if not line:
            break

        summ += array[int(line)]
        print(summ, end=" ")

    print("\n")
    print("Result = " + str(summ))
except IndexError:
    print("list index out of range")




