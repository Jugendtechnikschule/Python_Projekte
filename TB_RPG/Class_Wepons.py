class weapons():
    def __init__(self, name:str, damage:int, weight:int, equipped:bool=False, durability:int=100):
        self.name = name
        self.damage = damage
        self.weight = weight
        self.equipped = equipped
        self.durability = durability

    def equip(self):
        self.equipped = True
        print(f"You have equipped {self.name}.")
    def unequip(self):
        self.equipped = False
        print(f"You have unequipped {self.name}.")