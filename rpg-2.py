import random
import math

class  Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health 
        self.power = power
    
    def attack(self, power):
        self.power = power
    
    def d_dmg(self, power):
        self.power = Hero.power * (2)
   
    def alive(self, health):
        self.health > 0

    def health_status(self):
        print ("{}'s Health: {}, {}'s Power: {}".format(self.name, self.health, self.name, self.power))

Goblin = Character("Goblin", 20, 2)
Hero = Character("Hero", 100, 5)
Zombie = Character("Zombie", 100000, 1)
Medic = Character("Medic", 50, 1)

while Goblin.alive and Hero.alive and Zombie.alive: 
    Goblin.health_status()
    Hero.health_status()
    Zombie.health_status()
    Medic.health_status()
    print("You, the Hero and a Medic encounter a zombie, and goblin make a move:\n")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("4. fight zombie bad choice")
    print("> ",)
    user_input = input()
    if user_input == "1":
            # Hero attacks goblin
        Goblin.health -= Hero.power
        print("You did %d damage to the goblin." % Hero.power)

        if random.randrange(0,100) < 20:
            Hero.power = 10
       
        elif Hero.power == 10: 
            Hero.power = 5    
        
        if Goblin.health > 0:
        # Goblin attacks hero
            Hero.health -= Goblin.power
            print(" ")
            print("The goblin does %d damage to you." % Goblin.power)

        
        if random.randrange(0,100) < 20:
            while Hero.health < 100:
                Medic.health - 2 and Hero.health + 2
            continue
            


        if Hero.health <= 0:
            print(" ")
            print("Hero's Health: 0")
            print("You are dead.")
            break

        if Goblin.health <= 0:
            print(" ")
            print("Goblin's Health: 0")
            print("The goblin is dead.")
            break

    elif user_input == "2":
            print(" ")
            print("You stand there and watch the Zombie and Goblin hangout.")
            print(" ")
            pass

    elif user_input == "3":
            print(" ")
            print("Goodbye.")
            break

    elif user_input == "4":
        print(" ")
        Zombie.health -= Hero.power
        print("You did %d damage to the Zombie." % Hero.power)

        if random.randrange(0,100) < 20:
            Hero.power = 10
       
        elif Hero.power == 10: 
            Hero.power = 5    
        

        if Zombie.health > 0:
        # Goblin attacks hero
            Hero.health -= Zombie.power 
            print(" ")
            print("The zombie does %d damage to you." % Zombie.power)

        if random.randrange(0,100) < 20:
            while Hero.health < 100:
                Medic.health - 2 and Hero.health + 2
            continue

        if Hero.health <= 0:

            print(" ")
            print("Hero's Health: 0")
            print("You are dead.")
            break

        if Zombie.health <= 0:
            print(" ")
            print("Zombie's Health: 0")
            print("The Zombie is dead.")
            break
    else:
            print("Invalid input %r" % user_input)


# MEDIC NOT WORKING RIGHT NOW --- PUSHING TO GITHUB AS OF NOW THO 