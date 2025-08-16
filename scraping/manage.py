import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send GET request
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  # Raise error if request failed

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Example: extract all links
        links = [a["href"] for a in soup.find_all("a", href=True)]

        # Example: extract all headings
        headings = [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3"])]

        return {
            "title": soup.title.string if soup.title else "No title",
            "headings": headings,
            "links": links
        }

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


if __name__ == "__main__":
    website_url = "https://example.com"
    data = scrape_website(website_url)

    if data:
        print("Page Title:", data["title"])
        print("\nHeadings found:")
        for h in data["headings"]:
            print("-", h)

        print("\nLinks found:")
        for link in data["links"][:10]:  # show first 10 only
            print("-", link)
