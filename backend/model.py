
import requests
import exceptions as exc

url  = 'https://domain.freshdesk.com/api/v2/tickets'
password = 'password'
email = 'email'

def get_one(id):
  global url, email, password
  response = requests.get((url+'/'+id), auth=(email, password))
  if not response:
    raise exc.ItemNotStored('The item doesn\'t exist')
  else:
    response = response.json()
  return response

def get_all(order_type):
  global url, email, password
  # Orders ascending or descending according to the expiration date of the ticket
  params = {'order_by': 'due_by', 'order_type': 'desc'}
  if order_type:
    params['order_type'] = order_type
  response = requests.get(url, auth=(email, password), params=params)
  if not response:
    raise exc.ItemsNotStored('There aren\'t items')
  else:
    response = response.json()
  return response