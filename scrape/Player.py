from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#leetify.com
#for now, don't look too far ahead with the gui; focus on gathering player data

"""
    @param driver program's Selenium driver
    @param steamId SteamId of player
    @param name Player name
"""
#driver.find_elements - returns list of elements

class playerMap(object):
    def __init__(self, name, winrate, tScore, ctScore, matchesPlayed):
        self.name = name
        self.winrate = winrate
        self.tScore = tScore
        self.ctScore = ctScore
        self.matchesPlayed = matchesPlayed
        if tScore > ctScore:
            self.bestSide = "t"
        else:
            self.bestSide = "ct"

class Player(object):
    def __init__(self, driver, steamId, name):
        self.name = name
        self.driver = driver
        self.steamId = steamId
        self.playerMaps = []

        # Declare all player stats

        # cstracker
        self.cheatingPercent = None
        self.cheatingRisk = None
        self.accountAge = None
        self.elo = None
        self.kdRatio = None
        self.headshotPercent = None

        # leetify
        self.winrate = None
        self.timeToDamage = None
        self.ctRating = None
        self.tRating = None

        self.aimScore = None
        self.rankAimScore = None

        self.utilitySCore = None
        self.rankUtilitySCore = None

        self.positioningScore = None
        self.rankPositioningScore = None

        self.duelScore = None
        self.rankDuelScore = None

        self.clutchScore = None
        self.rankClutchScore = None

        self.bestMap = None
        self.bestMapSide = None

        self.timeToDamage = None
        self.crosshairPlacement = None


    # scraping stats from cs2tracker.gg
    def getTrackerStats(self):

        self.cheatingRisk = self.driver.find_element(By.CSS_SELECTOR, ".mt-2.metric-label").text
        self.cheatingPercent = self.driver.find_element(By.CSS_SELECTOR, ".gauge-number").text

        accountInfo = self.replaceElementStackWithValue(self.driver.find_elements(By.CSS_SELECTOR, ".mini-value"))
        self.accountAge = int(accountInfo[0])
        self.elo = int(accountInfo[4].strip(","))
        self.headshotPercent = accountInfo[7]
        self.kdRatio = int(accountInfo[6])


    #compares map win rates to find the highest
    def getBestMap(self, maps):
        pass

    #compares t vs ct ratings on best map to find the players best side
    def getBestMapSide(self, maps):
        pass

       # self.accountAge = self.driver.find_element(By.CSS_SELECTOR, ".mini-value").text

    # scraping stats from leetify
    def getLeetifyStats(self):
        self.driver.find_element(By.XPATH, "//*[text()=' All Maps ']").click()
        # pulls things like play scores, map scores, etc.
        scoreStack = self.replaceElementStackWithValue(self.driver.find_elements(By.CSS_SELECTOR, ".value"))

        self.aimScore = scoreStack[0]
        self.utilitySCore = scoreStack[1]
        self.positioningScore = scoreStack[2]
        self.duelScore = scoreStack[3]
        self.clutchScore = scoreStack[4]

        self.rankAimScore = self.replaceElementStackWithValue(self.driver.find_element(By.CSS_SELECTOR, ".benchmark-value.--first.ng-star-inserted"))
        rankScores = self.replaceElementStackWithValue(self.driver.find_elements(By.CSS_SELECTOR, ".benchmark-value.ng-star-inserted"))
        self.rankUtilitySCore = rankScores[0]
        self.rankPositioningScore = rankScores[1]
        self.rankDuelScore = rankScores[2]
        self.rankClutchScore = rankScores[3]

        #winrate, leet rating, ttd, ha, cp, t rating, ct rating, map wr
        advStatWinRate = self.replaceElementStackWithValue(self.driver.find_elements(By.CSS_SELECTOR, ".score-text.ng-star-inserted"))
        self.winrate = advStatWinRate[3]
        self.tRating = advStatWinRate[5]
        self.ctRating = advStatWinRate[6]
        self.timeToDamage = advStatWinRate[1]
        self.crosshairPlacement = advStatWinRate[2]

        mapNameStack = self.replaceElementStackWithValue(self.driver.find_elements(By.CSS_SELECTOR, ".name"))
        mapData = scoreStack[5:len(scoreStack)-5]
        #deletes leetify rating
        del mapData[1::4]

        #create players map data assignments
        for i in range(7,len(advStatWinRate)):
            self.playerMaps.append(playerMap(mapNameStack[i-7],advStatWinRate[i],mapData[1],mapData[2],mapData[0]))
            mapData = mapData[3:]
        for pmap in self.playerMaps:
            print(vars(pmap))


        print(advStatWinRate)
        print(scoreStack)


    # helper to replace elements returned from
    def replaceElementStackWithValue(self, stack):
        values = []
        for el in stack:
            text = el.text.strip()
            if not text:
                values.append(None)  # or raise, or retry
                continue
            cleaned = text.replace(",", "").replace("+", "").replace("%","")
            try:
                values.append(float(cleaned) if "." in cleaned else int(cleaned))
            except ValueError:
                values.append(text)  # keep raw string if it's not numeric (e.g. headshot %)
        return values


    # for developer testing
    def printStats(self):
        print(vars(self))
