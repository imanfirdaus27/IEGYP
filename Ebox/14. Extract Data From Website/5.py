import requests
from bs4 import BeautifulSoup
import re

def fetch_and_parse(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching and parsing the URL: {e}")
        return None
    
def extract():
    links = []
    emails = []
    soup = fetch_and_parse(url)
    if soup:
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        for email in re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.get_text()):
            emails.append(email)
    return {'links': links, 'emails': emails}

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    extracted_data = extract()
    print("Extracted data:", extracted_data)