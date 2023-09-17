import requests
import threading
import colorama

colorama.init(autoreset=True)

search = input("Search For: ")

base_url = "https://api.hypixel.net/skyblock/auctions"

def get_totalPages():
    return requests.get(url=base_url).json()["totalPages"]

def search_auctions(search):
    
    items = []

    def fetch_auctions(page):
        url = f"{base_url}?page={page}"
        data = requests.get(url=url).json()

        for item in data["auctions"]:
            if item["bin"] and search.lower() in item["item_name"].lower():
                items.append(item)
    
    threads = []
    for page in range(get_totalPages()):
        thread = threading.Thread(target=fetch_auctions, args=(page,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return items

for item in search_auctions(search):
    item_name = item["item_name"]
    item_price = colorama.Fore.YELLOW + "{:,}".format(item["starting_bid"]) + colorama.Fore.WHITE
    item_rarity = item["tier"]
    item_uuid = item["uuid"]

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

    print(f"{item_name} : {item_price},  /viewauction {item_uuid}")