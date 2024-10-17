import argparse

## argument parsing 
from JobScrapers.indeed.indeed_scraper import IndeedScraper
from utlits import AppConfig


if __name__ == '__main__':
    if AppConfig["is_test"]:
        print(AppConfig)
    else:
        print("Main")
        print(AppConfig)
        IndeedScraper(AppConfig).run()
        

