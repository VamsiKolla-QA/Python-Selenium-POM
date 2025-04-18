import os
from datetime import datetime

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Utility:
    @staticmethod
    def capture_screenshot(driver, test_name=None):
        """
        Capture a screenshot and save it in the assets/screenshots directory.
        Returns the screenshot as bytes for Allure reporting.
        """
        # -------------------------------
        # Generate a timestamp and build the screenshot filename
        # -------------------------------
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        name = f"{test_name}_{timestamp}" if test_name else f"screenshot_{timestamp}"

        # -------------------------------
        # Create the screenshots directory if it does not exist
        # -------------------------------
        screenshot_dir = os.path.join(os.getcwd(), "assets", "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        # -------------------------------
        # Capture and save the screenshot, then return the path
        # -------------------------------
        screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")

        # -------------------------------
        # Return screenshot as bytes for Allure
        # -------------------------------
        return driver.get_screenshot_as_png()

    @staticmethod
    def wait_for_element_visible(driver, locator, timeout=10):
        """
        Wait until the element specified by the locator is visible.
        """
        # -------------------------------
        # Create a WebDriverWait and wait for the element to become visible
        # -------------------------------
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

