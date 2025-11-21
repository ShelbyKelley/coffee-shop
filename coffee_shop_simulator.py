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
        print(f"\nOk, Let's get started. Have fun {self.player_name}!")
        # The main game loop
        running = True
        while running:
            # Display the day and add a "fancy" text affect
            self.day_header()
            # Get the weather
            temperature = self.weather
            # Display the cash and weather
            self.daily_stats(temperature)

            # Get price of a cup of coffee (but provide an escape hatch)
            response = prompt("What do you want to charge per cup of coffee? (type exit to quit)")
            if re.search("^exit", response, re.IGNORECASE):
                running = False
                continue
            else:
                cup_price = convert_to_float(response)
            
            # Do they want to buy more coffee inventory
            response = prompt("Want to buy more coffee? (hit ENTER for none or enter number)", False)
            if response:
                if not self.buy_coffee(response):
                    print("Could not buy additional coffee.")

            # Get advertising budget
            print("\nYou can buy advertising to help promote sales.")
            advertising = convert_to_float(prompt("How much do you want to spend on advertising (0 for none)?", False))
            # Deduct advertising from cash on hand
            self.cash -= advertising

            # Simulate today's sales
            cups_sold = self.simulate(temperature, advertising, cup_price)
            gross_profit = cups_sold * cup_price
            # Display the results
            print(f"You sold {cups_sold} cups of coffee today.")
            print(f"You made ${gross_profit:.2f} today.")
            # Add the profit to our coffers
            self.cash += gross_profit
            # Subtract inventory
            self.coffee_inventory -= cups_sold

            if self.cash < 0:
                print("\n:( GAME OVER! You ran out of cash.")
                running = False
                continue

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
    
    def buy_coffee(self, amount):
        try:
            i_amount = int(amount)
        except ValueError:
            return False

        if i_amount <= self.cash:
            self.coffee_inventory += i_amount
            self.cash -= i_amount
            return True
        else:
            return False

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
        print(f"You have ${self.cash:.2f} cash on hand and it's {temperature} degrees outside.")
        print(f"You have enough coffee on hand to make {self.coffee_inventory} cups.\n")

    def day_header(self):
        print(f"\n-------| Day {self.day} @ {self.shop_name} |-------")

    def daily_sales(self, temperature, advertising):
        sales = int((self.TEMP_MAX - temperature) * (advertising * 0.5))
        if sales > self.coffee_inventory:
            sales = self.coffee_inventory
            print("You would have sold more coffee but you ran out. Be sure to buy more inventory.")
        return sales
    
    @property
    def weather(self):
        # Generate a random temperature between TEMP_MIN and TEMP_MAX
        # We'll consider seasons later on, but this is good enough for now
        return random.choice(self.temps)
