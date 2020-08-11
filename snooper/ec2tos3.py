import boto3


def upload_file_to_s3bucket(filepath, datafilename, newname):
    # resource object
    s3 = boto3.resource('s3')

    # Upload a new file
    data = open(filepath+datafilename, 'rb')
    s3.Bucket('aws-scraper-bucket').put_object(Key='rawdata/'+newname, Body=data)
    data.close()
