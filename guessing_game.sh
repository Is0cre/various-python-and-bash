#!/bin/bash
# Generate a random number between 1 and 10
secret=$(($RANDOM % 10 + 1))
# Set the number of guesses to 0
guesses=0
echo "Welcome to the number guessing game!"
echo "I'm thinking of a number between 1 and 10. Can you guess what it is?"
while true; do
  # Increment the number of guesses
  ((guesses++))
  # Read the user's guess
  read -p "Enter your guess: " guess
  # Check if the guess is correct
  if [[ $guess -eq $secret ]]; then
    echo "Congratulations, you guessed the correct number in $guesses guesses!"
    break
  fi
  # Give the user a hint
  if [[ $guess -lt $secret ]]; then
    echo "Your guess is too low. Try again!"
  else
    echo "Your guess is too high. Try again!"
  fi
done
