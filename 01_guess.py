import random

five_letter_words = ["lucas", "dough", "melon", "cards"]
length = len(five_letter_words) - 1
answer_index = random.randint(0, length)
answer = five_letter_words[answer_index]
counter = 10

# while loop
# if statementthat compares user input to the answer
# counter that stops at 10

print("The five letter word starts with " + str(answer[0]) + "\nGood Luck guessing!")

while 1:
    user_input = input()
    if user_input.lower() == answer.lower():
        print("Good Job! You are one with the Source!")
        exit()

    elif (len(user_input) == 0):
        print("You wasted a guess =P")
        counter -= 1

    elif (len(user_input) > 5) or (len(user_input) < 5):
        print("0, 1, 2, 3, 4 is how we count to five!")
        counter -= 1

    elif user_input[0] != answer[0]:
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    elif user_input != answer:
        counter -= 1
        print("You have " + str(counter) + " guesses left!")

    if counter == 0:
        print("You lost! The correct answer was " + answer)
        exit()
