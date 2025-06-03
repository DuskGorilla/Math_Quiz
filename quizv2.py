import random


def yes_no(question):
    while True:
        response = input(question).lower()

        # checks the users response, question
        # repeat if the user does not enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no ")


def instructions():
    print("""
*** Instructions ***
To begin, choose number of rounds to be given a set of 
questions that are math equations.

Then choose how many rounds you'd like to play <enter> 
for infinite mode.

Your goal is to try to guess and and answer the math equations right

 Good luck.

    """)


print("🎶🎶🎶Welcome to my very Hard Math Quiz🎶🎶🎶")
print()

want_instructions = yes_no("Do you want to see the instructions? ")

# check if they use yes or no
if want_instructions == "yes":
    instructions()


# checks for an integer more than 0 (allow <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        response = input(question)

        # check for infinite mode
        if response == "":
            return "infinite"

        try:
            response = int(response)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

def quiz_answers(number1,number2):



# Main routine starts

for x in range(12):
    number1 = random.randint(1, 5)
    number2 = random.randint(1, 10)
    print("What is", number1, "+", number2, "=")

    users_answer = int(input(""))
    answer = number2 + number1
    if users_answer == answer:
        print("YAY You got it correct! 👍👍")
        score += 1
    else:
        print("Sorry? You got it wrong... 👎👎")
print("Your exact score is: ", score)