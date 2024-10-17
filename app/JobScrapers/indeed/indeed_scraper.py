import time
from JobScrapers.base_scraper import BaseScraper
import os
import json

class IndeedScraper(BaseScraper):
    def __init__(self, config):
        super().__init__(config)
        print("IndeedScraper __init__ called")
        self.config = config

        self.indeed_config = {}  # Dictionary to store JSON data
        
        # Get the directory of the current file
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # List all files in the current directory
        for filename in os.listdir(current_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(current_dir, filename)
                with open(file_path, 'r') as json_file:
                    # Load JSON data and store it in the dictionary
                    self.indeed_config[filename.replace(".json", "")] = json.load(json_file)
        print(self.indeed_config)
        self.job_config = self.indeed_config["job_config"]
        self.user_config = self.indeed_config["user_config"]



    def run(self):
        super().class_driver.get(self.job_config["site"])
        time.sleep(2) # let webpage load
        
        # Set Job query
        super().type_text_word_by_word(super().class_driver, self.job_config["search_input_id"], self.job_config["query"])
        # Set location
        super().type_text_word_by_word(super().class_driver, self.job_config["location_input_id"], self.job_config["location"])
        
        super().click_button_natural(super().class_driver, self.job_config["search_button_id"])
        page = super().class_driver.execute_script("return document.documentElement.outerHTML")
        return super().run()
