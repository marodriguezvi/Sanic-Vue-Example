import requests
import pymongo
from pymongo import MongoClient
import exceptions as exc

cliente = MongoClient()
db = cliente['api-tickets']
collection = db['tickets']

def get_one(_id):
  document = collection.find_one({'_id': int(_id)})
  if not document:
    raise exc.ItemNotStored('The item doesn\'t exist')

  return document

def get_all(order_type):
  # Orders ascending or descending according to the id
  order = pymongo.ASCENDING
  if order_type:
    order = pymongo.ASCENDING if (order_type == 'asc') else pymongo.DESCENDING 
  documents = collection.find().sort('_id', order)
  if not documents:
    raise exc.ItemsNotStored('There aren\'t items')

  return documents