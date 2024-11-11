# Step 1: Create a dictionary with month numbers as keys and number of days as values
month_days = {
    1: 31,   # January
    2: 28,   # February 
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

# Step 2: input the month number
month_number = int(input("Please enter the month number (1-12): "))

# Step 3: Check if the input is valid and output the number of days in the month
if 1 <= month_number <= 12:
    print(f"The number of days in month {month_number} is {month_days[month_number]}.")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
