import pandas as pd

# read csv file
df = pd.read_csv("student_performance.csv")

# convert to json
df.to_json("students.json", orient="records", indent=4)

print("JSON file created successfully")
