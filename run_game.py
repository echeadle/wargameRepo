""" Run Attack of the Orcs Game"""

import sys
from wargame.attackoftheorcs import AttackOfTheOrcs


sys.path.append("/wargame")

game = AttackOfTheOrcs()
game.play()
