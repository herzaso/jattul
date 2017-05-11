from flask_restful import Resource, reqparse, fields, marshal
from utils import login_required, get_resource

key = 'tracking'

data = [
]

fields = {
    'user_id': fields.Integer,
    'project_id': fields.Integer,
    'task_id': fields.Integer,
    'date': fields.DateTime(dt_format='rfc822'),
    'start_time': fields.Integer,
    'end_time': fields.Integer,
    'note': fields.String,
    'uri': fields.Url(key, absolute=True)
}


class TrackingListAPI(Resource):
    decorators = [login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('user_id', type=int, required=True,
                                   help='No {} user_id provided'.format(key),
                                   location='json')
        self.reqparse.add_argument('project_id', type=int, required=True,
                                   help='No {} project_id provided'.format(key),
                                   location='json')
        self.reqparse.add_argument('task_id', type=int, required=True,
                                   help='No {} task_id provided'.format(key),
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


class TrackingAPI(Resource):
    decorators = [login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('user_id', type=int)
        self.reqparse.add_argument('project_id', type=int)
        self.reqparse.add_argument('task_id', type=int)
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
