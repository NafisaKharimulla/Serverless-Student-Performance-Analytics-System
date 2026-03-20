import boto3
from boto3.dynamodb.conditions import Key

# Connect
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('student_performance')

print("\nTop students in Grade A:\n")

response = table.query(
    IndexName='grade-score-index',
    KeyConditionExpression=Key('grade').eq('A'),
    ScanIndexForward=False   # Highest score first
)

for item in response['Items']:
    print(item)
