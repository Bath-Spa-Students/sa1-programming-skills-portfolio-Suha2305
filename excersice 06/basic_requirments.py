# Step 1: Define the correct password  
correct_password = "12345"  

# Step 2: Use a while loop to repeatedly ask for the password
while True:
    # Ask the user to enter the password
    entered_password = input("Please enter the password: ")

    # Step 3: Check if the entered password is correct
    if entered_password == correct_password:
        print("Password correct! Access granted.")
        break  # Exit the loop once the correct password is entered
    else:
        print("Incorrect password. Please try again.")
