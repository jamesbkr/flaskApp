from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'number1'
api = Api(app)


jwt = JWT(app, authenticate, identity) # create /auth endpoint

items = []

class Item(Resource):
    @jwt_required() # forces authorization
    # Get specific item
    def get(self, name):
        item = next(filter(lambda x : x['name'] == name , items), None) #Lambda function to iterate over the list looking at name and returns first item that matches the name
        return {'item' : item}, 200 if item else 404 # 200 if item is returned.  If the item doesnt exist return 404

    # Create Specific item
    def post(self,name):
        if next(filter(lambda x : x['name'] == name , items), None) is not None:
            return { 'message' : 'there is already an item with that name'}, 400

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    # Delete specific Item
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name']!= name, items)) # items is list of items without the ones that are named the ones we are removing
        return {'items' : items}, 200

    # update or create specific item
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=float, required=True,help="need to have a price")
        data = parser.parse_args()
        item = next(filter(lambda x : x['name'] == name , items), None)
        if item is None:
            item = {'name':name,'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return{'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
if __name__=="__main__":

    app.run(port=5000, debug=True)
