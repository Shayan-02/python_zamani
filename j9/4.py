import random


def my_function(*child):
    a = random.randint(0, 4)
    print("The youngest child is " + child[a])

my_function("Emil", "Tobias", "reza", "Linus", "john")
