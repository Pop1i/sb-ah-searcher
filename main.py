import requests

search = input("item to search for: ")

url = "https://api.hypixel.net/skyblock/auctions"

data = requests.get(url=url).json()

auctions = []
for i in range(data["totalPages"]):
    data = requests.get(url=f"{url}?page={i}").json()
    
    for item in data["auctions"]:
        auctions.append(item)

for item in auctions:
    if item["bin"] == True:
        item_name = item["item_name"]
        if search.lower() in item_name.lower():
            item_price = item["starting_bid"]
            item_price = "{:,}".format(item_price)

            print(f"{item_name} : {item_price}")
