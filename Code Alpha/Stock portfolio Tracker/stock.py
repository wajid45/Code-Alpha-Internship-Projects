import requests


class Stock:
    def __init__(self, symbol, quantity, price):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price if price is not None else self.get_stock_price()

    def get_stock_price(self):
        # This method can be left empty or removed
        print(f"Please enter the price for {self.symbol}:")
        return float(input("Price: "))

    def current_value(self):
        return self.price * self.quantity
