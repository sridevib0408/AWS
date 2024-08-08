import boto3
client = boto3.client('s3')

response = client.create_bucket(
    ACL='private',
    Bucket='MyBucketSrideviB',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

#upload file to s3
file_reader = open('create_bucket.py').read()
response = client.put_object(
    ACL='private',
    Body=file_reader,
    Bucket='MyBucketSrideviB',
    Key='create_bucket.py'
)

#Delete Object
response = client.delete_object(
    Bucket='MyBucketSrideviB',
    Key='create_bucket.py'
)


#list Objects
response = client.list_objects(
    Bucket='MyBucketSrideviB'
)

for content in response['Contents']:
    print(content['Key'])

#list Buckets
response = client.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])

#get specific rows and colums from s3 bucket
resp = client.select_object_content(
    Bucket = 'MyBucketSrideviB',
    Key = 'file/Myfile.csv',
    Expression = 'select s.name,s.email from s3Object as s,
    ExpressionType ='SQL',
    InputSerialization = {CSV:{'FileHeaderInfo':'Use'}}
    OutputSerialization = {CSV:{}}
)
#list the data from csv file
for event in resp['payload']:
    if 'Records' in event:
        print(event['Records']['payload'].decode())
    print(


