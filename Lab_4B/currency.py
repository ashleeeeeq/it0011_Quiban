currency_file = open('currency.csv', 'r')
header = currency_file.readline().strip()
exchange_rates = {}

for line in currency_file:
    code, name, rate = line.strip().split(',')
    exchange_rates[code] = float(rate)

currency_file.close()

amount_usd = float(input("\nHow much dollar do you have?  "))
target_currency = input("What currency do you want to have (Enter code)? ").strip().upper()

# Convert currency
if target_currency in exchange_rates:
    converted_amount = amount_usd * exchange_rates[target_currency]
    print(f"Dollar: {amount_usd} USD")
    print(f"{target_currency}: {converted_amount:.2f}")
else:
    print(f"Currency '{target_currency}' not found in exchange rates.")