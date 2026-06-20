"""This module defines the items such as wepons, ... that can be found, crafted and used by the player in the game."""

class items:
    """Items are objects that can be found and used by the player. They can have various effects, such as 
    restoring health or mana, or providing temporary buffs."""

    def __init__(self, name: str, description: str, stackable: bool = True, quality: str = "common"):
        self.name = name
        self.description = description
        self.stackable = stackable
        self.quality = quality

class weapons(items):
    """Weapons are a type of item that can be equipped to increase the player's damage output."""

    def __init__(self,name: str, description: str = "", damage: int = 1, weight: int = 0, equipped: bool = False, durability: int = 100):
        super().__init__(name, description, stackable = False, quality = "common")
        self.damage = damage
        self.weight = weight
        self.equipped = equipped
        self.durability = durability
        
    def equip(self, equipped_wepon):

        equipped_wepon = self

        self.equipped = True
        print(f"You have equipped {self.name}.")

        return equipped_wepon

    def attack(self):
        if self.equipped:
            print(f"You attack with {self.name} for {self.damage} damage.")
            return self.damage
        else:
            print("You are not equipped with a weapon.")
            return 0