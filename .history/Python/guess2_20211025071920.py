import math
import random
print('Welcome To The Number Guessing Game')
print('Please Guess A Number From 0 - 100:')
#Create a random number from 0 to 100
rand_num = random.randint(0, 100)
max_guesses = round(math.log(100 - 0 + 1, 2))
print("You have",max_guesses,"chances to guess the number!\n")
# Create a variable to count the number of guesses.
count = 0

while True :
  #Increment count
  count = count + 1 
  
  #Check if count is more than the number of turns given
  if count > max_guesses:
    print("You've exceeded the number of guesses.")
    print("The number was, rand_num")
    break;
  player_guess = int(input('Please Guess A Number From 0 - 100:'))
  if player_guess == rand_num:
    print("You guessed the number in",count,"turn(s) !")
    break;
  elif player_guess < rand_num:
    print("The number is higher")
  elif player_guess > rand_num:
    print("The number is lower")

     