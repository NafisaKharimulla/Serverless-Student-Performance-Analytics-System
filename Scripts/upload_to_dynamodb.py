import boto3
import json
from decimal import Decimal

# AWS setup
dynamodb = boto3.resource('dynamodb')
TABLE_NAME = 'student_performance'
table = dynamodb.Table(TABLE_NAME)

# Function to convert floats to Decimal and add performance_category
def process_record(record):
    record['student_id'] = str(record['student_id'])
    for key in ['weekly_self_study_hours', 'attendance_percentage', 'class_participation', 'total_score']:
        record[key] = Decimal(str(record[key]))

    score = record['total_score']
    if score >= 90:
        record['performance_category'] = 'Excellent'
    elif 75 <= score < 90:
        record['performance_category'] = 'Good'
    elif 60 <= score < 75:
        record['performance_category'] = 'Average'
    else:
        record['performance_category'] = 'Poor'

    return record

def upload_to_dynamodb(json_file):
    # Load JSON
    print("Loading JSON file...")
    with open(json_file, 'r') as f:
        data = json.load(f)
    print(f"Loaded {len(data)} records.")

    # Batch upload
    print("Uploading records to DynamoDB...")
    with table.batch_writer(overwrite_by_pkeys=['student_id']) as batch:
        for idx, item in enumerate(data, start=1):
            clean_item = process_record(item)
            batch.put_item(Item=clean_item)
            # Print progress every 5 records
            if idx % 5 == 0 or idx == len(data):
                print(f"  Progress: {idx}/{len(data)} records uploaded.")

    print("✅ All records uploaded successfully!")

if __name__ == '__main__':
    upload_to_dynamodb('students.json')
