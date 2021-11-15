import boto3
from json import dumps

ec2 = boto3.client('ec2', region_name="us-east-1")

def lambda_handler(event, context):
    instance = ec2.describe_instances()['Reservations'][0]['Instances'][0]['InstanceId'] # Only works if there is a single EC2 Instance

    if event['action'] == 'start':
        try:
            response = ec2.start_instances(
                InstanceIds=[
                    instance
                ]
            )
            response = response['StartingInstances'][0]
            return {'statusCode': 200, 'message': f'Instance {response["InstanceId"]} is starting and is currently {response["CurrentState"]["Name"]}. Was {response["PreviousState"]["Name"]}.'}
        except Exception as e:
            return dumps(e)

        
    elif event['action'] == 'stop':
        try:
            response = ec2.stop_instances(
                InstanceIds=[
                    instance
                ]
            )
            response = response['StoppingInstances'][0]
            return {'statusCode': 200, 'message': f'Instance {response["InstanceId"]} is stopping and is currently {response["CurrentState"]["Name"]}. Was {response["PreviousState"]["Name"]}.'}
        except Exception as e:
            return dumps(e)

    else:
        return {'statusCode': 401, 'message': 'No action provided'}
