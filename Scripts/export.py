import boto3
import json
import csv

# Connect to AWS
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('student_performance')
s3 = boto3.client('s3')

# -------- STEP 1: Read data from DynamoDB --------
response = table.scan()
data = response['Items']

print("Records fetched:", len(data))


# -------- STEP 2: Export to JSON --------
with open('student_data.json', 'w') as f:
    json.dump(data, f, indent=4, default=str)

print("JSON file created")


# -------- STEP 3: Export to CSV --------
keys = data[0].keys()

with open('student_data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    writer.writerows(data)

print("CSV file created")


# -------- STEP 4: Upload files to S3 --------
bucket_name = 'student-performance-datasets'

s3.upload_file('student_data.json', bucket_name, 'exports/student_data.json')
s3.upload_file('student_data.csv', bucket_name, 'exports/student_data.csv')

print("Files uploaded to S3 successfully")
