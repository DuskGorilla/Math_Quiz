# checks user if they enter yes (y) or no (n)

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

Your goal is to try to guess and answer the math equations right 
with no wrong answers.

 Good luck.

    """)


# Main routine
print()
print("🎶🎶🎶Welcome to my very Hard Math Quiz🎶🎶🎶")
print()

# loop to test

want_instructions = yes_no("Do you want to see the instructions? ")

# check if they use yes or no
if want_instructions == "yes":
    instructions()

print()
print("Program continues")
