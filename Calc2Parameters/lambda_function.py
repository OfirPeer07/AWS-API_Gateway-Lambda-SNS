'''
# 1. Replace the current code with the code below.
# 2. Create a new file (adder.py).
# 3. Copy the ARN after you have created a Topic in the SNS Service.
# 4. Paste your ARN to "TopicArn=".
# 5. Save and Deploy your changes.
'''

import json
import boto3
from adder import add

print('Loading function')

def lambda_handler(event, context,):
    num1 = event['num1']
    num2 = event['num2']
    op = event['op']
    if op == "add":
        result = (f"The sum of {num1} and {num2} = {add(num1,num2)}")
    
    sns = boto3.client('sns')
    response = sns.publish(
        TopicArn='Add_Your_TopicArn',
        Message=result)

    return response
