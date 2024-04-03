if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import requests
from src.configs.configs import get_config


@custom
def transform_custom(*args, **kwargs):
    headers = {
        'Content-Type': 'application/json',
    }

    json_data = {
        'pipeline_run': {
            'variables': {
                'keyword': 'back end',
                'geo_id': 102890719,
            },
        },
    }

    url = get_config('pipelines', 'linkedin.url')
    uri = get_config('pipelines', 'linkedin.uri')
    response = requests.post(
        f'{url}{uri}',
        headers=headers,
        json=json_data,
    )

    return {
        'execution_date': response.json()['pipeline_run']['created_at']
    }