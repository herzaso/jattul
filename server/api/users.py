from flask_restful import Resource, reqparse, fields, marshal
from utils import login_required, get_resource

key = 'user'

data = [
    {'id':1, 'first_name':'Ofir', 'last_name':'Herzas', 'username':'ofirh@tikalk.com', 'password':'1234', 'role_id':0, 'projects':[1]},
    {'id':2, 'first_name':'Test', 'last_name':'', 'username':'admin', 'password':'admin', 'role_id':0, 'projects':[0]},
]

fields = {
    'first_name': fields.String,
    'last_name': fields.String,
    'username': fields.String,
    'password': fields.String,
    'role_id': fields.Integer,
    'projects': fields.List(fields.Integer),
    'uri': fields.Url(key, absolute=True)
}


class UserListAPI(Resource):
    decorators = [login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('first_name', type=str, required=True,
                                   help='No {} first_name provided'.format(key))
        self.reqparse.add_argument('role_id', type=int, default=1)
        super().__init__()

    def get(self):
        return {key+'s': [marshal(r, fields) for r in data]}

    def post(self):
        args = self.reqparse.parse_args()
        r = {'id': data[-1]['id'] + 1}
        for k in fields:
            if k != 'uri' and k in args:
                r[k] = args[k]
        data.append(r)
        return {key: marshal(r, fields)}, 201


class UserAPI(Resource):
    decorators = [login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('first_name', type=str)
        self.reqparse.add_argument('last_name', type=str)
        self.reqparse.add_argument('username', type=str)
        self.reqparse.add_argument('password', type=str)
        self.reqparse.add_argument('role_id', type=int)
        self.reqparse.add_argument('projects', type=list)
        super().__init__()

    def get(self, id):
        r = get_resource(data, id)
        return {key: marshal(r, fields)}

    def put(self, id):
        r = get_resource(data, id)
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                r[k] = v
        return {key: marshal(r, fields)}

    def delete(self, id):
        r = get_resource(data, id)
        data.remove(r)
        return {'result': True}


def get_user(username, password):
    try:
        user = [x for x in data if x['username'] == username and x['password'] == password][0]
        return user
    except: return None
