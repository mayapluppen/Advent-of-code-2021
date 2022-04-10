import math as calculate
from unicodedata import decimal
import math as math



def currentSeaFloorDepth(sonarDataFile, course):
    with sonarDataFile as f:
        array = []
        totalcurrentSeaFloorDepthDecreased = 0
        totalcurrentSeaFloorDepthIncreased = 0
        previousSeaFloorDepth = 0
        for currentSeaFloorDepth in f: # read rest of currentSeaFloorDepths
            
            if int(currentSeaFloorDepth) < previousSeaFloorDepth and previousSeaFloorDepth != 0:
                totalcurrentSeaFloorDepthDecreased = totalcurrentSeaFloorDepthDecreased + 1
            else:
                totalcurrentSeaFloorDepthIncreased = totalcurrentSeaFloorDepthIncreased + 1 
                
            previousSeaFloorDepth = int(currentSeaFloorDepth)
            array.append([int(x) for x in currentSeaFloorDepth.split()])
    
    sonarDataFile.close() 
    print(" ")
    print("-----------DAY 1 PART 1: Sonar Sweep -----------")
    print(" ")
    msg = "How many measurements are larger than the previous measurement? Answer: " + str(totalcurrentSeaFloorDepthIncreased-1)
    print(msg)
    print(" ")
    sonarDataFile.close()

   
