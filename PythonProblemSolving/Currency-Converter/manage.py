print("Welcome to currency Converter")

exchange_rate = {
    'USD': 1.0,          # Base currency
    'PKR': 277.0,        # Pakistani Rupees
    'EUR': 0.91,         # Euro
    'INR': 83.0,         # Indian Rupees
    'GBP': 0.78,         # British Pound
}

print("Available Curriences")
for currency in exchange_rate:
    print("-",currency)

from_currency = input("Enter FROM currency (e.g., USD): ").upper()
to_currency = input("Enter TO currency (e.g., PKR): ").upper()
amount = float(input(f"Enter amount in {from_currency}: "))

# Check if valid
if from_currency in exchange_rate and to_currency in exchange_rate:
    # Convert to USD first, then to target
    amount_in_usd = amount / exchange_rate[from_currency]
    converted_amount = amount_in_usd * exchange_rate[to_currency]

    print(f"\n{amount} {from_currency} = {round(converted_amount, 2)} {to_currency}")
else:
    print("Invalid currency code. Please use one of the listed currencies.")
