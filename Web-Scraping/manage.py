import requests

url = "https://exampl"
response = requests.get(url)
html = response.text

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
title = soup.title.text


url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"


import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
TARGET_PRICE = 20  # Set your desired price

headers = {
    "User-Agent": "Mozilla/5.0"
}

def check_price():
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract title
    title = soup.find("h1").text.strip()

    # Extract price
    price_text = soup.find("p", class_="price_color").text
    price = float(price_text.replace("£", "").strip())

    print(f"{title}: £{price}")

    if price < TARGET_PRICE:
        print("🚨 Price dropped! Time to buy!")

check_price()
