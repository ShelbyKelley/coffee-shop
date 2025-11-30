import unittest
from unittest.mock import patch
import numpy
import os


class TestCoffeeShopSimulator(unittest.TestCase):
    def setUp(self):
        # Mock user inputs for initialization
        with patch('builtins.input', side_effect=['Shelby', 'The Toasty Beans']):
            from coffee_shop_simulator import CoffeeShopSimulator
            self.simulator = CoffeeShopSimulator()

    def tearDown(self):
        # Remove save file if it exists
        if os.path.exists(self.simulator.SAVE_FILE):
            os.remove(self.simulator.SAVE_FILE)

    def test_initialization(self):
        self.assertEqual(self.simulator.player_name, 'Shelby')
        self.assertEqual(self.simulator.shop_name, 'The Toasty Beans')
        self.assertEqual(self.simulator.day, 1)
        self.assertEqual(self.simulator.cash, 100.00)
        self.assertEqual(self.simulator.coffee_inventory, 100)
        self.assertEqual(self.simulator.sales, [])
        self.assertIsNotNone(self.simulator.temps)

    def test_make_temp_distribution(self):
        temps = self.simulator.make_temp_distribution()
        # Check that temps is a numpy array
        self.assertIsInstance(temps, numpy.ndarray)
        self.assertEqual(len(temps), self.simulator.SERIES_DENSITY)
        # Check all values are non-negative (probability density)
        self.assertTrue(all(t >= 0 for t in temps))

    def test_weather_property(self):
        # The weather property uses random.choice on the probability density array,
        # so we just verify it returns an integer
        for _ in range(10):
            temp = self.simulator.weather
            self.assertIsInstance(temp, int)
        
        # Verify it's using values from the temps array
        with patch('random.choice', return_value=25.5) as mock_choice:
            temp = self.simulator.weather
            mock_choice.assert_called_once_with(self.simulator.temps)
            self.assertEqual(temp, 25)

    def test_increment_day(self):
        initial_day = self.simulator.day
        self.simulator.increment_day()
        self.assertEqual(self.simulator.day, initial_day + 1)

    def test_convert_to_float_valid(self):
        result = self.simulator.convert_to_float("3.50")
        self.assertEqual(result, 3.50)
        self.assertIsInstance(result, float)

    def test_convert_to_float_invalid(self):
        result = self.simulator.convert_to_float("not a number")
        self.assertEqual(result, 0)

    def test_convert_to_float_integer(self):
        result = self.simulator.convert_to_float("5")
        self.assertEqual(result, 5.0)

    def test_buy_coffee_success(self):
        initial_cash = self.simulator.cash
        initial_inventory = self.simulator.coffee_inventory
        amount = 50
        
        result = self.simulator.buy_coffee(str(amount))
        
        self.assertTrue(result)
        self.assertEqual(self.simulator.cash, initial_cash - amount)
        self.assertEqual(self.simulator.coffee_inventory, initial_inventory + amount)

    def test_buy_coffee_insufficient_funds(self):
        initial_cash = self.simulator.cash
        initial_inventory = self.simulator.coffee_inventory
        amount = 200  # More than starting cash
        
        result = self.simulator.buy_coffee(str(amount))
        
        self.assertFalse(result)
        self.assertEqual(self.simulator.cash, initial_cash)
        self.assertEqual(self.simulator.coffee_inventory, initial_inventory)

    def test_buy_coffee_invalid_input(self):
        initial_cash = self.simulator.cash
        initial_inventory = self.simulator.coffee_inventory
        
        result = self.simulator.buy_coffee("not a number")
        
        self.assertFalse(result)
        self.assertEqual(self.simulator.cash, initial_cash)
        self.assertEqual(self.simulator.coffee_inventory, initial_inventory)

    def test_daily_sales_basic(self):
        temperature = 30
        advertising = 10
        cup_price = 2.50
        
        sales = self.simulator.daily_sales(temperature, advertising, cup_price)
        
        self.assertIsInstance(sales, int)
        self.assertGreaterEqual(sales, 0)

    def test_daily_sales_limited_by_inventory(self):
        self.simulator.coffee_inventory = 5
        temperature = 30
        advertising = 100
        cup_price = 1.00
        
        sales = self.simulator.daily_sales(temperature, advertising, cup_price)
        
        self.assertLessEqual(sales, 5)

    def test_daily_sales_high_price_zero_sales(self):
        temperature = 30
        advertising = 0
        cup_price = 100.00  # Extremely high price
        
        sales = self.simulator.daily_sales(temperature, advertising, cup_price)
        
        # With high price and no advertising, sales should be 0
        self.assertEqual(sales, 0)

    def test_simulate(self):
        initial_sales_count = len(self.simulator.sales)
        temperature = 40
        advertising = 5
        cup_price = 3.00
        
        cups_sold = self.simulator.simulate(temperature, advertising, cup_price)
        
        # Check that sales record was added
        self.assertEqual(len(self.simulator.sales), initial_sales_count + 1)
        
        # Check sales record contains correct data
        last_sale = self.simulator.sales[-1]
        self.assertEqual(last_sale['day'], self.simulator.day)
        self.assertEqual(last_sale['temp'], temperature)
        self.assertEqual(last_sale['advertising'], advertising)
        self.assertEqual(last_sale['cup_price'], cup_price)
        self.assertEqual(last_sale['cups_sold'], cups_sold)

    @patch('builtins.print')
    def test_daily_stats(self, mock_print):
        self.simulator.cash = 150.50
        self.simulator.coffee_inventory = 75
        temperature = 65
        
        self.simulator.daily_stats(temperature)
        
        # Verify print was called
        self.assertTrue(mock_print.called)

    @patch('builtins.print')
    def test_day_header(self, mock_print):
        self.simulator.day = 5
        self.simulator.day_header()
        
        # Verify print was called with day information
        self.assertTrue(mock_print.called)

    def test_prompt_with_required_input(self):
        with patch('builtins.input', return_value='test input'):
            result = self.simulator.prompt("Test?", require=True)
            self.assertEqual(result, 'test input')

    def test_prompt_with_optional_empty_input(self):
        with patch('builtins.input', return_value=''):
            result = self.simulator.prompt("Test?", require=False)
            self.assertEqual(result, '')

    def test_prompt_retries_on_empty_required(self):
        with patch('builtins.input', side_effect=['', '', 'valid input']):
            result = self.simulator.prompt("Test?", require=True)
            self.assertEqual(result, 'valid input')

if __name__ == '__main__':
    unittest.main()