from bs4 import BeautifulSoup
import requests
import re
import json

search_term = input("What product do you want to search for? ")

url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

items_found = {}

for page in range(1, pages + 1):
    url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    
    div = doc.find(class_="item-cells-wrap border-cells short-video-box items-list-view is-list")    
    items = div.find_all(string=re.compile(search_term))
    
    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue
        link = parent['href']
        next_parent = item.find_parent(class_="item-container")
        price_element = next_parent.find(class_='price-current')

        if price_element and price_element.strong:
            price = price_element.strong.string.strip()
            items_found[item] = {"price": int(price.replace(",", "")), "link":link}   

sorted_items = sorted(items_found.items(), key=lambda x: x[1]["price"])

with open(("ścieżka do pliku, w którym chcesz zapisać dane: "), "w") as file:
    json.dump(items_found, file, indent=4)
    

    
    



# url = "https://www.newegg.ca/p/pl?d=4070&N=4131&page=1"
# response = requests.get(url)

# # Sprawdzenie, czy strona została załadowana poprawnie
# if response.status_code == 200:
#     doc = BeautifulSoup(response.text, "html.parser")

#     # Sprawdzenie, czy element z klasą istnieje
#     div = doc.find(class_="item-cells-wrap border-cells short-video-box items-list-view is-list")
    
#     if div:
#         items = div.find_all(text=re.compile("4070"))  # Przykład wyszukiwania
#         for item in items:
#             print(item.strip())
#     else:
#         print("Element with the specified class was not found.")
# else:
#     print(f"Error: Unable to access the page, status code: {response.status_code}")




    















# with open('D:/Programming/Pyfun/aplikacje/index.html', 'r') as f:
#     doc = BeautifulSoup(f, 'html.parser')

# tags = doc.find_all("input", type='text')
# for tag in tags:
#     tag['placeholder'] = 'I changed you'
    
# with open("changed.html", 'w') as file:
#     file.write(str(doc))













# with open('D:/Programming/Pyfun/aplikacje/index.html', 'r') as f:
#     doc = BeautifulSoup(f, 'html.parser')

# tags = doc.find_all(text=re.compile("\$.*"))
# for tag in tags:
#     print(tag.strip())
    
























# with open('D:/Programming/Pyfun/aplikacje/index.html', 'r') as f:
#     doc = BeautifulSoup(f, 'html.parser')

# tag = doc.find_all(["option"], text='Undergraduate', value="featured-courses")

# print(tag)













# base_url = 'https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/karta-graficzna-gigabyte-geforce-rtx-4060-eagle-oc-8gb-dlss-3'

# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# }

# response = requests.get(base_url, headers=headers)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, "html.parser")
    
#     prices = soup.find(text='zł')
#     parent = prices[0].parent
    
#     print(prices.prettify)
# else:
#     print('dyntka')








# url = 'https://www.newegg.ca/gigabyte-windforce-gv-n4070wf3oc-12gd-nvidia-geforce-rtx-4070-12gb-gddr6x/p/N82E16814932611'

# result = requests.get(url)
# doc = BeautifulSoup(result.text, "html.parser")

# prices = doc.find_all(text='$')
# parent = prices[0].parent
# strong = parent.find("strong")
# print(strong.string)










# with open("D:/Programming/Pyfun/aplikacje/index.html", 'r') as f:
#     doc = BeautifulSoup(f, "html.parser")

# tags = doc.find_all('p')[0]

# print(doc.find_all('b'))