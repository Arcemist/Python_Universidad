import random

def A():
    print("A")

def B():
    print("B")

selection = random.randrange(5)

if selection <= 1:
    A()
else:
    B()
