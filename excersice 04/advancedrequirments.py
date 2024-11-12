# stating 10 countries and its capitals 
countries_and_capitals = [
    ("France", "Paris"),
    ("Germany", "Berlin"),
    ("Italy", "Rome"),
    ("Spain", "Madrid"),
    ("United Kingdom", "London"),
    ("Portugal", "Lisbon"),
    ("Netherlands", "Amsterdam"),
    ("Belgium", "Brussels"),
    ("Sweden", "Stockholm"),
    ("Norway", "Oslo")
]

# storing 0 as the value of score in the beginning of the quiz
score = 0

# using for loop to loop throught all 10 countries and to ask for their capitals 
# for loop will make sure that all 10 questions are completed before ending the loop even if the answer given by the user is false
for country, correct_capital in countries_and_capitals:
    # Asking the user for the capital of the country
    user_answer = input(f"What is the capital of {country}? ")
    
    # Converting  the user's answer to lowercase to ignore capitalization
    if user_answer.lower() == correct_capital.lower(): 
        print("Correct!")
        score += 1  # Increase score to +1 if the answer given by user is correct
    else:
        print(f"Incorrect. The correct answer is {correct_capital}.")

# After the loop ends the final score is displayed
print(f"\nYou got {score} out of {len(countries_and_capitals)} correct!")
