import boto3
client = boto3.client('s3')

response = client.create_bucket(
    ACL='private',
    Bucket='javahomecloud123',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

#upload file to s3
file_reader = open('create_bucket.py').read()
response = client.put_object(
    ACL='private',
    Body=file_reader,
    Bucket='javahomecloud123',
    Key='create_bucket.py'
)

#Delete Object
response = client.delete_object(
    Bucket='javahomecloud123',
    Key='create_bucket.py'
)


#list Objects
response = client.list_objects(
    Bucket='javahomecloud123'
)

for content in response['Contents']:
    print(content['Key'])

#list Buckets
response = client.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])
