import random

print("Random Number Guesser From 1 - 10")

answer = random.randint(1,100)
print(f"(The answer is {answer})")

while True:
  print("Enter a number:")
  user_input = input()
  if user_input.isdigit():
    if int(user_input) >= 1 and int(user_input) <= 100:
      user_input = int(user_input)
      while user_input != answer:
          if user_input < answer:
            print("Too low")
            user_input = int(input())
          else:
            print("Too high")
            user_input = int(input())

      print("You won")
      break
    else:
      print("Please Enter A Number Between The Range Of 1 and 100. Try again.")
  else:
    print("Please Enter A Number. Try again")
    
  
