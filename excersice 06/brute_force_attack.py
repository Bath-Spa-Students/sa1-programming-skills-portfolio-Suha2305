# Define the correct password
correct_password = "12345"

#  While loop to repeatedly ask for the password
while True:
    # Ask the user to enter the password
    entered_password = input("Please enter the password: ")

    # Check if the entered password is correct
    if entered_password == correct_password:
        print("Password correct! Access granted.")
        break  # Exit the loop if the password is correct
    else:
        print("Incorrect password. Please try again.")
