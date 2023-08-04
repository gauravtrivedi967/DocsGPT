import requests
from bs4 import BeautifulSoup
from functools import lru_cache

@lru_cache(maxsize=128)  
def fetch_page_content(keyword):
    base_url = "https://nodejs.org/dist/latest-v16.x/docs/api/"
    search_url = f"{base_url}{keyword}.html"

    response = requests.get(search_url)
    if response.status_code != 200:
        return None

    return response.content

def scrape_nodejs_docs(keyword):
    content = fetch_page_content(keyword)
    if not content:
        print(f"Could not retrieve data for '{keyword}'")
        return []

    soup = BeautifulSoup(content, "html.parser")

    
    function_names = [h2.text for h2 in soup.find_all("h2")]

    
    return function_names

if __name__ == "__main__":
    keyword = input("Enter the keyword to search in Node.js documentation: ")
    result = scrape_nodejs_docs(keyword)
    if result:
        print(f"Found {len(result)} functions for '{keyword}':")
        print("\n".join(result))
    else:
        print(f"No functions found for '{keyword}'")
