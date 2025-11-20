import random
import re
from utilities import *

class CoffeeShopSimulator:
    # Minimum and maximum temperatures
    TEMP_MIN = 20
    TEMP_MAX = 90

    def __init__(self, player_name, shop_name):
        # Set player and show names
        self.player_name = player_name
        self.shop_name = shop_name
        # Current day number
        self.day = 1
        # Cash on hand at start
        self.cash = 100.00
        # Inventory at start
        self.coffee_inventory = 100
        # Sales list
        self.sales = []
        # Possible temperatures
        self.temps = self.make_temp_distribution()

    def run(self):
        print("\nOk, Let's get started. Have fun!")
        # The main game loop
        running = True
        while running:
            # Display the day and add a "fancy" text affect
            self.day_header()
            # Get the weather
            temperature = self.weather
            # Display the cash and weather
            self.daily_stats(temperature)
            # Get price of a cup of coffee
            cup_price = convert_to_float(prompt("What do you want to charge per cup of coffee?"))
            # Get advertising budget
            print("\nYou can buy advertising to help promote sales.")
            advertising = convert_to_float(prompt("How much do you want to spend on advertising (0 for none)?", False))
            # Deduct advertising from cash on hand
            self.cash -= advertising
            # Simulate today's sales
            cups_sold = self.simulate(temperature, advertising, cup_price)
            gross_profit = cups_sold * cup_price
            # Display the results
            print("You sold " + str(cups_sold) + " cups of coffee today.")
            print("You made $" + str(gross_profit) + " today.")
            # Add the profit to our coffers
            self.cash += gross_profit
            # Subtract inventory
            self.coffee_inventory -= cups_sold
            # Before we loop, add a day
            self.increment_day()

    def simulate(self, temperature, advertising, cup_price):
        # Find out how many cups were sold
        cups_sold = self.daily_sales(temperature, advertising)
        # Save the sames data for today
        self.sales.append({
            "day": self.day,
            "coffee_inv": self.coffee_inventory,
            "advertising": advertising,
            "temp": temperature,
            "cup_price": cup_price,
            "cups_sold": cups_sold
        })
        # We technically don't need this, but why make the nexxt step
        # read from the sales list when we have the data right here
        return cups_sold
    
    def make_temp_distribution(self):
        # Will make this more mathematically advanced later
        temps = []
        # First, find the average between TEMP_MIN and TEMP_MAX
        avg_temp = (self.TEMP_MIN + self.TEMP_MAX) / 2
        # Find the distance between TEMP_MAX and the average
        max_dist_from_avg = self.TEMP_MAX - avg_temp
        # Loop through all possible temperatures
        for i in range(self.TEMP_MIN, self.TEMP_MAX):
            # How far away is the temperature from the average?
            # abs() gives us the absolute value
            dist_from_avg = abs(avg_temp - i)
            # How far away is the dist_from_avg from the maximum
            dist_from_max_dist = max_dist_from_avg - dist_from_avg
            # If the value is zero, make it 1
            if dist_from_max_dist == 0:
                dist_from_max_dist = 1
            # Append the output of x_of_y to temps
            for t in x_of_y(int(dist_from_max_dist), i):
                temps.append(t)
        return temps

    def increment_day(self):
        self.day += 1

    def daily_stats(self, temperature):
        print("You have $" + str(self.cash) + " cash and it's " + str(temperature) + " degrees outside.")
        print("You have enough coffee on hand to make " + str(self.coffee_inventory) + " cups.\n")

    def day_header(self):
        print("\n-------| Day " + str(self.day) + " @ " + self.shop_name + " |-------")

    def daily_sales(self, temperature, advertising):
        return int((self.TEMP_MAX - temperature) * (advertising * 0.5))
    
    @property
    def weather(self):
        # Generate a random temperature between TEMP_MIN and TEMP_MAX
        # We'll consider seasons later on, but this is good enough for now
        return random.choice(self.temps)
