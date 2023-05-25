import pymongo
client = pymongo.MongoClient("mongodb+srv://rohanpagdal:RoAaru1619@rohanpagdal0.vevsotq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Rohan",
    "email" : "Rohanpagdal@gmail.com",
    "surname" : "Pagdal"

}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
