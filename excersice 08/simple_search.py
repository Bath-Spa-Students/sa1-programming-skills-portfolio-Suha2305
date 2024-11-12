# Type a list of strings containing names 
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# write the string you want to search in the list of strings mentioned above
search_name = "Sam"

# Search for the name in the list
if search_name in names:
    print("{search_name} was on the list.")
else:
    print("{search_name} was not on the list.")