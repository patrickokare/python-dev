## Project I: Magic 8-Ball

# Create a Python program that answers "Yes" or "No" questions with random fortunes.

### Project Requirements

# Build a [magic8.py](http://magic8.py) program that generates different responses each time it runs. The program should:

# - Accept a user's name and question
# - Randomly select from 9 possible answers:

# <aside>

# - Positive Responses:
#     - `Yes - definitely`
#     - `It is decidedly so`
#     - `Without a doubt`
# - Neutral Responses:
#     - `Reply hazy, try again`
#     - `Ask again later`
#     - `Better not tell you now`
# - Negative Responses:
#     - `My sources say no`
#     - `Outlook not so good`
#     - `Very doubtful`
# </aside>

import random

name = 'John'
question = "Will I win the lottery? "
answer = ""

# Generate random number between 1-9
random_number = random.randint(1, 9)

# Assign fortune based on random number
if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"

# Handle output based on input conditions
if question == "":
    print("Question Cannot be empty!")
elif name == "":
    print('Question:', question)
    print("Magic 8-Ball's answer:", answer)
else:
    print(name, 'asks:', question)
    print("Magic 8-Ball's answer:", answer)