
from sanic import Sanic, response
from sanic_cors import CORS, cross_origin
import model
import exceptions as exc

# Create instance of sanic
app = Sanic(__name__)
CORS(app)

async def get_user(request):
  _id = request.args.get('id')
  if _id:
    try:
      data = model.get_one(_id)
    except exc.ItemNotStored as e:
      return response.json({'error': e.args[0]}, status = 404)
    else:
      message = {
        'subject': data.get('subject'),
        'description': data.get('description_text'),
        'priority': data.get('priority')
      }
      return response.json(message, status = 200)
  
  else:
    return response.json({'error': 'id not found! please send me a id!'}, status = 404)



async def get_users(request):
  order_type = request.args.get('order_type')
  try:
    data = model.get_all(order_type)
  except exc.ItemsNotStored as e:
    return response.json({'error': e.args[0]}, status = 404)
  else:
    message = list()
    
    for item in data:
      message.append({
          'due_by': item.get('due_by'),
          'id': item.get('_id'),
          'status': item.get('status'),
          'priority': item.get('priority'),
          'type': item.get('type'),
          'name': item.get('name'),
          'responder_id': item.get('responder_id')
        })
    return response.json(message, status = 200)

# Endpoints

app.add_route(get_user, '/user', ['GET'])
app.add_route(get_users, '/users', ['GET'])

if __name__ == '__main__':
  # Run the application
  app.run(host='0.0.0.0', port=8000)