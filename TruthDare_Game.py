while True:
    a = input("\nPlease press \'T\' to select Truth\n and Press \'D\' to select dare\n and Press \'Q\' to quit :")
    print("\n")
    ##print(a)
    if(a == "q" or a == "Q"):
        break
    elif(a == "t" or a == "T"):   #TRUTH
        import random
        b = random.randrange(1,5)
        if(b==1):
            print("What is the most embarrassing thing you’ve ever done?") #1
        elif(b==2):
            print("Have you ever broken something and blamed someone else?") #2
        elif(b==3):
            print("What’s the weirdest dream you've ever had?") #3
        elif(b==4):
            print("What’s the most childish thing you still do?") #4
        elif(b==5):
            print("Who do you have a crush on right now?") #5

    elif(a == "d" or a == "D"):  #DARE
        import random
        b = random.randrange(1,5)
        if(b==1):
            print("Do 10 jumping jacks.") #1
        elif(b==2):
            print("Sing a song") #2
        elif(b==3):
            print("Say the alphabet backward.") #3
        elif(b==4):
            print("Pretend to be a cat for 1 minute.") #4
        elif(b==5):
            print("Tell a joke—if no one laughs, do a funny face.") #5

    else:
        print("Invalid input")