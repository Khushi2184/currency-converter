# Simple Currency Converter

# Exchange rates (example rates, you can update these)
exchange_rates = {
    "USD": {"EUR": 0.85, "INR": 74.0, "GBP": 0.75, "JPY": 110.0},
    "EUR": {"USD": 1.18, "INR": 87.0, "GBP": 0.88, "JPY": 130.0},
    "INR": {"USD": 0.013, "EUR": 0.011, "GBP": 0.010, "JPY": 1.5},
    "GBP": {"USD": 1.33, "EUR": 1.14, "INR": 99.0, "JPY": 150.0},
    "JPY": {"USD": 0.0091, "EUR": 0.0077, "INR": 0.67, "GBP": 0.0067},
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount
    try:
        rate = exchange_rates[from_currency][to_currency]
        return amount * rate
    except KeyError:
        print("Currency conversion not available for the provided currencies.")
        return None

def main():
    print("Welcome to the Currency Converter!")
    
    from_currency = input("Enter the currency you have (e.g., USD, EUR, INR): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., USD, EUR, INR): ").upper()
    amount = float(input(f"Enter the amount in {from_currency}: "))
    
    converted_amount = convert_currency(amount, from_currency, to_currency)
    
    if converted_amount is not None:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
