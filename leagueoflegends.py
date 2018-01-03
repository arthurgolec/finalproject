#from random import randint
#lets us make the game random

lanes = {"top", "mid", "jungle", "bot", "support"}

toplaners = {"Teemo", "Jax", "Riven", "Darius", "Nasus"}
junglers = {"Warwick", "Evelyn", "Kha'zix", "Zac", "Sejuani"}
midlaners = {"Zed", "Orianna", "Syndra", "Fizz", "Galio"}
botlaners = {"Draven", "Jhin", "Miss Fortune", "Kalista", "Twitch"}
supports = {"Thresh", "Janna", "Nami", "Leona", "Sona"}
#all the champs availible to pick from

carrychampions = {"Janna", "Syndra", "Riven", "Jax", "Twitch", "Draven", "Zed"}
#if the enemy team has any of the above, you pretty much lose

lane_select_1 = input

class MainCharacter(object):
    def __init__(self, name, ability1, ability2, ability3, ultimate, health, mana, ability1mana, ability2mana, ability3mana, ultimatemana, ability1skillshot, ultimateskillshot):
        self.name = name
        self.ability1 = ability1
        self.ability2 = ability2
        self.ability3 = ability3
        self.ultimate = ultimate
        self.mana = mana
        self.ability1mana = ability1mana
        self.ability2mana = ability2mana
        self.ability3mana = ability3mana
        self.ultimatemana = ultimatemana
        self.ability1skillshot = ability1skillshot
        self.ultimateskillshot = ultimateskillshot

class Champion(object):
    """Creates a character in the game with stats"""
    def __init__(self, name, ability1, ability2, ability3, ultimate, health, mana, ability1mana, ability2mana, ability3mana, ultimatemana, ability1skillshot, ultimateskillshot):
        self.name = name
        self.ability1 = ability1
        self.ability2 = ability2
        self.ability3 = ability3
        self.ultimate = ultimate
        self.mana = mana
        self.ability1mana = ability1mana
        self.ability2mana = ability2mana
        self.ability3mana = ability3mana
        self.ultimatemana = ultimatemana
        self.ability1skillshot = ability1skillshot
        self.ultimateskillshot = ultimateskillshot




selection = input("Welcome to the game? Would you like to play?  ").lower()

if selection == "yes" or selection == "y":
    print("Wrong answer, but we'll continue anyways.")
else:
    print("Feelsbadman. Your stuck playing anyways")

laneselect = input('What lane do you wanna play? (type "lanes" for a list of lanes)  ').lower()

while laneselect in lanes != True:
    if laneselect == "lanes":
        print('"top", "mid", "jungle", "bot", "support"')
        laneselect = input("So what lane do you want to play?  ")
    elif laneselect in lanes == True:
        lanes.remove(laneselect)
        break
    if laneselect in lanes !=True:
        laneselect = input("I didn't get that. What lane do you want to play?  ")
