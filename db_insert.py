#taken from class example -- added line 8 for the client      
import pymongo 

stats  = {"net": {"lo": {"rx ": 0,"tx": 0},"wlan0": {" rx ": 708,"tx": 1192},"eth0": {"rx ": 0,"tx": 0}},"cpu  ": 0.2771314211797171}

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mydb.utilization.insert(stats)