def get_stock_prices():
    return {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 320
    }

def calculate_total(stock_prices):
    total_value = 0
    details = []

    while True:
        stock = input("Enter stock name (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in stock_prices:
            print("Stock not found.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        value = stock_prices[stock] * quantity
        total_value += value
        details.append(f"{stock} - Qty: {quantity}, Value: {value}")

    return total_value, details

def save_to_file(total, details):
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-----------------------\n")
        for item in details:
            file.write(item + "\n")
        file.write(f"\nTotal Investment Value: {total}")

def stock_portfolio_tracker():
    print("Stock Portfolio Tracker")
    stock_prices = get_stock_prices()

    print("Available stocks:", list(stock_prices.keys()))
    total, details = calculate_total(stock_prices)

    if not details:
        print("No stocks added.")
        return

    print("\nPortfolio Details:")
    for item in details:
        print(item)

    print("Total Investment Value:", total)

    choice = input("Do you want to save this to a file? (yes/no): ").lower()
    if choice == "yes":
        save_to_file(total, details)
        print("Saved to portfolio.txt")

stock_portfolio_tracker()
