import boto3
s3 = boto3.resource('s3')

#bucket_name = str(input('What bucket will you go to: '))
#opened_bucket = s3.Bucket(bucket_name)

#for my_bucket_object in opened_bucket.objects.all():
#    print(my_bucket_object.key)

#s3.meta.client.upload_file(r'C:\Users\Zoroa\OneDrive\Documents\Python for Anything\FilestackPython\myPic.JPG', 'zoroarctestbucket', 'myPic0.JPG')

#path_file = str(input('Select File: '))
#object_name = str(input('What will be the objects name in the bucket: '))

#s3.meta.client.upload_file(path_file, bucket_name, object_name)

s3.meta.client.delete_object(Bucket='zoroarctestbucket', Key='CSdata.json')