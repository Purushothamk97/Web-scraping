from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Assuming you have a WebDriver instance (e.g., ChromeDriver) set up
driver = webdriver.Chrome()

# Navigate to YouTube
driver.get("https://www.youtube.com/")

# Find the search bar using an explicit wait
search_bar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "search_query"))
)

# Perform a search
search_bar.send_keys("stem astronomy calendar")

driver.find_element(By.ID,'search-icon-legacy').click()
# Keep the browser window open
input("Press Enter to close the browser...")

# Close the browser window
driver.quit()
