# ClydeBank Coffee Shop Simulator 4000
# Copyright (c) 2023 ClydeBank Media, All Rights Reserved.

# Import items frfom the random module to generate weather
from random import seed, randint

# Current day number
day = 1

# Starting cash on hand
cash = 100.00

# Coffee on hand
coffee = 100

# Sales list of dictionaries
# sales = [
#     {
#         "day": 1,
#         "coffee_inv": 100,
#         "advertising": 10,
#         "temp": 68,
#         "cups_sold": 16
#     },
#     {
#         "day": 2,
#         "coffee_inv": 84,
#         "advertising": 15,
#         "temp": 72,
#         "cups_sold": 20
#     },
#     {
#         "day": 3,
#         "coffee_inv": 64,
#         "advertising": 5,
#         "temp": 78,
#         "cups_sold": 10
#     },
# ]

# Create an emmpty sales list
sales = []

def welcome():
    print("ClydeBank Coffee Shop Simulator 4000, Version 1.00")
    print("Copyright (c) 2025 ClydeBank Media, All Rights Reserved.\n")
    print("Let's collect some information before we start the game.\n")

def prompt(display="Please input a string", require=True):
    if require:
        s = False
        while not s:
            s = input(display + " ")
    else:
        s = input(display + " ")
    return s

def daily_stats(cash_on_hand, weather_temp, coffee_inventory):
    print("You have $" + str(cash_on_hand) + " cash and it's " + str(weather_temp) + " degrees outside.")
    print("You have enough coffee on hand to make " + str(coffee_inventory) + " cups.\n")

def convert_to_float(s):
    # If conversion fails, assign 0 to it
    try:
        f = float(s)
    except ValueError:
        f = 0
    return f

def get_weather():
    # Generate a random temperature between 20 and 90
    # We'll consider seasons later on, but this is good enough for now
    return randint(20, 90)

# Print welcome message
welcome()

# Get name and store name
name = prompt("What is your name?")
shop_name = prompt("What do you want to name your coffee shop?")

# WE have what we need so lets get started!
print("\nOk, Let's get started. Have fun!")

# The main game loop
running = True
while running:
    # Display the day and add a "fancy" text affect
    print("\n-------| Day " + str(day) + " @ " + shop_name + " |-------")

    # Get weather
    temperature = get_weather()

    # Display the cash and weather
    daily_stats(cash, temperature, coffee)

    # Get price of a cup of coffee
    cup_price = prompt("What do you want to charge per cup of coffee?")

    # Get price of coffee
    print("\nYou can buy advertising to help promote sales.")
    advertising = prompt("How much do you want to spend on advertising (0 for none)?", False)

    # Convert advertising into a float
    advertising = convert_to_float(advertising)

    # Deduct advertising from cash on hand
    cash -= advertising

    # TODO: Calculate today's performance
    # TODO: Display today's performance

    # Before we loop around, add a day
    day += 1