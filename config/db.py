import pymongo


mongoURI = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongoURI)

db = client["RECIPE_APP"]
collection = db["recipes"]

def add(data):
    data = dict(data)
    if collection.find_one({"name": data["name"]}):
        return None
    response = collection.insert_one(data)
    return str(response.inserted_id)

def all():
    response = collection.find({}, {"_id": 0})  # id will not be shown in
    data = []
    for i in response:
        # i["_id"] = str(i["_id"])
        data.append(i)
    return data


def get_one(id):
    response = collection.find_one({"_id": id}) 
    response["_id"] = str(response["_id"])
    return response  

def update(data):
    data = data.dict()
    response = collection.update_one({"_id": (data["id"])},{"$set": {"name": data["name"], "ingredients": data["ingredients"]}})
    return response.modified_count


def delete(id):
    response = collection.delete_one({"_id": id})
    return response.deleted_count

