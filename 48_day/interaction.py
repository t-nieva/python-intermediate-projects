from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# active_editors = driver.find_element(By.CSS_SELECTOR, "a[href='/wiki/Special:Statistics']").text
active_editors = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print("Active editors:", active_editors.text)
# active_editors.click()

# Find Search element
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

# driver.quit()
