# Function to handle age input validation
def get_valid_age():
    while True:
        age_input = input("Please enter your age: ")
        # Check if the input is a valid integer (i.e., numeric)
        if age_input.isdigit():
            return int(age_input)  # Convert the valid age to an integer
        else:
            print("Invalid input! Please enter a numeric value for age.")

# Step 1: Collect user input for name, hometown, and age
name = input("Please enter your name: ")         # Input for name (string, supports multiple words)
hometown = input("Please enter your hometown: ") # Input for hometown (string)
age = get_valid_age()                            # Call the function to validate the age

# Step 2: Store the information in a dictionary
user_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Step 3: Print the values on separate lines using a single print() statement
print(f"\nName: {user_info['name']}\nHometown: {user_info['hometown']}\nAge: {user_info['age']}")


