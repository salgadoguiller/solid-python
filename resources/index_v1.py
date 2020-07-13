import requests
import json

from flask import jsonify
from flask_restful import Resource

from webargs.flaskparser import use_args

from schemas.user import UserSchema


class IndexResource(Resource):
    @use_args(UserSchema())
    def post(self, user):
        try:
            profile_id = user.get('profile_id')
            print(f'profile_id: {profile_id}')

            req = requests.get(
                f'https://us-central1-liu-profile-api-dev.cloudfunctions.net/user-details?profile_id={profile_id}')
            status_code = req.status_code

            if status_code != 200:
                print(f'Error getting user details. Status Code: {status_code}')
                return ('Error', 404)

            user_details = req.json()
            keys = user_details.keys()

            for key in keys:
                indexer_url = None
                if key == 'PXA5IVtq9QRwWQKduJKTQSdI70EvhFj8w5ql3UgI':
                    indexer_url = 'https://liu-search-api-dev.appspot.com/connections'
                if key == 'dtQrvgVlFP2VWV5IpTGZP5w179Wf9lad95vh9JHI':
                    indexer_url = 'https://app-search-aqory3l6ba-uc.a.run.app/api/v1/connections'
                if indexer_url is None:
                    continue

                payload = user_details.get(key)

                req = requests.post(
                    indexer_url,
                    headers={
                        'accept': 'application/json',
                        'content-type': 'application/json'
                    },
                    data=json.dumps(payload)
                )
                status_code = req.status_code

                if status_code not in [200, 201]:
                    raise ValueError(f'Error indexing user. Status Code: {status_code}')
                else:
                    print(f'User successfully indexed. Status Code: {status_code}')

            return ('Success', 200)
        except Exception:
            return ('Error', 500)