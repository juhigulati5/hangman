import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"

temp =[]

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in temp:
      print("You've already guessed that letter.")
    else:
      temp.extend(guess)
      
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter

      print(f"{' '.join(display)}")

      if "_" not in display:
          end_of_game = True
          print("\nYou win.")
        
      if guess not in chosen_word:
          print(f"{guess} is not in the word. You lose a life.")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print(f"\nYou lose. The word was {chosen_word}")
          
      print(stages[lives])

      
