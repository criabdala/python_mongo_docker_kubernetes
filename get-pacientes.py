import pymongo

#Define Connection
myclient = pymongo.MongoClient("mongodb://criabdala:<PASSWORD>cluster0-shard-00-00-yllbo.mongodb.net:27017,cluster0-shard-00-01-yllbo.mongodb.net:27017,cluster0-shard-00-02-yllbo.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")


mydb = myclient["centro_medico"] #Define DB
mycol = mydb["testCollection"]   #Define Collection (table)

#Insert Data in the collection
"""mydict = { "name": "Cristian", "username": "criabdala" }
x = mycol.insert_one(mydict)
mydict = { "name": "Carolina", "username": "caro" }
x = mycol.insert_one(mydict)
mydict = { "name": "Lucas", "username": "lucas" }
x = mycol.insert_one(mydict)
mydict = { "name": "Antonia", "username": "antonia" }
x = mycol.insert_one(mydict)
mydict = { "name": "Martina", "username": "martina" }
x = mycol.insert_one(mydict)
"""

#Find all registers whose name will be cristian
myquery = { "name": "Carolina" }
mydoc = mycol.find(myquery)
for fields in mydoc:
  print(fields)

#Return all table  
myquery = {}
mydoc = mycol.find(myquery)
for fields in mydoc:
  print(fields)