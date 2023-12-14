from requests_html import HTMLSession
from bs4 import BeautifulSoup


def scrape_data(url):
    print("scrape_data() called")
    session = HTMLSession()
    response = session.get(url)

    # Ensure that JavaScript is rendered
    response.html.render()

    if response.status_code == 200:
        # Parsing HTML using requests_html
        html = response.html

        # Extracting the page title
        # page_title = html.find('entry-title', first=True)
        # if page_title:
        #     print(f'Page Title: {page_title.text}')

        # Convert HTML from requests_html to BeautifulSoup for additional parsing
        soup = BeautifulSoup(html.html, "html.parser")
        print(soup.prettify())

        # Scraping H1 titles and text from div tags
        div_elements = soup.find_all(
            "div", class_="elementor-widget elementor-widget-text-editor"
        )
        for div in div_elements:
            h1_element = div.find("h1")
            if h1_element:
                title = h1_element.text.strip()
                print(f"H1 Title: {title}")

                text_element = div.find(
                    "p"
                )  # Adjust if your text is in a different tag
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

    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        # print(f"Attempt: {attempts + 1} of 3")
        # attempts += 1
        # time.sleep(delay)


url = "https://oland.fun/2023-07-14-epic-games-%f0%9f%9f%a5%f0%9f%9f%a9%f0%9f%9f%a8-auction-boosters-land-auctions-and-the-plan-twitter/"
scrape_data(url)
