from pymongo import MongoClient
import base64


client = MongoClient('mongodb://user:jesuisunelicorne1@ds155164.mlab.com:55164/ubeer?retryWrites=false')
db = client.ubeer
collection = db.Images

def insertImg():
    try:
        with open("../../asset/img/img3.jpg", "rb") as imageFile:
            string = base64.b64encode(imageFile.read())
            data = collection.insert_one({
            'id' : 3,
            'image' : string
            })
            print("image store in db")
    except Exception as e:
        print('Mongo: ' + str(e))

def getImg():
    qry = {'id' : 1}
    proj = {'image' : 1, '_id' : 0}

    try:
        string = collection.update_one(qry, proj)
        image = string['image']
        with open("test2.jpg", "wb") as fimage:
            fimage.write(image.decode('base64'))
    except Exception as e:
        print('Mongo: ' + str(e))

insertImg()
