from random import randint
def generateRandom():
    n=randint(1,100)
    return n

g=generateRandom()
while True:
    n=int(input("Guess number: "))
    if n<g:
        print("Too little")
    elif n>g:
        print("Too much")
    else:
        print("You guessed!")
        break