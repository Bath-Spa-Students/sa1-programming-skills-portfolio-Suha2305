# Function to handle age input validation   
def age(): #def (define)
    while True: # using while loop
        age_input = input("Please enter your age: ")
        # Check if the input is a valid integer (i.e., numeric)
        if age_input.isdigit():
            return int(age_input)  # Convert the valid age to an integer as it will only accept numerical
        else:
            print("Invalid input! Please enter a numeric value for age.")

# Step 1: Collect user input for name, hometown, and age
name = input("Please enter your name: ")         # name (string)
hometown = input("Please enter your hometown: ") # hometown (string)
age = age()                            # function to validate the age

# Step 2: stroring each information into a dictionary using {}
user_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Step 3: Print the values on separate lines using \n
print(f"\nName: {user_info['name']}\nHometown: {user_info['hometown']}\nAge: {user_info['age']}") # using a single print() statement\n to create new lines between each answer
