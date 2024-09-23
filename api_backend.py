import requests

key = ""
enable_cache = True
currency_value_cache = {}
crypto_value_cache = {}

def get_exchange(to_currency_code, from_currency_code):
    # Check cache for existing conversion rates
    if from_currency_code in currency_value_cache and to_currency_code in currency_value_cache[from_currency_code]:
        print("Found in cache")
        return str(currency_value_cache[from_currency_code][to_currency_code])

    print("Currency is not in the cache, calling API...")

    # API call to fetch exchange rates
    url = f"https://v6.exchangerate-api.com/v6/{key}/latest/{from_currency_code.lower()}"
    print(url)
    response = requests.get(url)

    if response.status_code == 200:
        response_json = response.json()  # Ensure it's a dictionary
        converted_rate = response_json.get('conversion_rates', {})

        if not isinstance(converted_rate, dict):
            print("Error: conversion_rates is not a dictionary!")
            return None

        rate = converted_rate.get(to_currency_code)

        if rate:
            # Cache the rate for future use
            if from_currency_code not in currency_value_cache:
                currency_value_cache[from_currency_code] = {}
            currency_value_cache[from_currency_code][to_currency_code] = rate

            print("Converted rate: " + str(rate))
            return str(rate)
        else:
            print(f"Rate for {to_currency_code} not found in API response.")
            return None
    else:
        print("API call failed")
        return None

crypto_value_cache = {}

def get_coin_exchange(from_currency_code, to_coin):
    # Check the cache first
    cache_key = f"{from_currency_code}_{to_coin}"
    if cache_key in crypto_value_cache:
        print("Found in cache")
        return crypto_value_cache[cache_key]

    print("Calling API...")

    # API call to fetch coin prices
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={to_coin}&vs_currencies={from_currency_code.lower()}"
    print(url)

    response = requests.get(url)

    if response.status_code == 200:
        converted_rate = response.json().get(to_coin, {})
        rate = converted_rate.get(from_currency_code.lower())

        if rate:
            # Cache the result
            crypto_value_cache[cache_key] = str(rate)
            print("Converted rate: " + str(rate))
            return str(rate)
        else:
            print(f"Rate for {to_coin} not found in API response.")
            return None
    else:
        print("API call failed")
        return None
