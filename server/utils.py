from flask import abort, make_response, jsonify, session
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session or not session['user']:
            return make_response(jsonify({'error': 'Unauthorized access'}), 403)
        return f(*args, **kwargs)
    return decorated_function

def get_resource(l, id):
    res = [x for x in l if x['id'] == id]
    try: return res[0]
    except: abort(404)
