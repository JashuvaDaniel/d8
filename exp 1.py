employees = {
"E001": {"name": "Alice", "age": 30, "salary": 55000},
"E002": {"name": "Bob", "age": 45, "salary": 75000},
"E003": {"name": "Charlie", "age": 28, "salary": 48000},
"E004": {"name": "David", "age": 35, "salary": 62000},
"E005": {"name": "Eva", "age": 40, "salary": 69000}
}
for emp_id, details in employees.items():
     print(f"Employee ID: {emp_id}")
     print(f" Name: {details['name']}")
print(f" Age: {details['age']}")
print(f" Salary: ${details['salary']}") 
print("-" * 30)