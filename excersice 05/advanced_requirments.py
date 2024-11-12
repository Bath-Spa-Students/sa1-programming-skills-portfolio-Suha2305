# Step 1: Create a dictionary with month numbers as keys and number of days as its values
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
def is_leap_year(year): # The function is_leap_year(year) checks if a year is a leap year 
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # what each function does - year % 4 == 0: Checks if the year is divisible by 4
        #year % 100 != 0: Ensures the year is not divisible by 100, unless it's divisible by 400.
        #year % 400 == 0: Allows century years divisible by 400 to be leap years.
        return True # if return turns True: Year is a leap year.
    return False # if return turns false: year is not a leap year.

# Step 3: input the month number and the year
month_number = int(input("Please enter the month number (1-12): ")) # month_number Stores the entered month number (1-12). eg 3= march
# the input function allows us to enter something
year = int(input("Please enter the year: ")) #int()function Converts the input (string) to an integer.

# Step 4: Adjust February days if it's a leap year
if month_number == 2: # month 2 is february
    if is_leap_year(year): # if is_leap_year(year): Calls the is_leap_year function to check if the year is a leap year.
        month_days[2] = 29  # February has 29 days in a leap year
    else:
        month_days[2] = 28  # February has 28 days in a common year

# Step 5: Check if the month number is valid
if 1 <= month_number <= 12: # this function  [] <= month_number <= 12:] Checks if the month number is between 1 and 12
    print(f"The number of days in month {month_number} of year {year} is {month_days[month_number]}.")
else:
    print("Invalid month number! Please enter a number between 1 and 12.") #if the month number entered is not between 1-12 this will be printed
