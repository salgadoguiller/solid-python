import requests
import json

from utils.user_data.user_data_final import UserData

class Document():

    def __init__(self, data: UserData):
        self.data = data.get()

    def index(self) -> bool:
        keys = self.data.keys()

        for key in keys:
            indexer_url = None
            if key == 'PXA5IVtq9QRwWQKduJKTQSdI70EvhFj8w5ql3UgI':
                indexer_url = '<search-url>'
            if key == 'dtQrvgVlFP2VWV5IpTGZP5w179Wf9lad95vh9JHI':
                indexer_url = '<search-url>'
            if indexer_url is None:
                continue

            payload = self.data.get(key)

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

        return True
