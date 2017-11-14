from os import path

from google.cloud.bigquery.client import Client

_json_file_path = path.dirname(__file__)
_json_file_path = path.join(_json_file_path, '..', '..', 'pointz-secret.json')
_json_file_path = path.abspath(_json_file_path)

client = Client.from_service_account_json(_json_file_path)

dataset_pointz = client.dataset('pointz')
