import io
import pandas as pd
import requests
import time
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from orchestrator.crawlers.LinkedinUrlGenerator import LinkedinUrlGenerator
from orchestrator.crawlers.LinkedinCrawler import scrape_data_from_url
from orchestrator.utils.hash import create_hash_id


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url_generator = LinkedinUrlGenerator() \
        .set_geo_id(102890719) \
        .set_keywords('Software Engineer')

    offset = 0
    dfs = []
    while True:
        offset += 1
        if offset % 10 == 0:
            time.sleep(5)
        print(f'get page {offset}.')
        df = scrape_data_from_url(url_generator.set_offset(offset).get())
        length = len(df)
        print(f'got {length} results.')
        if len(df) == 0:
            break
        dfs.append(df)
    
    result = pd.concat(dfs)
    result['hash_id'] = result.apply(lambda x: create_hash_id(x), axis=1)
    return result


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'