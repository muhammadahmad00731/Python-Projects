import random
def bowling():

    print("It's Your Bowling🥎\n")
    user_target = 0
    total_comp_score = 0

    for balls in range(1,7):
        user_score = int(input("Enetr number b\w 1-6 : "))
        comp_score = random.randint(0,6)
        print(f"Computer enter {comp_score}")

        if(comp_score == user_score):
            print("Computer is out.")
            break
        else:
            if(type(user_score) == int and user_score <= 6):
                total_comp_score += comp_score
            else:
                balls -= 1

    print("Computer Batting Ended.")
    print(f"Computer Score = {total_comp_score}")
    print(f"Your Target = {total_comp_score + 1}")
    print("\nIt's your Batting🏏\n")
#++++++++++++++++++++++++++++++++++++++++++++++++++++
    total_user_score = 0

    for balls in range(1,7):
        user_score = int(input("Enetr number b\w 1-6 : "))
        comp_score = random.randint(0,6)
        print(f"Computer enter {comp_score}")
        if(comp_score == user_score):
            print("You are out🤬")
            break
        else:
            if(type(user_score) == int and user_score <= 6):
                total_user_score += user_score
            else:
                balls -= 1

    print(f"Your Score = {total_user_score}")

    if(total_user_score > total_comp_score):
        print("You Win 😎")
    elif(total_user_score == total_comp_score):
        print("Match Tie 🥱")
    else:
        print("You loose 😖\n")
#_______________________________________________________________________________
def batting():
    print("You are Batting🏏")

    total_user_score = 0
    comp_target = 0

    for balls in range(1,7):
        user_score = int(input("Enetr number b\w 1-6 : "))
        comp_score = random.randint(0,6)
        print(f"Computer enter {comp_score}")

        if(comp_score == user_score):
            print("You are out🤬")
            break
        else:
            if(type(user_score) == int and user_score <= 6):
                total_user_score += user_score
            else:
                balls -= 1

    print("User Batting Ended.")
    print(f"User Score = {total_user_score}")
    print(f"Computer Target = {total_user_score + 1}")
    print("It's Computer Bowling🥎\n")
#++++++++++++++++++++++++++++++++++++++++++++++++++++
    total_comp_score = 0

    for balls in range(1,7):
        user_score = int(input("Enetr number b\w 1-6 : "))
        comp_score = random.randint(0,6)
        print(f"Computer enter {comp_score}")
        if(comp_score == user_score):
            print("Computer is out.")
            break
        else:
            if(type(user_score) == int and user_score <= 6):
                total_comp_score += comp_score
            else:
                balls -= 1
    print(f"Computer Score = {total_comp_score}")

    if(total_user_score > total_comp_score):
        print("You Win 😎")

    elif(total_user_score == total_comp_score):
        print("Match Tie 🥱")

    else:
        print("You loose 😖\n")

user_choice = int(input("Enter 1 for batting🏏 or 0 for bowling🥎 : "))
if(user_choice == 0):
    bowling()
elif(user_choice == 1):
    batting()
else:
    print("Invalid input😡")