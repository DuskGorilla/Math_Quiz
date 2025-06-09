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
            return "10_rounds"

        try:
            response = int(response)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main routine starts


# initialise quiz variables
mode = "10_rounds"
rounds_played = 0
rounds_lost = 0
rounds_won = 0
feedback = ""
quiz_history = []
all_scores = [0]
answered_right = 0
answered_wrong = 0


# Ask user for number of rounds or 10 round mode
num_rounds = int_check("How many rounds would you like? Push enter for 10 rounds")

if num_rounds == "10_rounds":
    mode = "10_rounds"
    num_rounds = 10

# Game loop starts here

while rounds_played < num_rounds:

    # Round headings
    if mode == "10_rounds":
        rounds_heading = f"\n👍👍👍 Question {rounds_played + 1} of {num_rounds} 👍👍👍"
    else:
        rounds_heading = f"\n✌️✌️✌️ Question {rounds_played + 1} of {num_rounds} ✌️✌️✌️"

    print(rounds_heading)



    number1 = random.randint(1, 5)
    number2 = random.randint(1, 10)
    question = int_check(f"What is {number1} + {number2} =")
    answer = number2 + number1
    if question == answer:
        print(f"YAY You got it correct! 👍👍 {answered_right + 1}")
        answered_right += 1

    else:
        print(f"Sorry? You got it wrong... 👎👎 {answered_wrong + 1}")
        answered_wrong += 1

    # Give user their feedback with the question and answer
    if question == answer:
        feedback = f"Nice, You got it correct this was your answer {number1} + {number2} = {answer}"

    else:
        feedback = f"Aw, Too bad you got it wrong here's the actual answer {number1} + {number2} = {answer}"



    rounds_played += 1

# Quiz History
    history_feedback = f"Round {rounds_played}: {feedback}"
    quiz_history.append(history_feedback)

    all_scores.append(answer)

if rounds_played > 0:
    # Calculate Statistics
    rounds_won = all_scores[0]
    rounds_lost = all_scores[0]
    print(f"you answered {rounds_played} questions")
    print(f"you got wrong {answered_wrong} questions")
    print(f"you got right {answered_right} questions")


    # ask user if they want to see their game history and output if requested
    see_history = yes_no("\nDo you want to see your quiz history? ")
    if see_history == "yes":
        for item in quiz_history:
            print(item)


    print()
    print("Thanks for playing.")