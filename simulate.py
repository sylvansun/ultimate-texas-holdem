__author__ = 'monica_wang'
from ultimatepoker import Game
import sys

try:
    simulateTimes = int(sys.argv[1])
except IndexError or ValueError:
    print ("Error: Input simulations times. Usage: python simulate.py [times]")
    exit(1)


totalGain = 0
totalBet = 0

for i in range(simulateTimes):
    game = Game(False)
    gain, bet = game.playGame()
    totalGain += gain
    totalBet += bet


print("=============Simulation Result================")
print(f"Total Gain after ", simulateTimes," times Play: ", totalGain)
print(f"Total Bet after ", simulateTimes," times Play: ", totalBet)
print(f"Total Gain Ratio after ", simulateTimes," times Play: ", totalGain/totalBet)


