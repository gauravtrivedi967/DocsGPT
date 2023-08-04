import requests
from bs4 import BeautifulSoup

def scrape_nodejs_docs(keyword):
    base_url = "https://nodejs.org/docs/latest-v20.x/api/"
    url = base_url + keyword + ".html"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        section = soup.find('section', {'class': 'sect1'})

        if section:
            title = section.find('h1').text.strip()
            description = section.find('p').text.strip()

            print(f"Title: {title}")
            print(f"Description: {description}")
        else:
            print(f"Keyword '{keyword}' not found in Node.js documentation.")
    else:
        print(f"Failed to fetch the documentation for '{keyword}'. Check if the keyword is valid.")

if __name__ == "__main__":
    keyword = input("Enter a keyword to search in Node.js documentation: ")
    scrape_nodejs_docs(keyword)
