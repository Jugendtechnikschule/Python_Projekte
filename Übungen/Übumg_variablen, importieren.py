"""übung von variablen, importieren von modulen und funktionen"""

# importieren von modulen
import time
# nur die benötigten module importieren
from random import randint

#localtime() gibt die aktuelle zeit zurück
print(time.localtime())

print("\n")

# variablen
name = "Max"
alter = 15
ist_schule = True
list = [1, 2, 3, 4, 5]
randzahl = randint(1, 100)

print("\n")

# ausgabe von variablen
print(name)
print(alter)
print(ist_schule)
print(list)
print(randzahl)

print("\n")

# verwenden von funktionen
def begruessung(name):
    print("Hallo " + name + "!")

begruessung("Max")

print("\n")

# for-schleife
for i in range(10):
    print(i)

print("\n")







