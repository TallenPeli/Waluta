import requests

key = "1ea948078024d6c63db9fa5f"

def get_exchange(from_currency_code, to_convert_currency_code):
    
    print("Calling API...")

    url = "https://v6.exchangerate-api.com/v6/"+key+"/latest/"+to_convert_currency_code.lower()
    response = requests.get(url)

    if response.status_code == 200:
        converted_rate = response.json().get('conversion_rates')

    rate = converted_rate[from_currency_code]

    print("Converted rate : " + str(rate))
    return str(rate)

def get_coin_exchange(from_currency_code, to_coin):

    print("Calling API...")

    url = "https://api.coingecko.com/api/v3/simple/price?ids="+ to_coin + "&vs_currencies=" + from_currency_code.lower()
    
    print(url)

    response = requests.get(url)

    if response.status_code == 200:
        converted_rate = response.json().get(to_coin)
    
    rate = converted_rate[from_currency_code.lower()]

    print("Converted rate : " + str(rate))

    return(str(rate))