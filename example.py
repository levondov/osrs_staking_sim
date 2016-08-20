###
### Example file to run functions
###
from duel import *

# choose the atk style for each player
P1P2styles = ('atk','atk')

# how many runs do you want to do
runs = 100000

# display extra duel info
extra_info = False

# which players are using a hasta
hasta = (True,False)

print duel(P1P2styles,hasta,runs,extra_info)
