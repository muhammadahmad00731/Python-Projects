dict1 = {
1 : "stone",
2 : "paper",
3 : "ceaser"
}
while True:
    a = int(input("\nPress 0 to quit\nPress 1 for stone \n 2 for paper \n 3 for ceaser : "))
    import random
    b = random.randrange(1,4)
    if(a == 0):
        break
    elif(a ==1 and b == 1):
        print(f"Computer choose {dict1[1]}")
        print("again")
    elif(a ==1 and b == 2):
        print(f"Computer choose {dict1[2]}")
        print("Computer wins!")
    elif(a ==1 and b == 3):
        print(f"Computer choose {dict1[3]}")
        print("You win!")

    elif(a ==2 and b == 1):
        print(f"Computer choose {dict1[1]}")
        print("You win!")
    elif(a ==2 and b == 2):
        print(f"Computer choose {dict1[2]}")
        print("Again")
    elif(a ==2 and b == 3):
        print(f"Computer choose {dict1[3]}")
        print("Computer wins!")

    elif(a ==3 and b == 1):
        print(f"Computer choose {dict1[1]}")
        print("Computer wins!")
    elif(a ==3 and b == 2):
        print(f"Computer choose {dict1[2]}")
        print("You win!")
    elif(a ==3 and b == 3):
        print(f"Computer choose {dict1[3]}")
        print("Again")
    else:
        print("Invalid Input")