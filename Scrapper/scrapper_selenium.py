from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_data(url):
    # Replace 'path/to/chromedriver' with the actual path to chromedriver
    driver = webdriver.Chrome(executable_path="path/to/chromedriver")

    driver.get(url)

    # Find H1 tag with class name 'entry-title'
    h1_element = driver.find_element(By.CSS_SELECTOR, "h1.entry-title")
    if h1_element:
        title = h1_element.text.strip()
        print(f"H1 Title: {title}")

    driver.quit()


url = "https://oland.fun/overlinet-ama-2022-12-13-olands-ai-world-builder-dream-engine-1-ocash-and-2023-twitter/"
scrape_data(url)
