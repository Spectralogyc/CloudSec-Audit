import boto3

def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        try:
            s3.head_bucket(Bucket=bucket['Name'])
            print(f"[+] Bucket seguro: {bucket['Name']}")
        except:
            print(f"[!] Bucket possivelmente público: {bucket['Name']}")

if __name__ == "__main__":
    list_s3_buckets()
