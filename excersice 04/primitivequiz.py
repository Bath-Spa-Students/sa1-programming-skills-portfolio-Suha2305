# Step 1: what is the capital of France
answer_france = input("What is the capital of France? ")

# Step 2: Check if the answer is correct
if answer_france.lower() == "paris": # by using the .lower() function the entire string/answer which is being inputted by the user will entirely be made into lower case. this is done to avoid case-sensitive mistakes during the quiz
    print("Correct!")# if the user enters the answer paris/PARIS/Paris the answer will be still correct as we used the .lower() function
else:
    print("Wrong! The correct answer is Paris.") # if the user enters any answer other than paris it will be deemed as wrong
