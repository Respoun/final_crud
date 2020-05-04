# coding: utf-8
from pymongo import MongoClient
from datetime import datetime

uri = 'mongodb://user:jesuisunelicorne1@ds155164.mlab.com:55164/ubeer'
client = MongoClient(uri, retryWrites=False)
#27017

#Set db/collections
mydb = client["ubeer"]
customer = mydb["Customers"]
bills = mydb["Bills"]
country = mydb["Countries"]
style = mydb["Styles"]
product = mydb["Products"]
brewery = mydb["Brewery"]
date = datetime.now()

dataCustomer = {
  "id": 1,
  "first_name": "toto",
  "last_name": "tata",
  "email": "toto@mail.com",
  "creation_date": "11/02/2020"
}

dataBills = {
  "id": 1,
  "client_id": 1,
  "started_date": "11/02/2020",
  "ended_date": "12/02/2020",
  "payed": True,
  "sum": 111,
  "product_id": 1
}

dataCountry = {
  "id": 1,
  "name": "France"
}

dataStyle = {
  "id": 1,
  "name": "pale ale"
}

dataproduct = {
  "id": 1,
  "name": "biere",
  "price": 1.2,
  "stock": 20,
  "informations": {
    "id_brewery": 1,
    "id_style": 1,
    "id_country": 1
  },
  "id_pics": 3,
  "id_bills": 1
}

dataBrewery = {
  "id": 1,
  "name": "Brasserie de Paris",
  "id_country": 1
}


#Insert data
try:
    a = customer.insert_one(dataCustomer)
    b = bills.insert_one(dataBills)
    c = country.insert_one(dataCountry)
    d = style.insert_one(dataStyle)
    e = product.insert_one(dataproduct)
    f = brewery.insert_one(dataBrewery)
except Exception as e:
    print("mongo: " + str(e))
    pass