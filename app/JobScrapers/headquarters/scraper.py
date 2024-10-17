from app.JobScrapers.base_scraper import BaseScraper


class HeadquartersScraper(BaseScraper):
    def __init__(self, config):
        super().__init__(config)
        print("HeadquartersScraper __init__ called")
