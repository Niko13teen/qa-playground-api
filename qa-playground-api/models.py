from flask_restful import Resource, reqparse


parser = reqparse.RequestParser()
parser.add_argument("email", type=str)
parser.add_argument("first_name", type=str)
parser.add_argument("last_name", type=str)

users = {
        7: {"id":7, "email":"alice@yahoo.com", "first_name":"Alice", "last_name":"Broflowsky"},
        8: {"id":8, "email":"kail@gmail.com", "first_name":"Kail", "last_name":"Latinos"},
        9: {"id":9, "email":"levi@mail.ru", "first_name":"Levi", "last_name":"Fake"},
        10: {"id":10, "email":"bob@gmail.com", "first_name":"Bob", "last_name":"Omagados"},
        11: {"id":11, "email":"mock@yandex.ru", "first_name":"Mock", "last_name":"Object"},
        12: {"id":12, "email":"secret@secret.com", "first_name":"#", "last_name":"#"}
        }

class Users(Resource):
    def get(self, user_id):
        try:
            if user_id == 0:
                return users
            else:
                return users[user_id]
        except:
            return 'Congratulations, you have found a crutch, nothing works without it!'

    def post(self, user_id):
        users[user_id] = parser.parse_args()
        return users, 201

    def put(self, user_id):
        users[user_id] = parser.parse_args()
        return users, 201

    def delete(self, user_id):
        del users[user_id]
        return users, 204
