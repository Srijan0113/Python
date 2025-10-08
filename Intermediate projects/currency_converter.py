from requests import get
from pprint import PrettyPrinter

BASE_URL='https://api.freecurrencyapi.com/v1/'
API_KEY='fca_live_YM1QOZjRuuFJaGhVVIKFZOosWDvZVhh7L5FRnYNO'

printer=PrettyPrinter()

def get_currencies():
    endpoint= f"currencies?apikey={API_KEY}"
    url=BASE_URL + endpoint
    data=get(url).json()['data']

    data = list(data.items())
    data.sort()

    return data
def print_currencies(currencies):
    for name,currency in currencies:
        name=currency['name']
        _id = currency['code']
        symbol=currency.get('symbol','')
        print(f"{_id}-{name}-{symbol}")

def exchange_rate(currency1,currency2):
    endpoint=f"latest?apikey={API_KEY}&base_currency={currency1}&currencies={currency2}"
    url= BASE_URL + endpoint
    response=get(url)
    data=response.json()['data']
    
    if len(data)==0:
        print("Invalid Currencies")
        return
    
    rate = round((list(data.values())[0]),2)
    print(f"{currency1} -> {currency2} = {rate}")

    return rate 

def converter(currency1,currency2,amount):
    rate=exchange_rate(currency1,currency2)
    if rate is None:
        return
    
    try:
        amount=float(amount)
    except:
        print("Invalid amount")
        return
    
    converted_amount=rate*amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount

def main():
    currencies=get_currencies()
    print("Welcome to currency converter! ")
    print("-"*60)
    print("1.List - lists the different currencies")
    print("2.Convert - Convert from one currency to another")
    print("3.Rate - Get the exchange rate to two currencies")
    print("-"*60)

    while True:
        command = input("Enter a command (q to quit)(List/Convert/Rate) : ").lower() 

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command=="convert":
            currency1=input("Enter a base currency : ").upper()
            amount=input(f"Enter an amount in {currency1} : ")
            currency2=input("Enter the currency to convert to : ").upper()
            converter(currency1,currency2,amount)

        elif command=="rate":
            currency1=input("Enter a base currency : ").upper()
            currency2=input("Enter the currency to convert to : ").upper()
            exchange_rate(currency1,currency2)
        else:
            print("Unrecognized command")

main()
# printer.pprint(data)

# data=get_currencies()
# print_currencies(data)
# rate=exchange_rate("USD","INR")
# print(rate)


