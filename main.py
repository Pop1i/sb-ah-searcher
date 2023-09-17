import requests
import colorama

colorama.init(autoreset=True)

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
            item_rarity = item["tier"]

            item_price = item["starting_bid"]
            item_price = colorama.Fore.YELLOW + "{:,}".format(item_price)

            match item_rarity:
                case "COMMON":
                    item_name = colorama.Fore.WHITE + item_name
                case "UNCOMMON":
                    item_name = colorama.Fore.GREEN + item_name
                case "RARE":
                    item_name = colorama.Fore.BLUE + item_name
                case "EPIC":
                    item_name = colorama.Fore.MAGENTA + item_name
                case "LEGENDARY":
                    item_name = colorama.Fore.YELLOW + item_name
                case "SPECIAL":
                    item_name = colorama.Fore.RED + item_name

            print(f"{item_name} : {item_price}")
