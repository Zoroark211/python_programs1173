import boto3

s3 = boto3.client('s3', aws_access_key_id='AKIAUTJSUAI6JR4ZP4IA', aws_secret_access_key='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')

bucket = 'zoroarctestbucket'
file = 'CTdata.json'
local_path = r"C:\Users\Zoroa\Downloads\CTdata.txt"

try:
    response = s3.download_file(bucket, file, local_path)
    print('Yay!!!')
except Exception as e:
    print(':(')