# import matplotlib.pyplot as plt

# import numpy as np

# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# plt.plot(x, y, label='sin(x)')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Sine Function')
# plt.legend()
# plt.show()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

# Specify the URL to scrape
url = "https://example.com"

# Create a new instance of the Firefox browser
driver = webdriver.Firefox()

# Open the browser and navigate to the URL
driver.get(url)

# Wait for the page to load (you might need to adjust the time based on the page's loading time)
time.sleep(2)

# Perform scraping actions here
# For example, you can find elements by their CSS selectors and extract text
element = driver.find_element_by_css_selector('h1')
print("Page Title:", element.text)

# After scraping, you can perform further actions like clicking buttons, filling forms, etc.
# For example, let's search for something in the page's search bar
search_input = driver.find_element_by_css_selector('input[type="search"]')
search_input.send_keys("search term" + Keys.RETURN)

# Wait for a few seconds to see the result
time.sleep(2)

# Once done, you can close the browser
driver.quit()
