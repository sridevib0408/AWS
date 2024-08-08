import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')
table.put_item(
    Item={
        'emp_id': '2',
        'name': 'kammana',
        'salary': 20000
    }
)


#Get items from table
resp = table.get_item(
    Key={
        'emp_id': '2'
    }
)

print(resp['Item'])

table.delete_item(
    Key={
        'emp_id': '2'
    }
)

#batch insert items
with table.batch_writer() as batch:
    for x in range(100):
        batch.put_item(
            Item={
                'emp_id': str(x),
                'name': 'Name-{}'.format(x)
            }
        )
