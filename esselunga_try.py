from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import time


driver = webdriver.Chrome()
driver.get("https://www.esselunga.it/it-it/promozioni/volantini/volantino-digitale.sconto-40.sol.1713.html")


wait = WebDriverWait(driver, 10)
accept_cookies_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "accept-all-btn")))

# Click the "Accept All" button
accept_cookies_button.click()

start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    
    # Break the loop after 60 seconds
    if elapsed_time > 60:
        print("Finished running the loop for a minute.")
        break
    
    try:
        # Find buttons by class name
        buttons = driver.find_elements(By.CLASS_NAME, 'load-more-products-btn')
        
        if not buttons:
            print("No more 'Load More' buttons found.")
            break
        
        for button in buttons:
            # Click the button
            driver.execute_script("arguments[0].click();", button)
            
    except NoSuchElementException:
        # No more buttons found, exit the loop
        print("No more 'Load More' buttons to click.")
        break



# Close the driver

 
card_items = driver.find_elements(By.CLASS_NAME, "card-item")
for item in card_items:
    try:
        # Attempt to find the product title element
        title_element = item.find_element(By.CSS_SELECTOR, ".card-top p")
        title = title_element.get_attribute("title") if title_element.get_attribute("title") else "No Title"

        # Attempt to find the promo price element
        promo_price_element = item.find_element(By.CSS_SELECTOR, ".card-price .promo-price span")
        promo_price = promo_price_element.text if promo_price_element else "No Promo Price"
        
        # Attempt to find the regular price element
        price_element = item.find_element(By.CSS_SELECTOR, ".card-price .price span")
        price = price_element.text if price_element else "No Regular Price"
        
        print(f"Title: {title}, Promo Price: €{promo_price}, Regular Price: €{price}")
    except NoSuchElementException:
        # Skip this item if any element is missing
        continue