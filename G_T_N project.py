import random
target = random.randint(0,100)
print(target)
i = 1
while True:
    user_input = int(input("\nGuess a number: "))
    if(user_input == target):
        print(f"\nCongrats you guess the right number at {i} attempts.")
        break
    elif(user_input > target):
        print("\nvery large guess! \nTry again")
    else:
        print("\nvery small guess! \nTry again")
    i+=1
##import os
##print(os.getcwd())
##print(os.listdir())
##os.makedirs('New_Folder')
##import pandas as  pd
##import numpy as np
##df = pd.read_csv("cab_rides_dataset.csv")
##pd.set_option('display.max_rows',300)
##print(df.head())
##print(df.columns)
##print(df.dtypes)
##print(df.head())
##print(df.groupby('payment_method')['customer_id'].count())