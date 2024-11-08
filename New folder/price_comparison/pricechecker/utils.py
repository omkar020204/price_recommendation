# pricechecker/utils.py
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
def get_ebay_price(product_name):
    search_url = f'https://www.ebay.com/sch/i.html?_nkw={product_name.replace(" ", "+")}'
    
    # Set up Chrome options to run in headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # This runs the browser in the background
    chrome_options.add_argument('--no-sandbox')  # Required for running in some environments (like Docker)
    chrome_options.add_argument('--disable-dev-shm-usage')  # Prevents crashes in some environments

    # Initialize the WebDriver with ChromeOptions
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(search_url)
    time.sleep(3)  # Wait for the page to load
    
    try:
        price_element = driver.find_element(By.CLASS_NAME, 's-item__price')
        price = price_element.text.strip()
        price_value = float(price.replace('$', '').replace(',', ''))
        print(f"Found eBay price: {price_value}")
        driver.quit()  # Close the browser
        return price_value
    except Exception as e:
        print(f"Error scraping eBay: {e}")
        driver.quit()
        return None
# pricechecker/utils.py
def get_amazon_price(product_name):
    search_url = f'https://www.amazon.com/s?k={product_name.replace(" ", "+")}'
    
    # Set up Chrome options to run in headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in background without GUI
    chrome_options.add_argument('--no-sandbox')  # Prevents issues in restricted environments
    chrome_options.add_argument('--disable-dev-shm-usage')  # Avoids crash in limited environments

    # Initialize the WebDriver with ChromeOptions
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(search_url)
    time.sleep(3)  # Wait for page to load

    try:
        price_element = driver.find_element(By.CLASS_NAME, 'a-price-whole')
        price = price_element.text.strip()
        price_value = float(price.replace('$', '').replace(',', ''))
        print(f"Found Amazon price: {price_value}")
        driver.quit()  # Close the browser
        return price_value
    except Exception as e:
        print(f"Error scraping Amazon: {e}")
        driver.quit()
        return None

def compare_prices(product_name):
    ebay_price = get_ebay_price(product_name)
    amazon_price = get_amazon_price(product_name)
    print("kjbdkajbkjfbkjadb")
    print(ebay_price)
    print(amazon_price)
    print("mnbakvjbs")
    prices = {
        "ebay": ebay_price,
        "amazon": amazon_price
    }

    # Filter out None prices
    prices = {site: price for site, price in prices.items() if price is not None}

    if prices:
        cheapest_site = min(prices, key=prices.get)
        return prices[cheapest_site], cheapest_site
    else:
        return None, None
