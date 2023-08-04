import requests
from bs4 import BeautifulSoup
from functools import lru_cache

@lru_cache(maxsize=128)  # Cache up to 128 most recently used requests
def fetch_page_content(keyword):
    base_url = "https://nodejs.org/docs/latest-v20.x/api/"
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

    # Extract the function names and descriptions
    function_details = []
    h2_tags = soup.find_all("h2")
    for h2 in h2_tags:
        function_name = h2.text.strip()
        next_element = h2.find_next_sibling()

        if next_element and next_element.name == "p":
            description = next_element.text.strip()
            function_details.append((function_name, description))

    return function_details

if __name__ == "__main__":
    keyword = input("Enter the keyword to search in Node.js documentation: ")
    result = scrape_nodejs_docs(keyword)
    if result:
        print(f"Found {len(result)} functions for '{keyword}':")
        for i, (function_name, description) in enumerate(result, 1):
            print(f"{i}. {function_name}")
            print(f"   {description}")
    else:
        print(f"No functions found for '{keyword}'")
