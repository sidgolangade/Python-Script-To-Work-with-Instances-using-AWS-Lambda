import boto3
import datetime

def stop_instances_on_weekends(event, context):
    # Create a Boto3 EC2 client
    ec2 = boto3.client('ec2')

    # Get the current day of the week
    current_day = datetime.datetime.now().weekday()

    # Check if it's a weekend (Saturday or Sunday)
    if current_day == 5 or current_day == 6:
        # Get all the running instances
        response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

        # Extract the instance IDs
        instance_ids = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_ids.append(instance['InstanceId'])

        # Stop the instances
        if instance_ids:
            ec2.stop_instances(InstanceIds=instance_ids)
            print(f"Stopped instances: {', '.join(instance_ids)}")
        else:
            print("No running instances found on weekends.")
    else:
        print("Not a weekend. No action required.")

    # Return a response
    return {
        'statusCode': 200,
        'body': 'Script executed successfully.'
    }
