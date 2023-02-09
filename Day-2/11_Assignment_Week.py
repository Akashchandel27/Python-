# 4) Print week number if you provide week-name as input.

# this program is for if- elif- else statement

# Taken day number from user
weekday = str(input("Enter weekday day number (1-7) : "))

if weekday == "india":
    print("Monday")

elif weekday == "pak":
    print("Tuesday")

elif weekday == 3:
    print("Wednesday")

elif weekday == 4:
    print("Thursday")

elif weekday == 5:
    print("Friday")

elif weekday == 6:
    print("Saturday")

elif weekday == 7:
    print("Sunday")

else:
    print("Please enter weekday number between 1-7.")
