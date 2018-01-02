from flask import Flask, jsonify, request
from user import User
from users import Users
import uuid
from uuid import UUID
app = Flask(__name__)

# THIS IS A SERVER
# GET = SEND DATA
# POST = RECIEVE DATA
# GET IS IMPLIED
# Objects in code:
#    user : person
#    facility : physical location
#    item : thing in physical location
#    internal location: location inside the facility











#######################################################
#######################################################
#######################################################
# MODELS
#######################################################
#######################################################
#######################################################

users = Users({})

#######################################################
#######################################################
#######################################################
# ENDPOINTS
#######################################################
#######################################################
#######################################################



#######################################################
# USER
#######################################################
# CREATE user
#POST /user data: {:name:}
@app.route('/user',methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(data['first_name'],data['last_name'])
    users.add_user(new_user)
    print(users)
    return str(new_user.uuid)
# READ user
# DELETE user
#GET /user/<string:name>
@app.route('/user/<string:uuid>', methods=['DELETE','GET'])
def get_user(uuid):
    if not str(uuid) in users.users:
        return 'there are no users by that name'
    else:
        return_user = users.users[str(uuid)]
        return str(return_user.last_name)

# READ all users
#GET ALL users /user
@app.route('/user')
def get_users():
    if not users.users:
       return 'there are no users'
    else:
       return Users.toString(users)


# UPDATE user
#UPDATE /user/<string:name>
@app.route('/user', methods=['UPDATE'])
def update_user_list():
    pass



#######################################################
# USERS
#######################################################
# CREATE users
#POST /users data: {:list_name:}
#@app.route('/users',methods=['POST'])
#def create_user_list():
#    data = request.get_json()
#    pass


# UPDATE all user
#UPDATE /user
#@app.route('/user', methods=['UPDATE'])
#def update_user():
#    pass



app.run(port=5000)
