import tkinter as gui
from unicodedata import decimal
import math
import sonarSweep as sonarSweep
import submarinePosition as submarinePosition
import submarineAim as submarineAim

window = gui.Tk()

#Day 1: Sonar Sweep, Part 1
dataFile = open('sonarData.txt')
sonarSweep.currentSeaFloorDepth(dataFile,'Vertical')

#Day 2 part 1: Submarine position
dataFile = open('diveData.txt')
submarinePosition.currentDepth(dataFile)

#Day 2 part 2: Submarine position using the aim-algorithm
dataFile = open('diveData.txt')
submarineAim.currentPosition(dataFile)