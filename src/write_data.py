import awswrangler as wr
from pathlib import Path

PATH_TO_FILE:Path = Path('data', 'sample.csv')


def write_data_to_albums_table():
    '''writes data to Albums table in DynamoDB'''
    table_name:str = 'Albums'
    wr.dynamodb.put_csv(
    PATH_TO_FILE,
    table_name=table_name
    )


if __name__ == '__main__':
    write_data_to_albums_table()
