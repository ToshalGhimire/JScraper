
from datetime import datetime
import os
from dateutil import parser
import re
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from logger import Log
from firebase_admin import firestore
import random

from utlits import AppConfig
import selenium as se
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.remote_connection import LOGGER
import time
import logging

LOGGER.setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("selenium").setLevel(logging.WARNING)

# https://googlechromelabs.github.io/chrome-for-testing/
class BaseScraper():
    def class_initWebDriver(config={"debug": True, "is_windows": True}):
        # browser init
        options = se.webdriver.ChromeOptions()
        if(not config["debug"]):
            options.add_argument('headless')
            options.add_argument('--no-sandbox')
            options.add_argument("--disable-gpu")
            options.add_argument('--disable-dev-shm-usage')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        driver = None

        if not config["debug"]:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(current_directory, 'chromedriver_117_prod')
            Log.info(f"Debug={config['debug']} ChromeDriverManager installed in {path}")

            #path = os.path.join(os.getcwd(), "ToshSpot-ATV\\app\\scrapers\\chromedriver.exe")
            service = Service(executable_path=path)
            driver = se.webdriver.Chrome(service=service, options=options)
        else:
            # chromedriver_path = f"{os.getcwd()}/app/chromedriver.exe"
            # print(f"ChromeDriver path: {chromedriver_path}")
            # driver = se.webdriver.Chrome(executable_path=chromedriver_path,options=options)
            current_directory = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(current_directory, 'chromedriver')

            #path = os.path.join(os.getcwd(), "ToshSpot-ATV\\app\\scrapers\\chromedriver.exe")
            Log.info(f"Debug={config['debug']} ChromeDriverManager installed in {path}")
            service = Service(executable_path=path)
            driver = se.webdriver.Chrome(service=service, options=options)
        
        return driver 

    class_driver = class_initWebDriver(AppConfig)

    def __init__(self, config):
        print("__init__ Called")

        
    def run(self):
        print("Run Called")


    def button_click(self, driver, element_id):
        """
        Clicks the button identified by element_id.

        :param driver: Selenium WebDriver instance.
        :param element_id: The id attribute of the button element.
        """
        # Locate the button element by its ID
        button = driver.find_element(By.ID, element_id)
        
        # Click the button
        button.click()

    def click_button_natural(self, driver, button_id,
                         min_delay= 0.2, max_delay = 0.5,
                         move_mouse = True):
        """
        Simulates a natural button click on the button identified by button_id.

        :param driver: Selenium WebDriver instance.
        :param button_id: The id attribute of the button element.
        :param min_delay: Minimum delay before clicking the button (in seconds).
        :param max_delay: Maximum delay before clicking the button (in seconds).
        :param move_mouse: If True, simulates moving the mouse over the button before clicking.
        """
        # Locate the button element by its ID
        try:
            button = driver.find_element(By.ID, button_id)
        except:
            button = driver.find_element(By.CLASS_NAME, button_id)

        
        # Random delay before the action
        time.sleep(random.uniform(min_delay, max_delay))
        
        if move_mouse:
            # Create an ActionChains object
            actions = ActionChains(driver)
            
            # Move to the button element
            actions.move_to_element(button)
            
            # Random small movement to simulate human behavior
            offset_x = random.randint(-5, 5)
            offset_y = random.randint(-5, 5)
            actions.move_by_offset(offset_x, offset_y)
            
            # Pause for a random duration to simulate hesitation
            actions.pause(random.uniform(0.1, 0.3))
            
            # Click the button
            actions.click()
            
            # Perform the actions
            actions.perform()
        else:
            # Directly click the button
            button.click()
    
    def type_text_word_by_word(self, driver, element_id, text, min_delay = 0.1, max_delay = 0.3):
        """
        Types the given text into the input field identified by element_id, word by word.

        :param driver: Selenium WebDriver instance.
        :param element_id: The id attribute of the input element.
        :param text: The text to type into the input field.
        :param delay: Delay between typing each word (in seconds).
        """
        # Locate the input element by its ID
        element = driver.find_element(By.ID, element_id)
        
        # Clear any existing text in the input field
        element.clear()
        
        # Split the text into words
        
        # Type each word followed by a space
        for letter in text:
            element.send_keys(letter)
            time.sleep(random.uniform(min_delay, max_delay))  # Optional delay to simulate typing speed


    