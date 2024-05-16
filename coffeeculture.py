# Define a dictionary representing coffee culture aspects
coffee_culture = {
    "What is Coffee Culture?": "Coffee culture refers to the social atmosphere and traditions surrounding the consumption of coffee.",
    "Origins": "Coffee culture has its roots in various countries around the world, including Ethiopia, Turkey, Italy, and France.",
    "Modern Coffee Culture": "In recent years, coffee culture has experienced a resurgence, with the rise of specialty coffee shops and third-wave coffee movements.",
    "Conclusion": "Coffee culture is more than just a beverage choice—it's a way of life for many people around the world."
}

# Function to display coffee culture aspects
def display_coffee_culture():
    print("Welcome to Coffee Culture!")
    for title, description in coffee_culture.items():
        print("\n" + title)
        print(description)

# Call the function to display coffee culture aspects
display_coffee_culture()
