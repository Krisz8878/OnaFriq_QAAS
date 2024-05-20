import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

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

# Wait for the landing page to load completely
wait = WebDriverWait(driver, 20)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".features_items .col-sm-4")))

# Scroll down to load the "Featured Items" section
driver.execute_script("window.scrollBy(0, 600);")

# 4. Navigate to Women -> Dress -> Women – Tops Products, add Fancy Green Top and Summer White Top to cart
driver.find_element(By.LINK_TEXT, 'WOMEN').click()
#driver.find_element(By.XPATH, '//div[@id="Women"]//a[contains(text(),"Dress")]').click()
driver.find_element(By.XPATH, '//a[normalize-space()="Tops"]')
#driver.find_element(By.LINK_TEXT, 'Women - Tops').click()

# Add Fancy Green Top to cart
fancy_green_top = driver.find_element(By.XPATH, '//div[@class="overlay-content"]//p[contains(text(),"Fancy Green Top")]')
driver.execute_script("arguments[0].scrollIntoView(true);", fancy_green_top)
time.sleep(2)  # Adding a small delay to ensure the element is fully scrolled into view
fancy_green_top = driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[2]/div/div[6]/div/div[1]/div[2]/div/a')
fancy_green_top.click()

# Add Summer White Top to cart
summer_white_top = driver.find_element(By.XPATH, '//a[contains(text(),"Summer White Top")]')
driver.execute_script("arguments[0].scrollIntoView(true);", summer_white_top)
time.sleep(2)  # Adding a small delay to ensure the element is fully scrolled into view
summer_white_top = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(),"Summer White Top")]')))
summer_white_top.click()

# Close window
driver.quit()

