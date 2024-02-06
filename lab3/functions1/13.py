from random import randrange 

def low():
    print("Your guess is too low.")
def high():
    print("Your guess is too high.")

print("Hello! What is your name?")
name = input()

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
random_number = randrange(1, 21)

cnt = 0

while True:
    cnt+=1
    num = int(input("Take a guess: \n"))
    if num == random_number:
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        break

    elif num < random_number and num <= 20:
        low()

    elif num > random_number and num <= 20:
        high()


    #Дополнительное условие если ввели число больше 20    
    elif num > 20:
        print("Guess in range 1 and 20")
