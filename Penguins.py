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
