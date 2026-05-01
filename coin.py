from fastapi import FastAPI
import requests

app = FastAPI()


class CryptoAlert:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_message(self):
        if self.price > 60000:
            return "Bullish Alert🚀"
        else:
            return "Market Update📉"


def llm_messager(a, b):
    if b > 60000:
        return f"{a.capitalize()} is at the cost of {b} Bullish Alert🚀"
    else:
        return f"{a.capitalize()} is at the cost of {b} Market Update📉"


def fetch_data():
    coins = ["bitcoin", "ethereum"]
    coin_string = ",".join(coins)
    resp = requests.get(
        f"https://api.coingecko.com/api/v3/simple/price?ids={coin_string}&vs_currencies=usd"
    )
    if resp.status_code == 200:
        data = resp.json()
    else:
        print(f"Error, status code:{resp.status_code}")
        data = {}
    return data


def get_expensive_coins(data, threshold=60000):
    result = []
    for i in data:
        price = data[i]["usd"]
        if price > threshold:
            bt1 = CryptoAlert(i, price)
            messages = llm_messager(bt1.name, bt1.price)
            result.append(
                {
                    "coin_name": bt1.name,
                    "coin_price": bt1.price,
                    "message": messages,
                }
            )
    return result


@app.get("/")
def home():
    return {"message": "API Running"}


@app.get("/coins")
def get_coins(coin: str = None, threshold: int = 60000):
    data = fetch_data()
    print(data)
    if coin != None:
        if coin in data:
            data = {coin: data[coin]}
        else:
            return {"message": "Coin values not found"}
    return get_expensive_coins(data, threshold)


@app.get("/coin")
def get_coin(coin: str = "bitcoin"):
    data = fetch_data()
    price = data[coin]["usd"]
    if coin:
        return {
            "coin_name": coin,
            "price": price,
            "message": llm_messager(coin, price),
        }
    else:
        return {"message": "coin not found"}


@app.get("/test")
def test():
    return {"message": "Working"}


@app.get("/summary")
def get_sum():
    data = fetch_data()
    length = len(data)
    fin_length = len(get_expensive_coins(data, threshold=40000))
    return {"Total C0ins": length, "Number of required coins": fin_length}

@aoo.get("/data")
def get_data():
    