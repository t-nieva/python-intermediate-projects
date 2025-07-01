from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul.menu li")
upcoming_events = {}
counter = 1
for event in events:
    date = event.find_element(By.TAG_NAME, "time")
    full_date = date.get_attribute("datetime")[:10]
    name = event.find_element(By.TAG_NAME, "a").text
    upcoming_events[counter] = {full_date: name}
    counter += 1
pprint(upcoming_events)

driver.quit()
