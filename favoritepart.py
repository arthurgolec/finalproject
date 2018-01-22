import time
from threading import Timer




time.sleep(2)
print("press the 'enter' key as fast as you can to continue breaking the turret!!")
timeout = 7
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