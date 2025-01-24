from bs4 import BeautifulSoup
import requests
import json

# URL for job search on OLX
url = 'https://www.olx.pl/zwierzeta/psy/konin/'
page = requests.get(url).text  #
doc = BeautifulSoup(page, "html.parser")  

links_found = {}  # Dictionary to store found links
div = doc.find("div", class_='css-j0t2x2')  # Finding the main div containing job listings

# Scraping next pages
all_pages = doc.find('ul', class_='pagination-list')  
last_page = all_pages.find_all('li')  
last_li = last_page[-1]  #
last_int = int(last_li.get_text(strip=True))  

print(last_int)  # Displaying the number of pages
print(type(last_int))  # Displaying the type of the last_int variable

# Checking if the div was found
if div:
    for page in range(1, last_int + 1):  # Iterating through all pages
        # Updating the URL for each page
        url = f'https://www.olx.pl/praca/informatyka/?page={page}&search%5Bfilter_enum_type%5D%5B0%5D=parttime&search%5Bfilter_enum_type%5D%5B1%5D=halftime&search%5Bfilter_enum_type%5D%5B2%5D=seasonal&search%5Bfilter_enum_workplace%5D%5B0%5D=remote_work_possibility'
        page_content = requests.get(url).text  # Sending a request to the new URL
        doc = BeautifulSoup(page_content, "html.parser")  # Parsing the new page
        
        # Finding the div on the new page
        div = doc.find("div", class_='css-j0t2x2')
        
        if div:
            
            items = div.find_all("a")
            for item in items:
                link = item["href"].strip()  # Ensuring there are no extra spaces
                full_link = f"https://www.olx.pl{link}"  # Creating the full link
                
                print(f"Full link: {full_link}")  # Debugging output
                
                # Checking if the advertisement contains the words
                try:
                    ad_page = requests.get(full_link).text
                    ad_doc = BeautifulSoup(ad_page, "html.parser")
                    ad_text = ad_doc.get_text()  
                    
                    # Checking if the advertisement does not contain specified words
                    if not ("18" in ad_text or "obywatelstwo" in ad_text or "pełnoletni" in ad_text or "pełnoletniość" in ad_text or "Pełnoletność" in ad_text):
                        links_found[item.get_text(strip=True)] = {"link": full_link}  # Using get_text() as the key
                        print(full_link)  # Displaying the valid link
                        # Saving results to a JSON file. Set your json file path.
                        with open("D:/Programming/Pyfun/aplikacje/scraper.json", "w") as file:
                            json.dump(links_found, file, indent=4)
                    else:
                        print(f"Skipping advertisement containing specified words.")
                except requests.exceptions.RequestException as e:
                    print(f"Error while fetching {full_link}: {e}")
        else:
            print("Did not find div with class 'css-j0t2x2' on page:", page)
else:
    print("Did not find div with class 'css-j0t2x2'.")











# doc = BeautifulSoup(page, "html.parser")
    
# div = doc.find(class_="item-cells-wrap border-cells short-video-box items-list-view is-list")    
# items = div.find_all(string=re.compile(search_term))

# for item in items:
#     parent = item.parent
#     if parent.name != "a":
#         continue
#     link = parent['href']
#     next_parent = item.find_parent(class_="item-container")
#     price_element = next_parent.find(class_='price-current')
#     if price_element and price_element.strong:
#         price = price_element.strong.string.strip()
#     items_found[item] = {"price": int(price.replace(",", "")), "link":link}   