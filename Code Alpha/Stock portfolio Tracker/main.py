class StockPortfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol].quantity += quantity
        else:
            self.stocks[symbol] = Stock(symbol, quantity)

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            if self.stocks[symbol].quantity > quantity:
                self.stocks[symbol].quantity -= quantity
            elif self.stocks[symbol].quantity == quantity:
                del self.stocks[symbol]
            else:
                print("Not enough shares to remove.")
        else:
            print("Stock not found in portfolio.")

    def track_portfolio(self):
        total_value = 0
        print("\nPortfolio Summary:")
        for stock in self.stocks.values():
            current_value = stock.current_value()
            total_value += current_value
            print(f"{stock.symbol}: {stock.quantity} shares, Total Value: ${current_value:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}")

def main():
    portfolio = StockPortfolio()

    while True:
        action = input("\nChoose an action: add, remove, track, exit: ").strip().lower()
        if action == 'add':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif action == 'remove':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity to remove: "))
            portfolio.remove_stock(symbol, quantity)
        elif action == 'track':
            portfolio.track_portfolio()
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()