# Serverless Student Performance Analytics System

## Project Overview

This project implements a serverless data processing system using AWS services to analyze student academic performance data.

The system automatically processes student datasets uploaded to Amazon S3, extracts the records using AWS Lambda (Python), stores them in Amazon DynamoDB, and supports CRUD operations, queries, analytics, and data export.

This project demonstrates practical implementation of Serverless Architecture using AWS + Python.

---

## Objective

Build a serverless system that:

- Automatically processes uploaded student datasets
- Stores student records in DynamoDB
- Calculates student performance category
- Supports CRUD operations
- Supports analytical queries
- Exports processed data into JSON/CSV format
- Detects students at risk
- Generates top performer leaderboard

---

## Technologies Used

- Amazon S3
- AWS Lambda (Python)
- Amazon DynamoDB
- IAM Roles
- Python (Boto3)
- JSON / CSV
- GitHub

---

## Dataset

Dataset used from Kaggle:
Student Performance Dataset

Dataset fields:

- student_id
- weekly_self_study_hours
- attendance_percentage
- class_participation
- total_score
- grade

Example record:

{
"student_id": "ST001",
"weekly_self_study_hours": 12,
"attendance_percentage": 92,
"class_participation": 8,
"total_score": 88,
"grade": "B"
}

---

## System Architecture

Student Dataset (JSON/CSV)
|
v
Amazon S3 Bucket
|
(S3 Event Trigger)
|
v
AWS Lambda (Python)
|
v
Amazon DynamoDB
|
CRUD + Queries + Export

---

## Project Features

### 1. Automatic Data Processing

Whenever a dataset file is uploaded to S3:

- Lambda is triggered automatically
- The file is read
- Student records are extracted
- Data is inserted into DynamoDB

---

### 2. Performance Category Calculation

Lambda automatically calculates a new field:

| Total Score | Performance Category |
| ----------- | -------------------- |
| >= 90       | Excellent            |
| 75 – 89     | Good                 |
| 60 – 74     | Average              |
| < 60        | Poor                 |

---

### 3. CRUD Operations

Python scripts are provided to perform:

- Insert a new student
- Read student record using student_id
- Update student performance details
- Delete a student record

---

### 4. Query Operations

The system supports the following analytical queries:

- Students with attendance > 90%
- Students with study hours > 10
- Students in Excellent category
- Top 10 students by total score
- Students at risk

---

### 5. Secondary Index (GSI)

A Global Secondary Index is created to support fast queries.

Index Configuration:

- Partition Key: grade
- Sort Key: total_score

Used to retrieve:

- Top students in Grade A
- Students with highest scores

---

### 6. Data Import

A dataset with more than 200 student records is uploaded to S3.

Lambda automatically:

- Processes the dataset
- Stores all records in DynamoDB

---

### 7. Data Export

The system exports student records into:

- JSON format
- CSV format

The exported files are uploaded back to Amazon S3.

---

### 8. Advanced Features

#### Student Risk Detection

A new field is added:

at_risk = True

If:

- attendance_percentage < 60  
  OR
- total_score < 50

---

#### Top Performers Leaderboard

System generates:
Top 10 students based on total_score.

---

#### Batch Processing

If a dataset contains more than 500 records:

- Batch write operations are used
- Improves performance and efficiency

---

#### Error Handling

The system handles:

- Invalid JSON files
- Missing fields
- Duplicate student records

---

## Project Folder Structure

Serverless-Student-Performance-Analytics-System/
│
├── lambda_function/
│ └── lambda_function.py
│
├── scripts/
│ ├── insert_student.py
│ ├── read_student.py
│ ├── update_student.py
│ ├── delete_student.py
│ ├── query_operations.py
│ └── export_data.py
│
├── dataset/
│ └── student_performance_200_records.json
│
├── exported_data/
│ ├── student_data.json
│ └── student_data.csv
│
├── screenshots/
│ ├── s3_bucket.png
│ ├── lambda_trigger.png
│ ├── dynamodb_table.png
│ ├── gsi_index.png
│ ├── dataset_upload.png
│ └── export_result.png
│
├── architecture/
│ └── architecture_diagram.png
│
└── README.md

---

## How the System Works

Step 1: Faculty uploads dataset to S3  
Step 2: S3 triggers Lambda automatically  
Step 3: Lambda reads the dataset  
Step 4: Performance category is calculated  
Step 5: Data is stored in DynamoDB  
Step 6: CRUD and queries are performed using Python scripts  
Step 7: Data is exported into JSON/CSV and uploaded to S3

---

## Deliverables Included

This repository contains:

- DynamoDB Table Schema
- Lambda Function Code
- Python Scripts for CRUD Operations
- Sample Dataset (200+ records)
- Exported JSON and CSV Files
- Screenshots of AWS Resources
- Architecture Diagram
- README Documentation

---

## Learning Outcomes

This project demonstrates:

- Serverless architecture using AWS
- Real-time data processing
- Working with DynamoDB using Python
- S3 event-based automation
- Batch data processing
- Cloud-based analytics system
