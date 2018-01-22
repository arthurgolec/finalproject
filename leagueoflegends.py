import random
#rng ftw
from random import randint
#more random stuff
import time
#make pauses inbetween text with time.sleep(seconds)
from threading import Timer
#makes a section of the game timed
import sys

lanes = ["top", "mid", "jungle", "bot", "support"]
#lanes to choose from in the game

class Teammate:
    """makes the teammates used in the game, v basic"""
    def __init__(self, username, champion, lane):
        self.username = username
        self.champion = champion
        self.lane = lane

player1 = Teammate("sorakamain1", "soraka", "support")
player2 = Teammate("tyler1", "draven", "bot")
player3 = Teammate("shiptur", "azir", "mid")
player4 = Teammate("peanut", "sejuani", "jungle")
player5 = Teammate("hashinshin", "jax", "top")

def gameover(player):
    """this function ends the game, taking the "player" arguement, which shows the player that ruined it"""
    print("""*for the entirety of the game, {player.champion} runs it down mid, a trademark move of his.
there is nothing you can do and your nexus turrets die within minutes.
your nexus dies shortly after""")
    time.sleep(10)
    print("the end")
    time.sleep(5)
    sys.exit()


def dodge():
    """this function is what happens when the player leaves the game, shows how the player has to go through champ-select and the ban again"""
    print("Welcome back to the game? Would you like to play?")
    time.sleep(.75)
    print("Of course you do, lets find you a game")
    time.sleep(2)
    print("before that, we have to find you another lane")
    laneselect1 = input("So what lane do you want to play?  ")
    while True:
        if laneselect1 == "lanes":
            print('"top", "mid", "jungle", "bot", "support"')
            laneselect1 = input("So what lane do you want to play?  ")
        elif laneselect1 in lanes:
            print("Got it, searching for game")
            lanes.remove(laneselect1)
            #takes out the players lane from the lanes to be given
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


pusername = input("Hey! Before we get started, what is your username?  ")
print("Ok, loading...")
time.sleep(2.5)

selection = input("Welcome to the game? Would you like to play?  ").lower()

if selection == "yes" or selection == "y":
    print("Wrong answer, but we'll continue anyways.")
else:
    print("Feelsbadman. Your stuck playing anyways")
#just a way to start off the game, has no true effect on outcome


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

time.sleep(2)
print(f"-->{player1.username} ~ hey guys! glhf")

time.sleep(1.5)
print(f"""-->{player2.username} ~ {player2.lane} or i feed
""")

print("""
_____________________________________________________
""")
#shows one player being a doodie face using teammates class

game_dodge_decision = input("Uh oh, a player is planning on inting. Do you want to leave and find another match or stay and wait it out?  ").lower()
while True:
    if game_dodge_decision == "leave" or game_dodge_decision == "leave and find another match" or game_dodge_decision == "find another match":
        leave_game_decision = input("Are you sure? You already left a few matches, so leaving now would result in a 20 minute ban.  ").lower()
        if leave_game_decision == "yes" or leave_game_decision == "y":
            print("Ok, leaving match")
            time.sleep(2)
            dodge()
            #if the player leaves, dodge runs and makes the player go through a 20 minute ban
        elif leave_game_decision == "no" or leave_game_decision == "n":
            print("Ok, good call")
            break
            #now the player goes back to the main game
        else:
            leave_game_decision = input("Sorry, didn't get that. Type 'yes' to leave or 'no' to stay.  ")
    if game_dodge_decision == "stay" or "stay and wait it out" or "wait it out":
        print("Good call, carry on")
        break
        #continues the game
    else:
        game_dodge_decision = input("Sorry, i didn't get that. Type 'leave' to leave or 'stay' to stay")

time.sleep(2)

print("""
_____________________________________________________
""")

print(f"-->{player3.username} ~ {player2.username} plz kys")
time.sleep(2.3)
print(f"-->{player1.username} ~ fine just give it to him")
time.sleep(1.4)
print("""
_____________________________________________________
""")
playertext1 = input("Say something mean to this guy!  ")
print("""
_____________________________________________________
""")
print(f"-->{pusername} ~ {playertext1}")
time.sleep(2)
print(f"-->{player2.username} ~ if someone says one more thing i run it down mid")
print("""
_____________________________________________________
""")
print("oh, narts, you were talking too much and forgot to pick a champion!")
time.sleep(5)
print("the champions that you can choose are:")
time.sleep(2)
print("""
Teemo
Riven
Sejuani
Kha'Zix
Azir
LeBlanc
Draven
Xayah
Tahm Kench
Alistar
""")

pickablechampions = ("teemo", "riven", "sejuani", "kha'zix", "azir", "leblanc", "draven", "tahm kench", "alistar")
#used in champselect to test for a valid input


time.sleep(1.5)

timeout = 4
t = Timer(timeout, print, ['Sorry, times up. You dodged'])
t.start()
prompt = "You have %d seconds to pick a champion...\n" % timeout
championselected = input(prompt).lower()
if championselected not in pickablechampions:
    print("DIDN'T GET THAT!!!")
t.cancel()
print("you picked one in time. phew, that was close!")


#this times you when you try and choose a champion to simulate the player getting distracted


if championselected not in pickablechampions:
    print("wow, time to search for a new match")
    dodge()

print("ok, loading game...")

badcomputerkid = randint(0,100)
if badcomputerkid == 2:
    print("oh no, someone has a bad computer in this game. This is gonna take a reeeeeeeallly take a long time to load")
    time.sleep(420)
#sometimes someone has a bad computer, and this simulates that bad computer kid taking 7 minutes to load in
for x in range(5):
    time.sleep(2)
    print("...")
print("game has loaded!")
time.sleep(1.7)


dravenint = input('uh oh. remember that draven from before? he started 5 pots and 2 control wards. do you want to "bm" him?  ').lower()
if dravenint == "yes" or dravenint == "y":
    bmmethod = input('so would you prefer to spam "?" or ping his items?').lower()
    while True:
        if bmmethod == "spam ?" or bmmethod == "?" or bmmethod == "spam":
            for x in range(6):
                print("?")
                time.sleep(.2)
            print(f"{(player).username} ~ *** this game. i hate all of you and i dont care anymore")
            time.sleep(2)
            print("oh no, you made the wrong call! draven sold all of his items and bought boots. i wonder why")
            time.sleep(2)
            gameover(player1)

        elif bmmethod == "ping items" or "ping" or "items":
            for x in range(6):
                print('"Draven(tyler1) - Health Potion (5)"')
                time.sleep(.2)
                print('"Draven(tyler1) - Control Ward (3)"')
                time.sleep(.2)
            print(f"{(player).username} ~ *** this game. i hate all of you and i dont care anymore")
            time.sleep(2)
            print("oh no, you made the wrong call! draven sold all of his items and bought boots. i wonder why")
            time.sleep(2)
            gameover(player1)
#this ends the game after printing what ends up happening, the second part is just how it looks not what happens
        else:
            bmmethod = input('sorry, i didn\'t get that. type "spam" to spam "?" at him or "ping" to ping his items')
            continue
else:
    print("good call, i think its not a good idea to get on this guy's nerves")
#first gameplay decision, whether the player wants to tilt his teammates

time.sleep(2)

if playeractuallane == "jungle":
    #gives gameplay decision based on what lane they play
    print("ok, as a jungler, you want a leash")
    time.sleep(2)
    print("you walk towards your red buff, but your bot doesnt come to help you")
    playerdecision2 = input("Do you ping your bot to help you?  ").lower()
    if playerdecision2 == "y" or playerdecision2 == "yes":
        print("your bot lane doesnt come.")
        playerdecision3 = input("Do you int or do you solo the red buff?  ").lower()
        while True:
            if playerdecision3 == "int":
                print("good call. you go to base, sell all your items, and buy boots.")
                time.sleep(2)
                print(f"you show the bot lane who's boss by running it down bot lane while spamming {championselected}'s mastery emote")
                time.sleep(5)
                print("gg")
                sys.exit()
                #ends the game for the team not helping the player
            elif playerdecision3 == "solo" or playerdecision3 == "solo it" or playerdecision3 == "solo the red buff" or playerdecision3 == "solo red buff":
                print("you get the red buff down to 600 hp, then get you red buff invaded by the enemy jungle and bot lane. you die")
                time.sleep(5)
                print("you then decide to go to your blue buff, only to get killed and have your blue stolen again.")
                time.sleep(5)
                print("your bot lane starts bm-ing you in chat")
                print(f"'/all {player1} ({player1.champion}) ~ gg'")
                print(f"the other two players, {player3} and {player4} also lose because their lanes were camped all game")
                gameover(player1)
                #ends the game because the team didn't help
            else:
                playerdecision3 = input("sorry, i didnt get that. type 'int' to int or 'solo' to solo the red buff")
    elif playerdecision2 == "no" or playerdecision2 == "n":
        print("you get the red buff down to 600 hp, then get you red buff invaded by the enemy jungle and bot lane. you die")
        time.sleep(2)
        print("you then decide to go to your blue buff, only to get killed and have your blue stolen again.")
        time.sleep(2)
        print("your bot lane starts bm-ing you in chat")
        time.sleep(1.5)
        print(f'"/all {player1}({player1.champion}) ~ gg"')
        time.sleep(1.2)
        print(f"the other two players, {player3} and {player4} also lose because their lanes were camped all game")
        gameover(player1)
        #the team loses because you died too early on
    else:
        playerdecision2 = input("sorry, i didnt get that. type 'yes' to ping or 'no' to not ping").lower()
#if you get jungle, you lose, #second decision in the game, deciding whether to leash the jungler

elif playeractuallane == "bot" or playeractuallane == "support":
    print("as you start walking to lane, you jungle pings for a leash")
    time.sleep(3)
    playerdecision4 = input("do you go and leash him?  ").lower()
    if playerdecision4 == "yes" or playerdecision4 == "y":
        print("you go to leash him and all goes well. nice!")
        #if the player helps, the game continues
    elif playerdecision4 == "no" or playerdecision4 == "n":
        playerdecision5 = input('uh oh, the jungler is continuing to ping "?" on you. are you sure you dont want to leash him?  ').lower()
        if playerdecision5 == "y" or playerdecision5 == "yes":
            print("wow, you suck")
            print("your jungler recalls and sells all his items. what ever may he do?")
            print(f"he buys boots and runs it down {playeractuallane}")
            print("because of your jungler, you lose your lane, and unfortunately, so do all other lanes")
            gameover(player4)
            #player loses for not helping the team
    else:
        print("you leash him anyways, making the jungler happy :)")
#second decision in the game, deciding whether to leash the jungler
else:
    print("wow, you go to lane and no one ints!")
#if the player gets top or mid, the game just continues

time.sleep(3)

print("you get to lane and come up against your worst counter - a good yasuo")

#i'm sorry, the part below is kind of disgusting

lanedecision1 = input("do you want to trade with the yasuo or just cs?  ").lower()
while lanedecision1 != "trade" or lanedecision1 != "trade with the yasuo" or lanedecision1 != "cs" or lanedecision1 != "just cs":
    #makes it so the game doesn't progress until a valid input is given
    if lanedecision1 == "trade" or lanedecision1 == "trade with the yasuo":
        print("oh no, you missed your ability!")
        print("yasuo hit lvl2 in the middle of the fight, which caused you to go down to 15% health.")
        junglehelp = input("you realize that you need some help. do you want to recall without having teleport ready or do you want to ping your jungler?  ").lower()
        if junglehelp == "recall":
            print("you try to recall under tower, but by the point you made that decision, yasuo had already shoved the wave under tower")
            time.sleep(2)
            print("during the last 2 seconds of your recall, yasuo flash-e-q-aa-ignites you, causing you to die")
            time.sleep(2)
            print("yasuo has also died, but it was an execute #feelsbadman (i.e. no gold for you)")
            time.sleep(1.5)
            print("you go back to lane, but at this point yasuo is already 20 cs and a kill up on you")
            time.sleep(2)
            print("yasuo begins to kda farm you")
            time.sleep(2)
            print("yasuo goes 12-0 and begins to fountain dive you")
            time.sleep(1.75)
            print("mid-lane was winning up to that point, at which point mid begins to int")
            gameover(player3)
            #ends the game if you decide to trade
        elif junglehelp == "call for jungle" or junglehelp == "jungle" or junglehelp == "ping your jungler" or junglehelp == "ping":
            print(f"your jungler, {player4.champion}, ganks your lane, but yasuo ends up getting a double kill after dying with his ignite")
            time.sleep(2)
            print("you go back to lane, but at this point yasuo is already 20 cs and a kill up on you")
            time.sleep(2)
            print("yasuo begins to kda farm you")
            time.sleep(2)
            print("yasuo goes 12-0 and begins to fountain dive you")
            time.sleep(2)
            print("mid-lane was winning up to that point, at which point mid begins to int")
            time.sleep(2)
            gameover(player3)
            #ends the game if you decide to ask for jungle help
    elif lanedecision1 == "cs" or lanedecision1 == "just cs":
        print("good call, better than fighting him")
        time.sleep(2)
        print("yasuo shoves you under tower and you begin missing cs")
        time.sleep(2)
        print("yasuo also begins poking you under tower")
        time.sleep(2)
        print("you never let him get kills in lane, but he gets ahead in cs and levels")
        lanedecision2 = input("yasuo begins to group with his team. Do you want to split push or group with your team?  ").lower()

        if lanedecision2 == "stay in lane" or lanedecision2 == "split push" or lanedecision2 == "split":
            print("good call! you let your team know not to engage since it's a 4v5")
            time.sleep(2.5)
            print("the tier 2 turret is at 40% hp, but enemies are missing.")
            time.sleep(2.75)
            lanedecision3 = input("do you want to finish off the turret or leave in case enemies come?")
            #lets the player choose if they want to stay and finish the turret

            if lanedecision3 == "stay" or lanedecision3 == "finish" or lanedecision3 == "finish the turret":
                print("oh no, you see the enemies coming")
                breakloop = True
                time.sleep(2)
                print("press the 'enter' key as fast as you can to continue breaking the turret!!")
                timeout = 4
                t = Timer(timeout, print, ['Sorry, you were too slow! You died before you got the turret'])
                t.start()
                print("You have %d seconds to break the turret...\n" % timeout)
                prompt = "click!"
                enterlist = []
                while len(enterlist) < 20:
                    entercommand = input(prompt)
                    enterlist.append(entercommand)
                t.cancel()
                print("you broke the turret in time! good job!")

                #the before is an actual real game mechanic where you have to click fast enough to break the turret
                time.sleep(1.5)
                print("you still died, but you killed the turret. Good job!")
                time.sleep(2)
                print("uh oh, your team is still flaming you")
                time.sleep(2)
                print("you tell them you got the turret and they only lost 1 for it, but they are still fuming")
                time.sleep(2.5)
                print("your midlaner gets tilted, and buys 5 'Tears of Morelicon' and 1 pair of 'Boots of Mobility'")
                time.sleep(2)
                gameover(player3)
                #if you stay and get the turret, your team tilts because you die and end up losing

            elif lanedecision3 == "leave" or lanedecision3 == "leave in case" or lanedecision3 == "leave in case enemies come":
                print("you tried to get away, but you still got caught")
                time.sleep(1.5)
                print("your team starts to flame you for split pushing and not even getting the tower")
                time.sleep(2)
                print(f"you try to fight back, but the whole team began talking about the teamfight that {player4.champion} threw")
                print("you try to calm everyone down, but its no hope")
                gameover(player4)
                #team feeds if you do not get the turret and you die instead

            else:
                lanedecision3 = input("sorry, didnt get that. type 'stay' to stay or 'leave' to 'leave")
        elif lanedecision2 == "group" or lanedecision3 == "group with team":
            print("you go to your team and start looking for an engage")
            time.sleep(2)
            print("your team decides to ignore the possibility rakan-yasuo knock-up combo")
            time.sleep(1.5)
            print("your team gets 5-man knocked up")
            time.sleep(2)
            print("the enemy team gets an ace")
            time.sleep(1.5)
            print("the enemy team destroys an inhib, the nexus turrets, and the nexus")
            time.sleep(1.5)
            print("gg")
            time.sleep(4)
            sys.exit()
            #you lose if you try and stay with the team
        else:
            lanedecision2 = input("sorry, i didnt get that. type 'group' to group or 'split' to split push")
    else:
        lanedecsion1 = input("sorry, didnt get that. type 'trade' to trade or 'cs' to farm creeps")

#bada bing
