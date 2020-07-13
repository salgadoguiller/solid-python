import requests
import json

from flask_restful import Resource

from webargs.flaskparser import use_args

from schemas.user import UserSchema
from utils.user_data.user_data_final import UserDataFromRequest, UserDataFromFile
from utils.document.document_final import Document

class IndexResource(Resource):

    @use_args(UserSchema())
    def post(self, user):
        try:
            profile_id = user.get('profile_id')
            data_from = user.get('data_from')
            print(f'profile_id: {profile_id}')
            print(f'data_from: {data_from}')

            if data_from == 'file':
                user_data = UserDataFromFile(profile_id)
            else:
                user_data = UserDataFromRequest(profile_id)

            document = Document(user_data)
            document.index()

            return ('Success', 200)

        except Exception as exc:
            print(exc)
            return ('Error', 500)
