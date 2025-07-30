"""
Selenium WebDriver Demo - Login Automation
Author: Muhammad Yasin Asif
Date: July 2025
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LoginAutomation:
    """Selenium automation class for login functionality testing"""
    
    def __init__(self, headless=False):
        """Initialize WebDriver with Chrome options"""
        self.chrome_options = Options()
        
        if headless:
            self.chrome_options.add_argument("--headless")
        
        # Additional options for stability
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--window-size=1920,1080")
        
        # Initialize WebDriver
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        
    def navigate_to_login_page(self, url):
        """Navigate to the login page"""
        try:
            logger.info(f"Navigating to: {url}")
            self.driver.get(url)
            return True
        except Exception as e:
            logger.error(f"Failed to navigate to {url}: {e}")
            return False
    
    def login(self, username, password):
        """Perform login with provided credentials"""
        try:
            # Wait for username field to be present
            username_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.clear()
            username_field.send_keys(username)
            logger.info(f"Entered username: {username}")
            
            # Find and fill password field
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(password)
            logger.info("Entered password")
            
            # Click login button
            login_button = self.driver.find_element(By.ID, "login-btn")
            login_button.click()
            logger.info("Clicked login button")
            
            return True
            
        except TimeoutException:
            logger.error("Timeout waiting for login elements")
            return False
        except NoSuchElementException as e:
            logger.error(f"Element not found: {e}")
            return False
        except Exception as e:
            logger.error(f"Login failed: {e}")
            return False
    
    def verify_successful_login(self):
        """Verify that login was successful"""
        try:
            # Wait for dashboard or success message
            success_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "dashboard"))
            )
            logger.info("Login successful - dashboard loaded")
            return True
        except TimeoutException:
            logger.error("Login verification failed - dashboard not loaded")
            return False
    
    def verify_failed_login(self):
        """Verify that login failed with error message"""
        try:
            error_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
            )
            error_text = error_element.text
            logger.info(f"Login failed as expected: {error_text}")
            return True
        except TimeoutException:
            logger.error("Expected error message not found")
            return False
    
    def take_screenshot(self, filename):
        """Take a screenshot of current page"""
        try:
            self.driver.save_screenshot(f"screenshots/{filename}.png")
            logger.info(f"Screenshot saved: {filename}.png")
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")
    
    def get_page_title(self):
        """Get current page title"""
        return self.driver.title
    
    def close_browser(self):
        """Close the browser"""
        self.driver.quit()
        logger.info("Browser closed")


def test_valid_login():
    """Test successful login with valid credentials"""
    automation = LoginAutomation(headless=True)
    
    try:
        # Navigate to login page
        assert automation.navigate_to_login_page("https://example.com/login")
        
        # Perform login
        assert automation.login("admin", "password123")
        
        # Verify successful login
        assert automation.verify_successful_login()
        
        # Take screenshot
        automation.take_screenshot("successful_login")
        
        logger.info("✅ Valid login test passed")
        return True
        
    except Exception as e:
        logger.error(f"❌ Valid login test failed: {e}")
        automation.take_screenshot("failed_login")
        return False
    finally:
        automation.close_browser()


def test_invalid_login():
    """Test failed login with invalid credentials"""
    automation = LoginAutomation(headless=True)
    
    try:
        # Navigate to login page
        assert automation.navigate_to_login_page("https://example.com/login")
        
        # Perform login with invalid credentials
        assert automation.login("invalid_user", "wrong_password")
        
        # Verify failed login
        assert automation.verify_failed_login()
        
        # Take screenshot
        automation.take_screenshot("failed_login")
        
        logger.info("✅ Invalid login test passed")
        return True
        
    except Exception as e:
        logger.error(f"❌ Invalid login test failed: {e}")
        automation.take_screenshot("test_error")
        return False
    finally:
        automation.close_browser()


def test_empty_credentials():
    """Test login with empty credentials"""
    automation = LoginAutomation(headless=True)
    
    try:
        # Navigate to login page
        assert automation.navigate_to_login_page("https://example.com/login")
        
        # Try to login with empty credentials
        assert automation.login("", "")
        
        # Verify validation error
        assert automation.verify_failed_login()
        
        logger.info("✅ Empty credentials test passed")
        return True
        
    except Exception as e:
        logger.error(f"❌ Empty credentials test failed: {e}")
        return False
    finally:
        automation.close_browser()


def test_login_page_elements():
    """Test that all required login page elements are present"""
    automation = LoginAutomation(headless=True)
    
    try:
        # Navigate to login page
        assert automation.navigate_to_login_page("https://example.com/login")
        
        # Check for required elements
        required_elements = ["username", "password", "login-btn"]
        
        for element_id in required_elements:
            element = automation.driver.find_element(By.ID, element_id)
            assert element.is_displayed()
            logger.info(f"✅ Element {element_id} is present and visible")
        
        logger.info("✅ Login page elements test passed")
        return True
        
    except Exception as e:
        logger.error(f"❌ Login page elements test failed: {e}")
        return False
    finally:
        automation.close_browser()


def run_all_tests():
    """Run all login automation tests"""
    tests = [
        test_valid_login,
        test_invalid_login,
        test_empty_credentials,
        test_login_page_elements
    ]
    
    passed = 0
    total = len(tests)
    
    logger.info(f"🚀 Starting {total} login automation tests...")
    
    for test in tests:
        if test():
            passed += 1
        time.sleep(1)  # Brief pause between tests
    
    logger.info(f"📊 Test Results: {passed}/{total} tests passed")
    
    return passed == total


if __name__ == "__main__":
    # Create screenshots directory if it doesn't exist
    import os
    os.makedirs("screenshots", exist_ok=True)
    
    # Run all tests
    success = run_all_tests()
    
    if success:
        print("🎉 All tests passed!")
    else:
        print("❌ Some tests failed. Check logs for details.") 