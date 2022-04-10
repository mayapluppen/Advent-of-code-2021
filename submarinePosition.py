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
            print(currentCourse)
            print(units)
            
            if currentCourse == "up":
                print(currentCourse + '-> Up = Decreased by ' + units + ' units.')
                totalcurrentSeaFloorDepthDecreased = totalcurrentSeaFloorDepthDecreased + 1
                currentDepth = currentDepth - int(units)
            elif currentCourse == "down":
                print(currentCourse + '-> Down = Increased by ' + units + ' units.')
                totalcurrentSeaFloorDepthIncreased = totalcurrentSeaFloorDepthIncreased + 1 
                currentDepth = currentDepth + int(units)
            elif currentCourse == "forward":
                print(currentCourse + '-> Forward = Increased by ' + units + ' units.')
                totalHorizontalPositionIncreased = totalHorizontalPositionIncreased + 1 
                currentHorizontalPosition = currentHorizontalPosition + int(units)
        
            previousSeaFloorDepth = int(currentDepth)
          
    
    msg = "Total down? Answer: " + str(totalcurrentSeaFloorDepthIncreased)
    print(msg)
    msg = "Total up? Answer: " + str(totalcurrentSeaFloorDepthDecreased)
    print(msg)
    msg = "Current depth? Answer: " +  str(currentDepth)
    print(msg) 
    msg = "Current horizontal position? Answer: " +  str(currentHorizontalPosition)
    print(msg) 
    resultmsg = "The result is DEPTH x HORIZAONTAL POSITION = " + str(currentDepth*currentHorizontalPosition) 
    print(resultmsg)
    diveDataFile.close() 