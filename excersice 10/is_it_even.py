# Define a function that checks if the number is even or odd
def check_even_odd(number):
    # Perform integer division by 2 and multiply it back to check for even or odd
    if (number // 2) * 2 == number:  # using integer division (//) to divide the number by 2, then multiplies it by 2.
        #If the result is equal to the original number, it means the number is even. Otherwise, it is odd
        return "The number is even." 
    else:
        return "The number is odd."

# Define the main function
def main():
    # Ask the user to input a number
    user_input = int(input("Enter a number: "))  # Convert the input to an integer

    # Call the check_even_odd function with the user's input and store the result
    result = check_even_odd(user_input)

    # Print the result returned by the check_even_odd function
    print(result)

# Call the main function to run the program
if __name__ == "__main__":
    main()
