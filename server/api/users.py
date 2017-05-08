from flask_restful import Resource, reqparse, fields, marshal
from utils import auth, get_resource

key = 'user'

data = [
    {'id':1, 'first_name':'Ofir', 'last_name':'Herzas', 'email':'ofirh@tikalk.com', 'password':'1234', 'role_id':0, 'projects':[1]}
]

fields = {
    'first_name': fields.String,
    'last_name': fields.String,
    'email': fields.String,
    'password': fields.String,
    'role_id': fields.Integer,
    'projects': fields.List(fields.Integer),
    'uri': fields.Url(key, absolute=True)
}


class UserListAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('first_name', type=str, required=True,
                                   help='No {} first_name provided'.format(key),
                                   location='json')
        self.reqparse.add_argument('role_id', type=int, default=1,
                                   location='json')
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
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('first_name', type=str, location='json')
        self.reqparse.add_argument('last_name', type=str, location='json')
        self.reqparse.add_argument('email', type=str, location='json')
        self.reqparse.add_argument('password', type=str, location='json')
        self.reqparse.add_argument('role_id', type=int, location='json')
        self.reqparse.add_argument('projects', type=list, location='json')
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
