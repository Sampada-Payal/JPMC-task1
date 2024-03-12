import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Update this function ------------- """
    if price_b == 0:
        return None  # Return None instead of nothing
    return price_a / price_b


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in range(N):  # iter(range(N)) is unnecessary
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        """ ----------- Update to get the ratio --------------- """
        prices = {}  # Initialize dictionary to store prices
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
            prices[stock] = price  # Store the price in the prices dictionary with the stock symbol as key

        # Check if both stocks are in prices dictionary before calculating ratio
        if "ABC" in prices and "DEF" in prices:
            ratio = getRatio(prices["ABC"], prices["DEF"])
            if ratio is not None:
                print("Ratio %s" % ratio)
            else:
                print("Cannot calculate ratio because price_b is 0")
        else:
            print("Cannot calculate ratio because one or both stock prices are missing")
