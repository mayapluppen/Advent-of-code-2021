import tkinter as gui
from unicodedata import decimal
import math
import sonarSweep as sonarSweep
import submarinePosition as submarinePosition

msg= "Time to Dive!"                                         
print(msg.center(100))

print(msg)

window = gui.Tk()

#Day 1: Sonar Sweep, Part 1
dataFile = open('sonarData.txt')
sonarSweep.currentSeaFloorDepth(dataFile,'Vertical')

#Day 2: Submarine position
dataFile = open('diveData.txt')
submarinePosition.currentDepth(dataFile)

