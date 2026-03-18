import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('student_performance')

def performance_calculation(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 60:
        return "Average"
    else:
        return "Poor"

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    try:
        # Get S3 bucket and file name
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        # Read file from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')

        # Convert JSON to Python
        data = json.loads(content)

        for student in data:
            # Calculate performance
            score = student.get('total_score', 0)
            student['performance_category'] = performance_calculation(score)

            # Insert into DynamoDB
            table.put_item(Item=student)

        return {
            "statusCode": 200,
            "body": "Data processed successfully"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "error": str(e)
        }