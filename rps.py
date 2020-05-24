import random

# Create global constant
COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3
ROCK = 1
PAPER = 2
SCISSORS = 3
 
# Value returning function that takes in the argument choice 
# (the number representing rock, paper, or scissors) 
# and return as strings
def choiceString(choice):
	if choice == ROCK:
		return 'Rock'
	if choice == PAPER:
		return 'Paper'
	if choice == SCISSORS:
		return 'Scissors'
	else:
		return 'Something went wrong'

# This function takes in integers of choice as arguments,
# returns one of the following values: 
# TIE, PLAYER_WINS, COMPUTER_WINS, INVALID	
def rockPaperScissors(computer, player):
	if (player == ROCK and computer == SCISSORS):
		return PLAYER_WINS
	elif (player == SCISSORS and computer == PAPER):
		return PLAYER_WINS
	elif (player == PAPER and computer == ROCK):
		return PLAYER_WINS
	elif (computer == ROCK and player == SCISSORS):
		return COMPUTER_WINS
	elif (computer == SCISSORS and player == PAPER):
		return COMPUTER_WINS
	elif (computer == PAPER and player == ROCK):
		return COMPUTER_WINS
	elif (computer == ROCK and player == ROCK):
		return TIE
	elif (computer == PAPER and player == PAPER):
		return TIE
	elif (computer == SCISSORS and player == SCISSORS):
		return TIE
	else:
		return INVALID   

def main():
 # 0 is a placeholder and will not be used.
	player_wins = 0
	computer_wins = 0
 
 # This loop will run the game 5 times that count
 # and keep track of how many wins.
 # There must be a winner who wins five times
	while player_wins != 5 and computer_wins != 5:
 
		# Computer chooses a random number.
		computer = random.randint(1, 3)

		# User enter their numeric choice from a menu.
		player = int(input('Enter 1 for rock, 2 paper, 3 scissors: '))
  
  # Check user's input using a validation loop.
		while player > 3 or player < 1:
			print('Please choose a value of 1, 2, or 3')
			print()
			player = int(input('Enter 1 for rock, 2 paper, 3 scissors: '))
 
		# Call choiceString(choice) function to print the player’s hand
		playerString = choiceString(player)
		print('Player chose:',playerString)

		# Call choiceString(choice) function to print the computer’s hand
		computerString = choiceString(computer)
		print('Computer chose:',computerString)
  
  # Call your value returning function rockPaperScissors(computer, player)
		# to get the result of the round between the computer and player.
		result = rockPaperScissors(computer, player)
  
  # Show player if the result is tie
		if result == TIE:
			print('You made the same choice as the computer. Starting over\n')
		# Declare if the computer is the winner
		elif result == COMPUTER_WINS:
			print('The computer wins the game\n')
			computer_wins = computer_wins + 1
		# Declare if the player is the winner
		elif result == PLAYER_WINS:
			print('The player wins the game\n')
			player_wins = player_wins + 1
		# Declare invalid input
		elif result == INVALID:
			print('You made an invalid choice. No winner\n')
 # Display score
	print('After 5 runs, the totals are:')
	print('You\t', player_wins)
	print('Computer', computer_wins)

# Call the main function
main ()
