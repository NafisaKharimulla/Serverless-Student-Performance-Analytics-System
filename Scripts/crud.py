import boto3
from decimal import Decimal

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('student_performance')


# ---------------- CREATE ----------------
def create_student():
    table.put_item(
        Item={
            'student_id': '101',
            'weekly_self_study_hours': Decimal('10'),
            'attendance_percentage': Decimal('80'),
            'class_participation': 'Medium',
            'total_score': Decimal('75'),
            'grade': 'B'
        }
    )
    print("Student created")


# ---------------- READ ----------------
def read_student():
    response = table.get_item(
        Key={'student_id': '101'}
    )

    if 'Item' in response:
        print(" Student data:", response['Item'])
    else:
        print(" Student not found")


# ---------------- UPDATE ----------------
def update_student():
    table.update_item(
        Key={'student_id': '101'},
        UpdateExpression="SET total_score = :t, grade = :g",
        ExpressionAttributeValues={
            ':t': Decimal('85'),
            ':g': 'A'
        }
    )
    print(" Student updated")


# ---------------- DELETE ----------------
def delete_student():
    table.delete_item(
        Key={'student_id': '101'}
    )
    print("Student deleted")


# ---------------- RUN ALL ----------------
create_student()
read_student()
update_student()
read_student()
delete_student()
read_student()
