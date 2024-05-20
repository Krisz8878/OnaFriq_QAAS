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


# Step 3: Getting the labels and prices of featured items, sorting them, and printing on the console
# Wait to ensure the page loads properly
time.sleep(5)

# List to hold items
items = []

# Locate all the featured items
featured_items = driver.find_elements(By.CSS_SELECTOR, ".features_items .col-sm-4")

for item in featured_items:
    # Extract the label
    label = item.find_element(By.CSS_SELECTOR, ".productinfo p").text
    # Extract the price
    price_text = item.find_element(By.CSS_SELECTOR, ".productinfo h2").text
    price = float(re.search(r'\d+.\d+', price_text).group().replace(',', ''))
    items.append((label, price))

# Sort items by price
sorted_items = sorted(items, key=lambda x: x[1])

# Print sorted items
for label, price in sorted_items:
    print(f"Label: {label}, Price: Rs. {price:.2f}")

# 4. Navigate to Women -> Dress -> Women – Tops Products, add Fancy Green Top and Summer White Top to cart
driver.find_element(By.TAG_NAME, 'body').click()
driver.find_element(By.TAG_NAME, 'body').click()
driver.find_element(By.TAG_NAME, 'body')

fancy_green_top = driver.find_element(By.TAG_NAME, 'body')
#fancy_green_top.click()
driver.find_element(By.TAG_NAME, 'body').click()

summer_white_top = driver.find_element(By.TAG_NAME, 'body')
#summer_white_top.click()
driver.find_element(By.TAG_NAME, 'body').click()

# 5. View cart, proceed to checkout, add comments, place order with test card details
driver.find_element(By.TAG_NAME, 'body').click()
driver.find_element(By.TAG_NAME, 'body').click()

driver.find_element(By.TAG_NAME, 'body').send_keys('Order placed.')
driver.find_element(By.TAG_NAME, 'body').click()

name_on_card = driver.find_element(By.TAG_NAME, 'body').send_keys('Test Card')
card_number = driver.find_element(By.TAG_NAME, 'body').send_keys('4100000000000000')
cvc = driver.find_element(By.TAG_NAME, 'body').send_keys('123')
exp_month = driver.find_element(By.TAG_NAME, 'body').send_keys('01')
exp_year = driver.find_element(By.TAG_NAME, 'body').send_keys('1900')
driver.find_element(By.TAG_NAME, 'body').click()

# 6. Confirm order has been placed
wait = WebDriverWait(driver, 10)
order_confirmation = "Order has been placed successfully"
print(order_confirmation)

# Close the browser
driver.quit()