import random
from replit import clear
from art import logo

print(logo)

# System generates number for player to guess
def generate_number():
  number = range(1, 101)
  selected_number = random.choice(number)
  return selected_number


# Player chooses difficulty
def difficulty_setting():
  attempts = 0
  choose_difficulty = input('Choose a difficulty. Type "easy" or "hard" ').lower()
  if choose_difficulty == 'easy':
      attempts = 10
  else:
    attempts = 5
  return attempts


def playing():
  # Player starts game 
  print('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.\n')
  
  num_to_guess = generate_number()
  num_of_attempts = difficulty_setting()
  previous_attempts = []
  game_in_play = True
    
  while num_of_attempts > 0 and game_in_play:
    print(f'You have {num_of_attempts} attempts to guess the number.')
    player_guess = int(input('Make a guess: '))
    if player_guess in previous_attempts:
      print(f'You have already guessed {player_guess}. Try again.\n')
    elif player_guess > num_to_guess:
      print('Too high\n')
      num_of_attempts -= 1
      previous_attempts.append(player_guess)
    elif num_to_guess > player_guess:
      print('Too low\n')
      num_of_attempts -= 1
      previous_attempts.append(player_guess)
    elif num_to_guess == player_guess:
      print(f'You got it! The answer is {num_to_guess}.\n')
      game_in_play = False
    
    if num_of_attempts == 0:
      print(f'Game over. The correct number is {num_to_guess}.')
      game_in_play = False

while input('\nDo you want to play Guess the Number? Type "Y" or "N": ').upper() == "Y":
  clear()
  print(logo)
  playing()
else:
  print('Next time then.')