class mobs:
    def __init__(self, name: str, description: str, hp: int):
        self.name = name
        self.description = description
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount



class enemy(mobs):
    def __init__(self, name: str, description: str, hp: int = 100, mana: int = 100, damage: int = 10, level: int = 1, loot: list = []):
        super().__init__(name, description, hp)
        self.mana = mana
        self.damage = damage
        self.level = level
        self.loot = loot



test_d = {
    "test_d": enemy("Test Enemy", "A test enemy for debugging purposes", hp=100, mana=100, damage=10, level=1, loot=[]),
    "goblin": enemy( "Goblin", "A small, green humanoid creature that is often found in forests and caves.", hp=50, mana=30, damage=5, level=1, loot=["Gold Coin", "Rusty Dagger"])



}