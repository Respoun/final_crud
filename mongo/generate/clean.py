from pymongo import MongoClient

uri = 'mongodb://user:jesuisunelicorne1@ds155164.mlab.com:55164/ubeer'
client = MongoClient(uri, retryWrites=False)

mydb = client["ubeer"]
client.drop_database(mydb)