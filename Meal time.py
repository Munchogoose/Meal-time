"""Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00,
lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.
This program tells the user what to eat base on their time."""

This is a program that prompts a user for a time and outputs whether it’s breakfast time,
lunchtime, or dinner time. If it’s not time for a meal,
depending on the real world time at their current location."""


#Asking user what the time is.
def main():
    time = input("Please enter the time in the format ##:##\n\n")
    if ":" in time[2] and len(time) == 5:
        time = time.split(":")
        convert(time)
    else:
        print("Invalid time format, please try again")
        print("\n")
        main()


#Converting the digital time format into a decimal.
def convert(t):
    t[0] = int(t[0])
    minutes_conversion = float(t[1])/60
    time_as_decimal = round(t[0]+minutes_conversion,2)
    meal_type(time_as_decimal)


#Telling user what to eat based on their time which has been converted into a decimal
def meal_type(x):
    if 7 <= x <= 8:
        print("Breakfast time")
    elif 12<= x <= 13:
        print("Lunch time")
    elif 18<= x <= 19:
        print("Dinner time")
    else:
        print("Hope your not feeling too peckish, it's note quite time to eat yet")


main()
