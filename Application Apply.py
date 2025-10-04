import datetime

# Define deadlines
deadlines = {
    1: ("uet", datetime.datetime(2025, 8, 10)),
    2: ("comsat", datetime.datetime(2025, 7, 20)),
    3: ("lums", datetime.datetime(2026, 8, 17)),
    4: ("fast", datetime.datetime(2025, 7, 4)),
    5: ("umt", datetime.datetime(2025, 7, 17)),
    6: ("itu", datetime.datetime(2025, 6, 30)),
    7: ("pu", datetime.datetime(2025, 7, 4)),
    8: ("gcu", datetime.datetime(2025, 7, 5)),
}

today = datetime.datetime.now()

# Get user input
user_input = int(input("Enter \n1 for uet\n2 for comsat\n3 for lums\n4 for fast\n5 for umt\n6 for itu\n7 for pu\n8 for gcu :\n"))

# Check deadline
if user_input in deadlines:
    value = deadlines[user_input]
    uni_name = value[0]
    deadline = value[1]
    if today.date() == deadline.date():
        print("Today is the last day to apply!!!")
    elif today.date() < deadline.date():
        print(f"{deadline.day}-{deadline.strftime('%B')}-{deadline.year} is the last date to apply.")
    else:
        print("Deadline has passed.")
else:
    print("Invalid input.")