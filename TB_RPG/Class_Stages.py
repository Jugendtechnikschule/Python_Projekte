class Stages():
    def __init__(self, gegner: list, loot: list):
        self.gegner = gegner
        self.loot = loot




    def add_stage(self, gegner, loot):
        self.gegner.append(gegner)
        self.loot.append(loot)
        

        pass
