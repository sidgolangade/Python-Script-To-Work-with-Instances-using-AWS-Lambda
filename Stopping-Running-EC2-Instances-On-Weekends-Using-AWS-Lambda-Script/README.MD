## AWS Lambda Function to Stop EC2 Instances on Weekends
This repository contains a Python script that utilizes an AWS Lambda function to automatically stop running EC2 instances on weekends. By scheduling the Lambda function to trigger on Saturdays and Sundays, you can ensure cost savings by stopping non-essential instances when they are not needed.

## Prerequisites
- Python 3.x 

## Configuration
To configure and deploy the AWS Lambda function:

- In the AWS Management Console, create a new Lambda function.
- Choose the Python 3.x runtime for the function.
- Configure the function to use an execution role with the necessary permissions to describe and stop EC2 instances. 
- Set the trigger for the function to be a scheduled event using CloudWatch Events. Configure it to trigger on Saturdays and Sundays.
- Save and deploy the Lambda function.

## Usage
The Lambda function will automatically execute on the configured schedule, stopping any running EC2 instances on weekends. You can check the CloudWatch Logs for the Lambda function to view the execution logs and verify the instances that were stopped.

### Refer to the Screenshots folder for more information.