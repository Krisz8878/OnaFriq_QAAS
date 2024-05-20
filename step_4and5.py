from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import re
import time

# Initialize the WebDriver (replace the path with the location of your Chrome driver)
service = Service("C:/browserdrivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 1. Go to "https://www.automationexercise.com/" and click on Sign-In
driver.get('https://www.automationexercise.com/')
driver.maximize_window()
driver.find_element(By.LINK_TEXT, 'Signup / Login').click()

# Sign-In using following credentials
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-email"]').send_keys('qat@mailinator.com')
driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-password"]').send_keys('123456')
driver.find_element(By.CSS_SELECTOR, 'button[data-qa="login-button"]').click()

wait = WebDriverWait(driver, 20)
# Scroll down to load the "Featured Items" section
driver.execute_script("window.scrollBy(0, 600);")


# 4. Navigate to Women -> Dress -> Women – Tops Products, add Fancy Green Top and Summer White Top to cart
driver.find_element(By.XPATH, "//a[normalize-space()='Women']").click()
driver.find_element(By.CSS_SELECTOR, "a[href='/category_products/1']")
driver.find_element(By.XPATH, "//a[normalize-space()='Tops']")  #.click()

fancy_green_top = driver.find_element(By.XPATH, "//div[@class='features_items']//div[1]//div[1]//div[1]//div[1]//div[1]")
#fancy_green_top.click()
add_to_cart_fancy_green_top = driver.find_element(By.XPATH, "body > section:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(3)")

summer_white_top = driver.find_element(By.XPATH, "//a[@data-product-id='9']")
summer_white_top.click()

# 5. View cart, proceed to checkout, add comments, place order with test card details
driver.find_element(By.LINK_TEXT, "View Cart").click()
driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()

# Add comments
comments_field = driver.find_element(By.CSS_SELECTOR, "textarea[name='message']")
comments_field.send_keys("Order placed.")

# Place order
driver.find_element(By.LINK_TEXT, "Place Order").click()

# Enter card details
name_on_card = driver.find_element(By.CSS_SELECTOR, "input[name='name_on_card']")
name_on_card.send_keys("Test Card")

card_number = driver.find_element(By.CSS_SELECTOR, "input[name='card_number']")
card_number.send_keys("4100000000000000")

cvc = driver.find_element(By.CSS_SELECTOR, "input[name='cvc']")
cvc.send_keys("123")

exp_month = driver.find_element(By.CSS_SELECTOR, "input[name='exp_month']")
exp_month.send_keys("01")

exp_year = driver.find_element(By.CSS_SELECTOR, "input[name='exp_year']")
exp_year.send_keys("1900")

driver.find_element(By.CSS_SELECTOR, "button[data-qa='pay-button']").click()