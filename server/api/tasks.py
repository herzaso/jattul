from flask_restful import Resource, reqparse, fields, marshal
from utils import login_required, get_resource

key = 'task'

data = [
    {'id': 1, 'name':'General', 'description':'', 'projects':[1]},
    {'id': 2, 'name':'Sick Leave', 'description':'', 'projects':[]},
]

fields = {
    'name': fields.String,
    'description': fields.String,
    'projects': fields.List(fields.Integer),
    'uri': fields.Url(key, absolute=True)
}


class TaskListAPI(Resource):
    decorators = [login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True,
                                   help='No {} name provided'.format(key))
        self.reqparse.add_argument('description', type=str, default="")
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


class TaskAPI(Resource):
    decorators = [login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str)
        self.reqparse.add_argument('description', type=str)
        self.reqparse.add_argument('projects', type=bool)
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
