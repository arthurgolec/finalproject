import random
import time
#lets us make the game random

lanes = ["top", "mid", "jungle", "bot", "support"]
usernames = ["t1", "solofeed", "aniviabot", "urmomhahaha", "CodySimpsonFan", "jgorfeed", "epicwin", "hashinshin", "dardoch"]


class Player(object):
    """The player's stats throughout the game"""
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


pusername = input("Hey! Before we get started, what is your username?  ")
print("Ok, loading...")
time.sleep(2.5)

selection = input("Welcome to the game? Would you like to play?  ").lower()

if selection == "yes" or selection == "y":
    print("Wrong answer, but we'll continue anyways.")
else:
    print("Feelsbadman. Your stuck playing anyways")
#just a way to start off the game

laneselect = input('What lane do you wanna play? (type "lanes" for a list of lanes)  ').lower()

while True:
    if laneselect == "lanes":
        print('"top", "mid", "jungle", "bot", "support"')
        laneselect = input("So what lane do you want to play?  ")
    elif laneselect in lanes:
        print("Got it, searching for game")
        lanes.remove(laneselect)
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        break
    else:
        laneselect = input("I didn't get that. What lane do you want to play?  ")
#way to choose a lane to play in, actually just makes you autfill

playeractuallane = random.choice(lanes)
print(f"Ah, narts, you got autofilled to {playeractuallane}. Unfortunate!")

print("loading team chat.....")
time.sleep(5)
print("""







_____________________________________________________
""")
#makes a space showing chat log prompt

print(f"-->{random.choice(usernames)} ~ hey guys! glhf")

time.sleep(.5)
print(f"""-->{random.choice(usernames)} ~ {playeractuallane} or i feed

""")

game_dodge_decision = input("Uh oh, a player is planning on inting. Do you want to leave and find another match or stay and wait it out?")
while True:
    if game_dodge_decision == "leave" or "leave and find another match" or "find another match":
        leave_game_decision = input("Are you sure? You already left a few matches, so leaving now would result in a 20 minute ban.").lower()
        if leave_game_decision == "yes" or "y":
            print("Ok, leaving match")
            time.sleep(2)
            print("Welcome back to the game? Would you like to play?")
            print("Of course you do, lets find you a game")
            print("before that, we have to find you another lane")
            laneselect1 = input("So what lane do you want to play?  ")
            while True:
                if laneselect1 == "lanes":
                    print('"top", "mid", "jungle", "bot", "support"')
                    laneselect1 = input("So what lane do you want to play?  ")
                elif laneselect1 in lanes:
                    print("Got it, searching for game")
                    lanes.remove(laneselect1)
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("...")
                    break
                else:
                    laneselect1 = input("I didn't get that. What lane do you want to play?  ")
                for x in range(20):
                    print(f"{x} minutes have passed. {20-x} minutes remaining")
                    for x in range(4): #this will show a ... every 15 seconds of waiting
                        time.sleep(15)
                        print("...")
                #this is going to show the 20 minute ban for leaving the game
        if leave_game_decision == "no" or "n":
            print("Ok, good call")
            break
            #now the player goes back to the main game
        else:
            leave_game_decision = input("Sorry, didn't get that. Type 'yes' to leave or 'no' to stay. ")
    if game_dodge_decision == "stay" or "stay and wait it out" or "wait it out":
        print("Good call, carry on")
        break
    else:
        game_dodge_decision = input("Sorry, i didn't get that. Type 'leave' to leave or 'stay' to stay")



