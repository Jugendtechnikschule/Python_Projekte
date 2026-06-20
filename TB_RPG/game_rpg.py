import random

from Class_Items import items, weapons
from Class_Mobs import enemy

#variablen
current_world_level = 1
# character werte
hp = 100
mana = 100
level = 1
xp = 0
inventory = []
#enemy werte
goblin = enemy("Goblin", "Ein kleiner, grüner Goblin")

enemy_hp = goblin.hp
enemy_mana = goblin.mana
enemy_damage = goblin.damage

# waffen auswahl status

equipped_wepon = hand = weapons("Hand", "Deine bloßen Hände", 1, 0, True)
 
sword = weapons("Schwert", "Ein simples Schwert", random.randint(5, 15), 5)
Langschwert = weapons("Langschwert", "Ein langes Schwert", random.randint(10, 20), 10)
Schild = weapons("Schild", "Ein schweres Schild", random.randint(5, 10), 15)
Mage = weapons("Mage", "Ein Zaubererstab", random.randint(15, 25), 5)
Dolch = weapons("Dolch", "Ein kleiner Dolch", random.randint(5, 10), 3)
Kurtzschwert = weapons("Kurtzschwert", "Ein kurzes Schwert", random.randint(5, 10), 7)
Bogen = weapons("Bogen", "Ein langen Bogen", random.randint(5, 10), 8)
Hammer = weapons("Hammer", "Ein schwerer Hammer", random.randint(10, 20), 12)
Not_defind_Weapon = weapons("Not defind Weapon", "Ein nicht definierte Waffe")

wepon_list = [sword, Langschwert, Schild, Mage, Dolch, Kurtzschwert, Bogen, Hammer, Not_defind_Weapon]
# fight status
ran_away = False
fighting = False

print("Link Start!")
print("HP:",hp,"mana:",mana,"level:",level)

def create_enemy(amount):
  global enemy_list
  enemy_list = []
  for i in range(amount):
    enemy_list.append(enemy(f"enemy{i}" ,f"Ein feindlicher Mob Nr.{i}"))
    print(enemy_list[i].name, "wurde erstellt mit", enemy_list[i].hp, "HP und", enemy_list[i].mana, "Mana.")
  print(enemy_list)


def enemy_hp_ramp_up():
  global enemy_hp
  enemy_hp = enemy_hp * 1.10
def world_level(enemy_hp, enemy_damage):
  global schleim_hp, current_world_level
  if current_world_level ==  2:
    enemy_hp *= 1.20
    enemy_damage *= 1.20
    print("World level:", current_world_level)    
def level_up():
    global level, hp, mana
    level += 1
    hp = min(int(hp * 1.10), 10**18)
    mana = min(int(mana * 1.10), 10**18)
    print("You leveled up!")
    print("You're now level", level)
    print("HP:", hp)
    print("Mana:", mana)
def fight():
  global hp, mana, xp, enemy_hp, enemy_mana, ran_away, fighting, schleim_hp, equipped_wepon
  print("You are fighting an enemy!")
  while hp > 0 and enemy_hp > 0 and not ran_away:
    
        print("Your HP:", hp)
        print("Enemy HP:", enemy_hp)
        print("Your Mana:", mana)
        print("Enemy Mana: nich da sorry")
        print("What do you want to do?")
        print("1. Attack")
        print("2. Use item")
        print("3. Run away")
        choice = input("Enter your choice: ")
        if choice == "1":
          damage = equipped_wepon.attack()
          enemy_hp -= damage
        elif choice == "2":
          print("Which item do you want to use?")
          print("1. Health Potion")
          print("2. Mana Potion")
          item_choice = input("Enter your choice: ")
          if item_choice == "1":
              if hp < 100:
                  hp += 20
                  print("You used a Health Potion and restored 20 HP!")
              else:
                    print("You already have full HP!")
          elif item_choice == "2":
            if mana < 100:
              mana += 20
              print("You used a Mana Potion and restored 20 mana!")
            else:
              print("You already have full mana!")
          else:
            print("Invalid choice.")
        elif choice == "3":
          print("You ran away from the battle.")
          ran_away = True
        if enemy_hp > 0 and not ran_away:
            enemy_damage = random.randint(5, 15)
            hp -= enemy_damage
            print("The enemy attacked you and dealt", enemy_damage, "damage!")
        if hp <= 0:
            print("You died!")
        elif enemy_hp <= 0:
          print("You won the battle!")
          print("You defeated the enemy!")
          earned_xp = 100
          xp += earned_xp
   

def main():
  global hp, mana, enemy_hp, enemy_mana, level, Langschwert, Schild, Mage, Tank, Dolch, Kurtzschwert, Bogen, xp, xp_level_up, fighting, equipped_wepon
  print("spiel beginnt")
  
user_input = input("Wähle(f, xp(+100), c(create enemy))")
if user_input == "f":
  fight()
  print("kampf zu ende")
elif user_input == "xp":
  xp += 100
elif user_input == "c":
  create_enemy(5)
if xp == 100:
  level_up()
  xp = 0
if __name__ == "__main__":
  print("name=main")
  main()
  print("fertig")