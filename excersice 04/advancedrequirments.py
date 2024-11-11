# Advanced Requirements: Quiz for 10 European countries
countries_and_capitals = {
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Finland": "Helsinki",
    "Ireland": "Dublin"
}

for country, capital in countries_and_capitals.items():
    answer = input(f"What is the capital of {country}? ")
    
    if answer.lower() == capital.lower():
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {capital}.")

print("Quiz finished!")