# ## Project VI: Scrabble Word Score Calculator

# Let's build an interactive Scrabble scoring system that calculates points for words and tracks player scores!

# ### Project Overview

# In this engaging project, we'll create a scoring system for a group of friends playing Scrabble. Using Python dictionaries, we'll organize and track players, their words, and corresponding points.

# We'll work with two important lists:

# - 📝 `letters`: Contains all uppercase letters (A-Z)
# - 🎯 `points`: Contains corresponding point values

# Our goal is to combine these lists into a dictionary that maps each letter to its Scrabble point value.

# ### Step 1: Create Letter-Points Dictionary

# Using Python's list comprehension and `zip`, we'll create `letter_to_points` to map letters to their point values. Don't forget to account for blank tiles (worth 0 points)!

# ### Step 2: Word Scoring System

# We'll develop a scoring function that calculates points for any given word:

# - Create `score_word` function with `word` parameter
# - Initialize `point_total` to track score
# - Loop through letters and sum up points
# - Handle missing letters (assign 0 points)

# Let's test with the word "BROWNIE" which should score 15 points:

### Step 3: Game Score Tracking

# Now we'll track scores for multiple players:

# | 📝 player1 | 🎲 wordNerd | 📚 Lexi Con | 👨‍🏫 Prof Reader |
# | --- | --- | --- | --- |
# | BLUE | EARTH | ERASER | ZAP |
# | TENNIS | EYES | BELLY | COMA |
# | EXIT | MACHINE | HUSKY | PERIOD |

# To implement the scoring system:

# - Create `player_to_words` dictionary mapping players to their words
# - Initialize empty `player_to_points` dictionary
# - Calculate total points for each player's words
# - Store final scores in `player_to_points`


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters,points)}
letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for x in word:
    point_total += letter_to_points.get(x, 0) 
  return point_total

brownie_points = score_word("BROWNIE")
# print(brownie_points)


player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

player_to_points ={}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print(player_to_points)
























