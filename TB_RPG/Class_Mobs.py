class mobs:
    def __init__(self, name: str, description: str, hp: int):
        self.name = name
        self.description = description
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount
class enemy(mobs):
    def __init__(self, name: str, description: str, hp: int = 100, mana: int = 100, damage: int = 5, level: int = 1, loot: list = []):
        super().__init__(name, description, hp)
        self.mana = mana
        self.damage = damage
        self.level = level
        self.loot = loot

