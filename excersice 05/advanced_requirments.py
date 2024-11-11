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

# Step 2: Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Step 3: input the month number and the year
month_number = int(input("Please enter the month number (1-12): "))
year = int(input("Please enter the year: "))

# Step 4: Adjust February days if it's a leap year
if month_number == 2:
    if is_leap_year(year):
        month_days[2] = 29  # February has 29 days in a leap year
    else:
        month_days[2] = 28  # February has 28 days in a common year

# Step 5: Check if the month number is valid
if 1 <= month_number <= 12:
    print(f"The number of days in month {month_number} of year {year} is {month_days[month_number]}.")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
