import random

#word magic
def updatedisplay(recent,theword,displayword):
  result = ""
  for k in range(len(displayword)):
    if recent == theword[k]:
      result += recent
    else:
      result += displayword[k]
  return result
#main code
print("guess my super secret word, you may make 5 mistakes")
mistake = 5
secretwords = ["lung","catapult","shop","pizza","pineapple","superlongpeiceoftextlolololololololololololololololololololololololololololololololol","thequickbrownfoxjumpedoverthelazydog"]
value = random.randint(0,6)
theword = secretwords[value]
displayword = "_" * len(theword)
guessed = []
while True:
  print("you have",mistake,"mistakes left")
  print("guessed letters",guessed,)
  print(displayword)
  guess = input("guess one letter here: ")
  if len(guess) > 1:
    print("ONE LETTER AT A TIME!!!")
    continue
  if guess in guessed:
    print("you already guessed that")
    continue
  if guess in theword:
    print("correct, good job")
    guessed.append(guess)
    displayword=updatedisplay(guess,theword,displayword)
    if displayword == theword:
      print(theword)
      print("you found the word good job")
      break
    continue
  if guess not in theword:
    print("incorrect")
    guessed.append(guess)
    mistake = mistake - 1
    if mistake == 0:
      print("you lost, the word was",theword)
      break
    continue