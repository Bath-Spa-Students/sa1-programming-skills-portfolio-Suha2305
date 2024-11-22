# Allow user input for the search term
search_term = input("Enter the name you want to search for: ")

# List of names given
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] # putting all the names into strings into a varibale (name)

# Function to search for the string within the list
def search_name(names, search_term):  # names is the list of names to search through, search_term is the name you're looking for
    if search_term in names:
        print(search_term + " is found in the list.")  # using Concatenation to combine strings.
    else:
        print(search_term + " is not in the list.")  # Added a space after search_term for better formatting


# Call the search function
search_name(names, search_term)  
