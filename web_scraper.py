from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys

# Set console encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

def run_web_scraper():
    # Set up the WebDriver (Chrome) with automatic ChromeDriver installation
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)  # Create a WebDriverWait instance

    try:
        # Open the target website
        print("Opening website...")
        driver.get("https://srem.moj.gov.sa/realestates-info")

        print("Waiting for search input field...")
        input_field = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[contains(@class, 'ant-select-selection-search-input') and @role='combobox'])[1]")
            )
        )

        # Enter a search value
        print("Entering search term...")
        input_field.send_keys("مدينة الرياض، منطقة الرياض")
        time.sleep(1)  # Wait briefly to mimic natural typing

        # Scroll down to the search button
        print("Scrolling to search button...")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Allow the page to load completely

        # Locate and click the search button
        print("Clicking search button...")
        search_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[span[text()='عرض النتائج']]")
            )
        )
        search_button.click()

        # Wait for the results to load
        print("Waiting for results to load...")
        time.sleep(5)

        # Get and save the page source
        print("Getting page source...")
        data = driver.page_source
        
        # Save to file instead of printing
        with open('search_results.html', 'w', encoding='utf-8') as f:
            f.write(data)
        print("Results saved to search_results.html")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        print("Closing browser...")
        driver.quit()

if __name__ == "__main__":
    run_web_scraper()
