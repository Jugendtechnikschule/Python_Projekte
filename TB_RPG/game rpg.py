import random
import time

from Class_Wepons import weapons

#variablen
current_world_level = 1
# character werte
hp = 100
mana = 100
level = 1
xp = 0
#enemy werte
schleim_hp = 100
schleim_mana = 100
enemy_hp = 100
enemy_mana = 100
# waffen auswahl status
sword = weapons("swort", random.randint(5, 15), 5)



Langschwert = True
Schild = False
Mage = False
Dolch = False
Kurtzschwert = False
Bogen = False
Hammer = False
Hammer_eigeschaft = ("stumpf")

wepons = [Langschwert, Schild, Mage, Dolch, Kurtzschwert, Bogen, Hammer]  

# fight status
ran_away = False
fighting = False

print("HP:",hp,"mana:",mana,"level:",level)
geg = 10
def test(lol):
  lol = lol + 1
  print(lol)
  
test(geg)



def wald():
  global user_input
  print("Du bist im Wald")
  print("Du siehst: Einen Baum, Einen Teich und einen schleim")
  user_input = input("Wohin möchtest du gehen?")
  print("baum, teich, schleim(Kampf)")
  if user_input == "baum":
    print("Du gehst zum Baum")
  if user_input == "teich":
    print("Du bist am Teich")
  if user_input == "schleim":
    print("Du kämpfst gegen einen schleim")
    fight()
  
def dorf():
  print("Du bist im Dorf")
def fluss():
  print("Du bist am Fluss")
def gebirge():
  print("du bist im Gebirge")
def enemy_hp_ramp_up():
  global enemy_hp
  enemy_hp = enemy_hp * 1.10
def world_level(enemy_hp, enemy_damage):
  global schleim_hp, current_world_level
  if current_world_level ==  2:
    enemy_hp = enemy_hp * 1.20
    enemy_damage = enemy_damage * 1.20
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
  global hp, mana, xp, enemy_hp, enemy_mana, ran_away, fighting, schleim_hp
  print("You are fighting an enemy!")
  while hp > 0 and enemy_hp > 0 and not ran_away:
    
        print("Your HP:", hp)
        print("Enemy HP:", enemy_hp)
        print("Your Mana:", mana)
        print("Enemy Mana:", enemy_mana)
        print("What do you want to do?")
        print("1. Attack")
        print("2. Use item")
        print("3. Run away")
        choice = input("Enter your choice: ")
        if choice == "1":
          if Langschwert:
            damage = random.randint(10, 20)
            enemy_hp -= damage
            print("You attacked the enemy with your Langschwert and dealt", damage, "damage!")
          elif Schild:
            damage = random.randint(5, 10)
            enemy_hp -= damage
            print("You attacked the enemy with your Schild and dealt", damage, "damage!")
          elif Mage:
            damage = random.randint(15, 25)
            enemy_hp -= damage
            mana -= 10
            print("You attacked the enemy with your Mage and dealt", damage, "damage!")
          elif Dolch:
            damage = random.randint(5, 10)
            enemy_hp -= damage
            print("You attacked the enemy with your Dolch and dealt", damage, "damage!")
          elif Kurtzschwert:
            damage = random.randint(5, 10)
            enemy_hp -= damage
            print("You attacked the enemy with your Kurtzschwert and dealt", damage, "damage!")
          elif Bogen:
            damage = random.randint(5, 10)
            enemy_hp -= damage
            print("You attacked the enemy with your Bogen and dealt", damage, "damage!")
          else:
            print("You don't have a weapon equipped.")
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
  global hp, mana, enemy_hp, enemy_mana, level, Langschwert, Schild, Mage, Tank, Dolch, Kurtzschwert, Bogen, xp, xp_level_up, fighting
  print("spiel beginnt")
  print("Wähle deine Waffe:")
  print("Langschwert=1")
  print("Schild=2")
  print("Mage=3")
  print("Dolch=5")
  print("Kurtzschwert=6")
  print("Bogen=7")
  print("Hammer=8")
  
  user_input = input("Wähle einen character aus")
  if user_input == "1":
    print("Du hast den Langschwert gewählt")
    Langschwert = True
  elif user_input == "2":
    print("Du hast den Schild gewählt")
    Schild = True
  elif user_input == "3":
    print("Du hast den Mage gewählt")
    Mage = True
  elif user_input == "4":
    print("Du hast den Tank gewählt")
    Dolch = True
  elif user_input == "6":
    print("Du hast den Kurtzschwert gewählt")
    Kurtzschwert = True
  elif user_input == "7":
    print("Du hast den Bogen gewählt")
    Bogen = True
  elif user_input == "8":
    print("Du hast den Hammer gewählt")
  else:
    print("ungültige eingabe")
    

print("Du bist auf einer wiese.In einer anderen welt")
print("Du siehst: Einen Wald, Ein Dorf, Ein Fluss und Ein Gebirge")
user_input = input("Wohin möchtest du gehen?")
print("wald, Dorf, Fluss, Gebirge")

if user_input == "Wald" or "wald":
  print("Du gehst in den Wald")
  wald()
elif user_input == "Dorf" or "dorf":
  print("Du gehst in das Dorf")
  dorf()
elif user_input == "Fluss" or "fluss":
  print("Du gehst zum Fluss")
  fluss()
elif user_input == "Gebirge" or "gebirge":
  print("Du gehst in das Gebirge")
  gebirge()
else:
  print("ungültige eingabe")
if user_input == "f":
    fight()
    print("kampf zu ende")
if xp == 100:
    level_up()
    xp = 0
if __name__ == "__main__":
  print("name=main")
  main()
  print("fertig")