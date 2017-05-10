from flask import abort
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify({'message': 'Unauthorized access'}), 403)

def get_resource(l, id):
    res = [x for x in l if x['id'] == id]
    try: return res[0]
    except: abort(404)
