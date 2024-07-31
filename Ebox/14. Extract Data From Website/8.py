import requests
from bs4 import BeautifulSoup

base_url = 'http://books.toscrape.com/'

# Input minimum and maximum price
minimum_price = float(input("Enter the minimum amount\n"))
maximum_price = float(input("Enter the maximum amount\n"))

# Make request to the website and parse with BeautifulSoup
response = requests.get(base_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all book articles with class 'product_pod'
books = soup.find_all('article', class_='product_pod')

print(f"Books between £{minimum_price:.2f} and £{maximum_price:.2f}:")

for book in books:
    # Extract title and price of the book
    book_title = book.h3.a['title']
    book_price = float(book.find('p', class_='price_color').text.strip('£'))

    # Check if the book price is within the specified range
    if minimum_price <= book_price <= maximum_price:
        print("Title:", book_title)
        print("Price: £{:.2f}".format(book_price))
        print()