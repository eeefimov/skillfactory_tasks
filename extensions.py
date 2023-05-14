import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f"Failed to process same currency {base}.")
            
        if int(amount) <= 0;
            raise ConvertionException("Enter more then 0")


        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"failed to process currency {qoute}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"failed to process currency {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Failed to process quantity {amount}")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[keys[base]] * amount

        return total_base
