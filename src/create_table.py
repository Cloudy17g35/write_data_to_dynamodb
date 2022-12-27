import boto3


def create_albums_table(dyn_resources=None):
    '''creates DynanmoDB table in AWS'''
    
    if dyn_resources is None:
        dyn_resources = boto3.resource('dynamodb')

    table_name = "Albums"

    schema = {
    "AttributeDefinitions": [
        {
            "AttributeName": "album_name",
            "AttributeType": "S",
        },
        {
            "AttributeName": "album_id",
            "AttributeType": "N"
        },
    ],
    "KeySchema": [
        {"AttributeName": "album_name", "KeyType": "HASH"},
        {"AttributeName": "album_id", "KeyType": "RANGE"},
    ],
    "BillingMode": "PAY_PER_REQUEST",
    "TableName": table_name
    }

    table = dyn_resources.create_table(**schema)
    print(f'Creating table {table_name}')
    table.wait_until_exists()
    print('Table created')
    return table


if __name__ == '__main__':
    create_albums_table()

