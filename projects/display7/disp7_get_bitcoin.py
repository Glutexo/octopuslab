# get bitcoin

from time import sleep
import urequests, json
from utils.octopus import w, disp7_init
from shell.terminal import printTitle


w()
d7 = disp7_init()

def bitcoin_usd():
    # res = urequests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin/")
    # btcusd = res.json()[0]['price_usd']
    res = urequests.get("https://api.coinpaprika.com/v1/tickers/btc-bitcoin")
    btcusd = res.json()['quotes']["USD"]["price"]
    return float(btcusd)

printTitle("get_bitcoin.py")
print("this is simple Micropython example | ESP32 & octopusLAB")
print()    

while True:
    btc = bitcoin_usd()
    print(btc)
    d7.show(btc)
    sleep(20)
    d7.show("btc-usd")
    sleep(3)
