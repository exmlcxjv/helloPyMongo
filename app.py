import pymongo
from pymongo import MongoClient

#cloud Mongo
#cluster = MongoClient("mongodb+srv://exmlcxjv:fucklehkim@clustertest-ue3wk.mongodb.net/test?retryWrites=true&w=majority")
#db = cluster["first-test"]
#collection = db["users"]

#local Mongo
cluster = MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")
db = cluster["testDB"]
collection = db["testCollection"]

insertone = {"name": "Max"}
insertmany = [{"name": "John"},{"name": "Aaron", "age": 20}]
#msg = collection.insert_one(insertone)
#msg = collection.insert_many(insertmany)

results = collection.find()

for result in results:
    print(result)
