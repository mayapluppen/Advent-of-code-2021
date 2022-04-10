import math as calculate
from unicodedata import decimal
import math as math

def currentDepth(diveDataFile):
    with diveDataFile as f:
        array = []
        totalcurrentSeaFloorDepthDecreased = 0
        totalcurrentSeaFloorDepthIncreased = 0
        totalHorizontalPositionIncreased = 0
        currentDepth = 0
        currentHorizontalPosition = 0
        previousSeaFloorDepth = 0
        for line in f: # read rest of currentSeaFloorDepths

            currentCourse = line.split()[0]
            units = line.split()[1]
            
            if currentCourse == "up":
                totalcurrentSeaFloorDepthDecreased = totalcurrentSeaFloorDepthDecreased + 1
                currentDepth = currentDepth - int(units)
            elif currentCourse == "down":
                totalcurrentSeaFloorDepthIncreased = totalcurrentSeaFloorDepthIncreased + 1 
                currentDepth = currentDepth + int(units)
            elif currentCourse == "forward":
                totalHorizontalPositionIncreased = totalHorizontalPositionIncreased + 1 
                currentHorizontalPosition = currentHorizontalPosition + int(units)
        
            previousSeaFloorDepth = int(currentDepth)
          
    print("-----------DAY 2 PART 1: Submarine Position -----------")
    print(" ")
    print("Total down? Answer: " + str(totalcurrentSeaFloorDepthIncreased))
    print("Total up? Answer: " + str(totalcurrentSeaFloorDepthDecreased))
    print("Current depth? Answer: " +  str(currentDepth))
    print("Current horizontal position? Answer: " +  str(currentHorizontalPosition))
    resultmsg = "The result is DEPTH x HORIZAONTAL POSITION = " + str(currentDepth*currentHorizontalPosition) 
    print(resultmsg)
    print(" ")
    diveDataFile.close() 