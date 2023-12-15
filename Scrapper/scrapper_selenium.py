from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# enable headless mode in Selenium
options = Options()
options.add_argument("--headless=new")

driver = webdriver.Chrome(
    options=options,
    # other properties...
)


driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)


def scrape_data(url):
    # initialize an instance of the chrome driver (browser)
    driver = webdriver.Chrome()
    # visit your target site
    driver.get(url)

    h1_element = driver.find_element(By.CSS_SELECTOR, "h1.entry-title")
    a_element = driver.find_element(By.CSS_SELECTOR, "a[href*='https://twitter.com']")
    p_elements = driver.find_elements(
        By.CSS_SELECTOR, "div.elementor-widget-text-editor p"
    )

    if h1_element:
        title = h1_element.text.strip()
        print(f"Title: {title}")

    if a_element:
        x_link = a_element.get_attribute("href")
        print(f"Source: {x_link}")

    if p_elements:
        print(f"Context: {p_elements}")

    # release the resources allocated by Selenium and shut down the browser
    driver.quit()


url = "https://oland.fun/overlinet-ama-2022-12-13-olands-ai-world-builder-dream-engine-1-ocash-and-2023-twitter/"
scrape_data(url)
