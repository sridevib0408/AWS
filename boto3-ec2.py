import boto3
client = boto3.client("ec2")
resp = client.run_instances(ImageId = 'ami-467fiewhef', InstanceType = 't2.micro', MinCount = 1, MaxCount = 1)
for instance in resp['Instances']:
    print(instance['InstanceId'])


# start ec2 instances
client.start_instances(InstanceIds= ['somexyz'])

#stop ec2 instances
client.stop_instances(InstanceIds= ['somexyz'])

#terminate ec2 instance
resp = client.terminate_instances(InstanceIds = ['somexyz'] )

for instance in resp['TerminatingInstances']:
    print("The instance which got terminated is {}".format(instance['InstanceId']))


#for describing instance
resp = client.describe_instances()
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print("The instance Id of the instance is {}". format(instance['InstanceId']))

#for describing instance with filter
resp = client.describe_instances(Filters = [{
    'Name' : 'instance-state-name',
    'Values' : ['running']
}])
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print("The instance Id of the instance is {}". format(instance['InstanceId']))

resp = client.describe_instances(Filters = [{
    'Name' : 'tag:Env',
    'Values' : ['Prod']
}])
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print("The instance Id of the instance is {}". format(instance['InstanceId']))

#create EBS snapshots of all instance with tag name backup and send EMAIL notification
ec2 = boto3.resource('ec2')
sns_client = boto3.client('sns')
filter_cond =   [
    {'Name':'tag :backup',
     'Values' : 'Yes'}
]

snapshot_ids = []
for instance in ec2.instances.filter(Filters = filter_cond):
    for vol in instance.volumes.all():
        snapshot = vol.create_snapshot("Created by boto3")
        snapshot_ids.append(snapshot.snapshot_id)

sns_client.publish(
    TopicArn =  'fefverfvre',
    Subject = 'EBS Snapshot',
    Message = str(snapshot_ids)

)
