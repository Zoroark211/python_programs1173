import boto3

iam = boto3.client('iam')
response = iam.list_users()

for user in response['Users']:
    print('Username:', user['UserName'])
    print('ARN:', user['Arn'])
    print('Created:', user['CreateDate'].strftime('%Y-%m-%d %H:%M:%S'))
    print()
