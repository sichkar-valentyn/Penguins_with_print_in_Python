# File: Penguins.py
# Description: Function for modifying lists with remove and count methods
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Drawing penguins with the help of print function in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Penguins_with_print_in_Python (date of access: XX.XX.XXXX)




# Implementing the task
# Showing of desired number of penguins

# Entering number of penguins we need to show
number = int(input())


# Creating a function to show 'n' penguins
def penguin(n):
    for i in range(n):
        print('   _~_   ', end=' ')
    print()
    for i in range(n):
        print('  (o o)  ', end=' ')
    print()
    for i in range(n):
        print(' /  V  \\ ', end=' ')
    print()
    for i in range(n):
        print('/(  _  )\\', end=' ')
    print()
    for i in range(n):
        print('  ^^ ^^  ', end=' ')


# Showing the results
penguin(number)
