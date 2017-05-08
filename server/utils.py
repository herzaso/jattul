from flask import make_response, jsonify, abort, g
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.verify_password
def verify_password(username, password):
    if username == 'admin' and password == 'admin':
        return True
    return False

# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify({'message': 'Unauthorized access'}), 403)

def get_resource(l, id):
    res = [x for x in l if x['id'] == id]
    try: return res[0]
    except: abort(404)
