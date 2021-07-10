import boto3

import sys

bucket = "sec-test-training-jp"


def write_string(s):
    s3 = boto3.client("s3")

    # Print out bucket names
    print("\nCurrent buckets:")
    for v in s3.list_buckets().get("Buckets"):
        print(f"{v}")

    print("\nwriting to bucket")
    resp = s3.put_object(Body=s, Bucket=bucket, Key="testing.txt")
    print(resp)


if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

    write_string(sys.argv[1])
