points = 0

print("Do you want to play this multiple choice game? (y/n)")

while True:
    user_play = input()

    if user_play.lower() == "y":
        print('''\nQuestion 1: What is the Square Root of 9?
  A) 3 
  B) 4
  C) 5
  D) 2''')
        while True:
            user_ans1 = input("Enter your answer (A/B/C/D): ")
            if user_ans1.upper() in ["A", "B", "C", "D"]:
                if user_ans1.upper() == "A":
                    points += 1
                break
            else:
                print("You have entered an invalid value (A/B/C/D)")

        # Question 2

        print('''\nQuestion 2: 9 + 6 = ?
  A) 13
  B) 14
  C) 15 
  D) 17''')
        while True:
            user_ans1 = input("Enter your answer (A/B/C/D): ")
            if user_ans1.upper() in ["A", "B", "C", "D"]:
                if user_ans1.upper() == "C":
                    points += 1
                break
            else:
                print("You have entered an invalid value (A/B/C/D)")

        # Question 3

        print('''\nQuestion 3: What is a verb?
  A) A person, place or thing. 
  B) Something used to describe something else.
  C) An identifier, i.e, He, she, they, etc.
  D) An action word ''')
        while True:
            user_ans1 = input("Enter your answer (A/B/C/D): ")
            if user_ans1.upper() in ["A", "B", "C", "D"]:
                if user_ans1.upper() == "D":
                    points += 1
                break
            else:
                print("You have entered an invalid value (A/B/C/D)")

        # Question 4

        print('''\nQuestion 4: Which nations are currently at war?
  A) The USA and Canada
  B) Russia and Ukraine 
  C) North Korea and Israel 
  D) Britain and Japan''')
        while True:
            user_ans1 = input("Enter your answer (A/B/C/D): ")
            if user_ans1.upper() in ["A", "B", "C", "D"]:
                if user_ans1.upper() == "B":
                    points += 1
                break
            else:
                print("You have entered an invalid value (A/B/C/D)")

        # Question 5

        print('''\nQuestion 5: Which body part is the nervous system focused on?
  A) The heart
  B) The kidneys
  C) The brain 
  D) The reproductive organs''')
        while True:
            user_ans1 = input("Enter your answer (A/B/C/D): ")
            if user_ans1.upper() in ["A", "B", "C", "D"]:
                if user_ans1.upper() == "C":
                    points += 1
                break
            else:
                print("You have entered an invalid value (A/B/C/D)")

        # Question 6

        print('''\nQuestion 6: Which of these compounds are a base?
  A) NaOH 
  B) NaCl 
  C) C6H12O6
  D) HCl''')
        while True:
            user_ans1 = input("Enter your answer (A/B/C/D): ")
            if user_ans1.upper() in ["A", "B", "C", "D"]:
                if user_ans1.upper() == "A":
                    points += 1
                break
            else:
                print("You have entered an invalid value (A/B/C/D)")

        # Question 7

        print('''\nQuestion 7: What is the derivative of 3x^4 + e^x?
  A) 6x^2 + e^x
  B) 12x^3 + xe^x
  C) 3x^4 + ln(e)
  D) 12x^3 + e^x''')
        while True:
            user_ans1 = input("Enter your answer (A/B/C/D): ")
            if user_ans1.upper() in ["A", "B", "C", "D"]:
                if user_ans1.upper() == "D":
                    points += 1
                break
            else:
                print("You have entered an invalid value (A/B/C/D)")

        # Question 8

        print('''\nQuestion 8: Which datatype makes a word in Java?
A) Int
B) String 
C) Char
D) Boolean''')
        while True:
            user_ans1 = input("Enter your answer (A/B/C/D): ")
            if user_ans1.upper() in ["A", "B", "C", "D"]:
                if user_ans1.upper() == "B":
                    points += 1
                break
            else:
                print("You have entered an invalid value (A/B/C/D)")

        # Question 9

        print('''\nQuestion 9: Batman is from which franchise?
A) Marvel
B) DC 
C) Star Wars
D) Harry Potter''')
        while True:
            user_ans1 = input("Enter your answer (A/B/C/D): ")
            if user_ans1.upper() in ["A", "B", "C", "D"]:
                if user_ans1.upper() == "B":
                    points += 1
                break
            else:
                print("You have entered an invalid value (A/B/C/D)")

        # Question 10

        print('''\nQuestion 10: Which religion classifies Jesus (Isa) as God?
A) Judaism
B) Christianity 
C) Islam
D) Hinduism''')
        while True:
          user_ans1 = input("Enter your answer (A/B/C/D): ")
          if user_ans1.upper() in ["A", "B", "C", "D"]:
              if user_ans1.upper() == "B":
                  points += 1
              break
          else:
              print("You have entered an invalid value (A/B/C/D)")

        score = points /10
        print("You got: " + str(points) + "/10")
        if points >5:
          print("Congratulations, you pass.")
        else:
          print("You have failed the quiz.")

    elif user_play.lower() == "n":
        print("")
        break

    else:
        print("Please Enter A Valid Input")
