import random
 
def main():
    player_wins = 0
    computer_wins = 0
 
    # This loop will run the game 5 times that count
    # and keep track of how many wins.
    # There must be a winner who wins five times
    while player_wins != 5 and computer_wins != 5:
 
        # Computer chooses a random number.
        comp_number = random.randint(1, 3)
 
        # Initialize value of comp_choice variable
        # corresponding to the comp_number value.
        if comp_number == 1:
            comp_choice = 'Rock'
        elif comp_number == 2:
            comp_choice = 'Paper'
        else:
            comp_choice = 'Scissor'
 
        # User enter their numeric choice from a menu.
        user_number = int(input('Enter 1 for rock, 2 paper, 3 scissors: '))
 
        # Check user's input using a validation loop.
        while user_number > 3 or user_number < 1:
            print('Please choose a value of 1, 2, or 3')
            print()
            user_number = int(input('Enter 1 for rock, 2 paper, 3 scissors: '))
 
        # Get the value in string.
        choice_string = choiceString(user_number)
 
        # Get the computer's and user's choices.
        rock_paper_scissors = rockPaperScissors(comp_choice, choice_string)
 
        # Display user's choice
        print('You chose ' + choice_string)
 
        # Display computer's choice
        print('Computer chose ' + comp_choice)
 
        # Determine and display who wins this game
        # Calculate computer's and user's score
        if rock_paper_scissors == 1:
            print('The computer wins the game')
            print()
            computer_wins = computer_wins + 1
        elif rock_paper_scissors == 2:
            print('You win the game')
            print()
            player_wins = player_wins + 1
        elif rock_paper_scissors == 0:
            print ('You made the same choice as computer. Starting over')
            print ()

    # Display score
    print('After 5 runs, the totals are:')
    print('You\t', player_wins)
    print('Computer', computer_wins)
main ()

# The choiceString function receives the choice number
# and returns that value in string
def choiceString (choice):
    if choice == 1:
        return 'Rock'
    elif choice == 2:
        return 'Paper'
    else:
        return 'Scissor'
   
# The rockPaperScissors function receives numbers
# representing the computer's and player's choices.
def rockPaperScissors (computer, player):
    if (player == 'Rock' and computer == 'Scissor'):
        return 2
    elif (player == 'Scissor' and computer == 'Paper'):
        return 2
    elif (player == 'Paper' and computer == 'Rock'):
        return 2
    elif (computer == 'Rock' and player == 'Scissor'):
        return 1
    elif (computer == 'Scissor' and player == 'Paper'):
        return 1
    elif (computer == 'Paper' and player == 'Rock'):
        return 1
    elif (computer == 'Rock' and player == 'Rock'):
        return 0
    elif (computer == 'Paper' and player == 'Paper'):
        return 0
    elif (computer == 'Scissor' and player == 'Scissor'):
        return 0      
           
      
