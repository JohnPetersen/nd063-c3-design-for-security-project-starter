import boto3

# From https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

# Let's use Amazon S3
s3 = boto3.resource("s3")

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
