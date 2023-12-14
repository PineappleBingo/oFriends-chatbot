import requests
from bs4 import BeautifulSoup


def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Scraping H1 titles and text from div tags
    div_elements = soup.find_all(
        "div", class_="elementor-widget elementor-widget-text-editor"
    )
    for div in div_elements:
        h1_element = div.find("h1")
        if h1_element:
            title = h1_element.text.strip()
            print(f"H1 Title: {title}")

            text_element = div.find("p")  # Adjust if your text is in a different tag
            if text_element:
                text = text_element.text.strip()
                print(f"Text: {text}")

    # Scraping a tags with class name containing "https://twitter.com/i/spaces"
    twitter_links = soup.find_all(
        "a", class_=lambda value: value and "https://twitter.com/i/spaces" in value
    )
    for link in twitter_links:
        href = link.get("href")
        print(f"Twitter Spaces Link: {href}")


url = "https://oland.fun/2023-07-14-epic-games-%f0%9f%9f%a5%f0%9f%9f%a9%f0%9f%9f%a8-auction-boosters-land-auctions-and-the-plan-twitter/"

scrape_data(url)
