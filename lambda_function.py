import boto3

ec2 = boto3.client('ec2', region_name="us-east-1")

def lambda_handler(event, context):
    if event['action'] == 'start':
        try:
            response = ec2.start_instances(
                InstanceIds=[
                    event['instance']
                ]
            )
            response = response['StartingInstances'][0]
            return {'statusCode': 200, 'message': f'Instance {response["InstanceId"]} is starting and is currently {response["CurrentState"]["Name"]}. Was {response["PreviousState"]["Name"]}.'}
        except Exception as e:
            return e.message

        
    elif event['action'] == 'stop':
        try:
            response = ec2.stop_instances(
                InstanceIds=[
                    event['instance']
                ]
            )
            response = response['StoppingInstances'][0]
            return {'statusCode': 200, 'message': f'Instance {response["InstanceId"]} is stopping and is currently {response["CurrentState"]["Name"]}. Was {response["PreviousState"]["Name"]}.'}
        except Exception as e:
            return e

    else:
        return {'statusCode': 401, 'message': 'No action provided'}

a = lambda_handler({"action":"start", "instance":"123"}, 1)
print(a)