from statistics import mean


class Team(object):
    def __init__(self, players):
        # declare all team score averages
        self.players = players
        self.kd = self.getAvg("kdRatio")
        self.headshotPercent = self.getAvg("headshotPercent")
        self.winrate = self.getAvg("winrate")
        self.timeToDamage = self.getAvg("timeToDamage")
        self.ctRating = self.getAvg("ctRating")
        self.tRating = self.getAvg("tRating")
        self.aimScore = self.getAvg("aimScore")
        self.utilityScore = self.getAvg("utilityScore")
        self.positioningScore = self.getAvg("positioningScore")
        self.duelScore = self.getAvg("duelScore")
        self.clutchScore = self.getAvg("clutchScore")

        self.timeToDamage = self.getAvg("timeToDamage")
        self.crosshairPlacement = self.getAvg("crosshairPlacement")
        self.bestMap = self.getBestMapAvg()


    # helper to get averages
    def getAvg(self, var):
        playerVars = []
        for player in self.players:
            playerVars.append(getattr(player, var))
        return mean(playerVars)

    # different syntax for getting bestMap
    def getBestMapAvg(self):
        playerMaps = []
        for player in self.players:
            playerMaps.append(player.bestMap.winrate)
        return mean(playerMaps)
    def printStats(self):
        print(vars(self))
