import json
import sys
import urllib


printstr = ""
with open('query.txt') as json_file:
    data = json.load(json_file)
    for x in range(len(data["features"])):
        for i in range(len(data["features"][x]["geometry"]["rings"])):
            for j in range(len(data["features"][x]["geometry"]["rings"][i])):
                printstr += "["+ str(data["features"][x]["geometry"]["rings"][i][j][1])+ "," + str(data["features"][x]["geometry"]["rings"][i][j][0])+ "],"

        f = open(data["features"][x]["attributes"]["GIS_FeatureKey"]+ ".txt", "w")
        f.write(printstr[:-1])
        printstr = ""
    
