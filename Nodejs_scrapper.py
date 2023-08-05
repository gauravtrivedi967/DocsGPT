import requests
from bs4 import BeautifulSoup

def scrape_nodejs_documentation(keyword):
    url = f"https://nodejs.org/api/all.html#all_{keyword}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        description = soup.select_one(".desc")
        
        if description:
            return description.text.strip()
    
    return f"No description found for '{keyword}'"

if __name__ == "__main__":
    keyword_to_search = "fs"  # Replace this with the desired keyword you want to search
    description = scrape_nodejs_documentation(keyword_to_search)
    print(description)
