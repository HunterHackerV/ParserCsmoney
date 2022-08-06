import requests
import json
items = {}
items["items"] = []
def filter():
    for i in range(0, len(items["items"])): 
        for j in range(i+1, len(items["items"])): 
            if(items["items"][i]["Overprice"] == None):
                items["items"][i]["Overprice"] = 0
        
            if(items["items"][j]["Overprice"] == None):
                items["items"][j]["Overprice"] = 0

            if(items["items"][j]["Overprice"] != None and items["items"][i]["Overprice"] != None and -1*items["items"][i]["Overprice"] < -1*items["items"][j]["Overprice"]): 
                temp = items["items"][i]
                items["items"][i] = items["items"][j]
                items["items"][j] = temp
def Parsing():
    offset = 0
    while True:
        url = f"https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=15.78273536994487&minPrice=1&offset={offset}&order=asc&sort=price&withStack=true"
        jsonCode = json.loads(requests.get(url).text)
        try:
            if(jsonCode["error"] == 2):
                break
        except:
            print()
        finally:
            print()
        for item in jsonCode["items"]:
            if (item["overprice"] != None and item["overprice"] >= 0) == False and item["quality"] != None:
                print(item["float"])
                items["items"].append({
                    "Name": item["fullName"],
                    "Quality": item["quality"],
                    "Float": item["float"],
                    "Price": item["price"],
                    "Overprice": item["overprice"]
                })
        offset += 60
if "__main__" == __name__:
    Parsing()
    filter()
    with open('data.json', 'w') as outfile: 
        json.dump(items, outfile)