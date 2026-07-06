import time

from selenium.webdriver.support.wait import WebDriverWait

from Player import Player
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




class statScraper(object):
    """
    @param steamIds list of Steam ID's for all players in match (besides you)
    """
    def __init__(self, steamIds):
        self.service = Service(driver_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.steamIds = steamIds
        #headers for links to scrape
        self.leetify = "https://leetify.com/app/profile/"
        self.cs2tracker = "ttps://cs2tracker.gg/stats/"

        # initialize
        self.driver.get("https://leetify.com/app/profile/76561199103680570")

        p = Player(self.driver, self.steamIds, "")
        time.sleep(15)
        p.getLeetifyStats()
        p.printStats()




statScraper("")
