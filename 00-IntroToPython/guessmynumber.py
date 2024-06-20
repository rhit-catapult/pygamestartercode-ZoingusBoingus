import random

print("Guess My Super Secret Number")
print("The Number is Somewhere Betwen 1 and 100")
secretnumber = random.randint(1,100)
guesses = 0
print("Make your Choice")

while True:
  guesses = guesses+1
  guess = int(input('I guess '))
  if guess > secretnumber:
    print(guess, "is too high Try Again")
  if guess < secretnumber:
    print(guess, "is too low Try Again")
  if guess == secretnumber:
   break
  if guesses > 20: print("Woah Woah Woah, slow down and think about it a little bit at least")
if guess != 1:
  print("Good Job! it only took you" ,guesses, "guesses")
if guesses == 1:
  print("Lucky Guess")