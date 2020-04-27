
from pymongo import MongoClient
# from pprint import pprint

cString = 'mongodb://db:27017/?readPreference=primary&ssl=false'
client = MongoClient(cString)


def getServerStatus():
    db=client.admin
    # Issue the serverStatus command and print the results
    serverStatusResult=db.command("serverStatus")
    return serverStatusResult 
