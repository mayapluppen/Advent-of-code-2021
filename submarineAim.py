import math as calculate
from unicodedata import decimal
import math as math

def currentPosition(diveDataFile):
    with diveDataFile as f:
        array = []
        currentAim = 0 # Measured in units of X
        currentHorizontalPosition = 0
        currentDepth = 0
        previousAim = 0
        previousDepth = 0
        for line in f: # Read rest of position data

            currentCourse = line.split()[0]
            X = line.split()[1] #A
            
            if currentCourse == "up":
                currentAim = currentAim - int(X)
                currentDepth = previousDepth

            elif currentCourse == "down":
                currentAim = currentAim + int(X)
                currentDepth = previousDepth
            elif currentCourse == "forward":
                currentHorizontalPosition = currentHorizontalPosition + int(X)
                currentDepth = previousDepth + currentAim*int(X)
        
            previousDepth = int(currentDepth)
            previousAim = int(currentAim)

    print("-----------DAY 2 PART 2: Submarine Aim -----------")
    print(" ")
    print("Aim? Answer: " + str(currentAim))
    print("Depth? Answer: " + str(currentDepth))
    print("Horizontal position? Answer: " +  str(currentHorizontalPosition))
    resultmsg = "The result is DEPTH x HORIZAONTAL POSITION = " + str(currentDepth*currentHorizontalPosition) 
    print(" ")
    print(resultmsg)
    diveDataFile.close() 
