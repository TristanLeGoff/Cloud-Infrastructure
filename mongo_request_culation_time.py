import pymongo
import time
from datetime import datetime

# print(datetime(2018))
myclient = pymongo.MongoClient(host="mongodb010", port=30000)
mydb = myclient["testDB"]

time_list = []
#R1
mycol = mydb["couses"]
myaggregate = [{"$project": { 
    "title": 1,
    "_id": 0,
    "clearRate" : { 
        "$cond":[
            {"$eq": [ {"$size":"$playedBy"}, 0 ]}, 
            0, 
            {"$divide": [ {"$size":"$clearedBy"}, {"$size":"$playedBy"} 
        ]}]
    }
}}]

#R2
# mycol = mydb["couses"]
# myaggregate = [
#     {"$match":{"difficulty":"superExpert"}},
#     {"$project": {"_id":0, "title":1, "totalLike": { "$size":"$likedBy" }}},
#     {"$sort": {"totalLike":-1}},
#     {"$limit":1}
# ]

#R3
# mycol = mydb["players"]
# myaggregate = [
#     {"$project": { 
#         "name": 1, 
#         "totalClear": { "$size":"$clears" }, 
#         "totalPlay": { "$size":"$plays" }, 
#     }},
#     {"$match":{"totalPlay":{"$gt":1000}}},
#     {"$sort": {"totalClear":1}}
# ]

#R4
# mycol = mydb["players"]
# myaggregate = [
#     {"$project": {"numberMaker": { "$size":"$maker" },"_id":0, "name":1}},
#     {"$sort": {"numberMaker":-1}},
# ]

#R5
# mycol = mydb["couses"]
# myaggregate = [
#     {"$project": {"_id":0, "totalRecord": { "$size":"$recordedBy" },"list player record":"$recordedBy"}},
#     {"$sort": {"totalRecord":-1}},
#     {"$limit":1}
# ]

#R6
# mycol = mydb["couses"]
# myaggregate = [
#     { "$project": { "difficulty":1, "lastMeta": {"$first": { "$slice": [ "$courseMeta.clearRate", -1] } } } },
#     { "$group": { "_id": "$difficulty", "average_clear_rate": { "$avg": "$lastMeta"}}},
#     { "$sort": { "average_clear_rate": -1} }
# ]

#R7
# mycol = mydb["players"]
# myaggregate = [
#     {"$project": { 
#         "name": 1, 
#         "totalClear": { "$size":"$clears" }, 
#         "totalPlay": { "$size":"$plays" }, 
#     }},
#     {"$match":{"totalPlay":{"$gt":1000}}},
#     {"$sort": {"totalClear":1}}
# ]

#R8
# mycol = mydb["couses"]
# start_dt = datetime(2017,1,1)
# end_dt = datetime(2018,1,1)
# myaggregate = [
#     {"$match":{"creation":{"$regex" : "2017"}}},
#     {"$project": {"title":1, "totalLike": { "$size":"$likedBy" }, "tweet": {"$first": { "$slice": [ "$courseMeta.tweets", -1] } }}},
#     {"$sort": {"totalLike":-1}},
#     {"$limit":1},
# ]

for i in range(10):
    # Start timer
    start_time = time.time()
    # Send request
    # mydoc = mycol.find(myquery)
    mydoc = mycol.aggregate(myaggregate)
    # End timer
    end_time = time.time()
    # Time execution
    time_execution = end_time - start_time
    time_list.append(time_execution)

time_list.remove(max(time_list))
time_list.remove(min(time_list))
print("Mean time execution:", sum(time_list)/len(time_list),"seconds")
list_doc = list(mydoc)
print("Number of docs retrieved:",len(list_doc))
print("First result:\n",list_doc[0])
