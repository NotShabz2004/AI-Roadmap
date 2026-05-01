import requests


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


r = []

a = fetch_data()
for j in a:
    p = a["bitcoin"]["usd"]
    r.append([j, p])
print(r[0][0])
