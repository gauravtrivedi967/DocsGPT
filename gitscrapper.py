import requests
import base64

def get_readme_content(repo_url):
    # Construct the API URL for the README file
    api_url = f"https://api.github.com/repos/{repo_url}/readme"

    # Make a GET request to the GitHub API
    response = requests.get(api_url)

    if response.status_code == 200:
        readme_data = response.json()
        readme_content = readme_data.get("content")

        # Decode the base64 encoded content
        decoded_content = base64.b64decode(readme_content).decode('utf-8')

        return decoded_content
    else:
        print(f"Failed to fetch README content. Status code: {response.status_code}")
        return None

def extract_keyword_details(content, keyword):
    keyword_details = []
    lines = content.split('\n')
    
    for line in lines:
        if keyword in line:
            keyword_details.append(line)
    
    return keyword_details

if __name__ == "__main__":
    repo_url = input("Enter GitHub repository (owner/repository): ")
    keyword = input("Enter keyword to search for: ")
    
    readme_content = get_readme_content(repo_url)
    
    if readme_content:
        keyword_details = extract_keyword_details(readme_content, keyword)
        
        if keyword_details:
            print(f"Details related to '{keyword}':")
            for detail in keyword_details:
                print(detail)
        else:
            print(f"No details found related to '{keyword}'.")
