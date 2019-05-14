import time
import requests
import pymongo
from pymongo import MongoClient

cliente = MongoClient()
db = cliente['api-tickets']
collection = db['tickets']

url  = 'https://domain.freshdesk.com/api/v2/tickets'
password = 'password'
email = 'email'

def get_elements(params):
  # Order the query by the update date
  params['order_by'] ='updated_at'
  params['include'] = 'description'
  response = requests.get(url, auth=(email, password), params=params)
  if response:
    response = response.json()
  return response

def update_key(values):
  for value in values:
    value['_id'] = value.pop('id')


if __name__ == "__main__":
  last_update = ''
  
  if collection.count_documents({}) == 0:
    tickets = get_elements({})
    update_key(tickets)
    collection.insert_many(tickets)
  else:
    last_update = collection.find().limit(1).sort('updated_at', pymongo.DESCENDING)[0]
    last_update = last_update['updated_at']

  while True:
    # Consult from the last saved update date in the database
    params = {'updated_since': last_update}
    tickets = get_elements(params)
    
    if tickets:
      for ticket in tickets:
        ticket['_id'] = ticket.pop('id')
        collection.replace_one({'_id': ticket['_id']}, ticket, True)
    
      last_update = tickets[0]['updated_at']    
    time.sleep(3)