import mysql.connector
import random
from faker import Faker
from datetime import datetime, timedelta


fake = Faker()

# MySQL connection details
conn = mysql.connector.connect(
    host="10.50.250.21",
    user="tktdev",
    password="60i9zSkx*31z",
    database="salary"
)
# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the table
create_table_query = """
CREATE TABLE IF NOT EXISTS attrition_data (
    EmployeeCode VARCHAR(10),
    FirstName VARCHAR(50),
    Gender VARCHAR(10),
    DepartmentName VARCHAR(50),
    DesignationName VARCHAR(50),
    EmploymentStatus VARCHAR(20),
    IsDelete INT,
    LocationName VARCHAR(50),
    SubDepartmentName VARCHAR(50),
    JoiningDate DATE,
    EndDate DATE
);
"""
cursor.execute(create_table_query)

job_titles = [
    'Software Engineer',
    'Data Analyst',
    'Marketing Manager',
    'Sales Representative',
    'Product Manager',
    'UX/UI Designer',
    'Financial Analyst',
    'Human Resources Manager',
    'Operations Coordinator',
    'Customer Support Specialist'
]
# Generate and insert data into the table
for _ in range(1550):
    employee_code = str(random.randint(1000, 9999))
    first_name = fake.first_name()
    gender = random.choice(["Male", "Female"])
    department_name = random.choice(["Admin", "Microsoft", "Business Support", "Digital Marketing", "Finance and Accounts", "Human Resource", "Mobile Application Development", "Open Source", "Quality", "Sales", "Systems"])
    designation_name = random.choice(job_titles)
    employment_status = random.choice(["Confirmed", "Probabation"])
    is_delete = random.choice([0, 1])
    location_name = random.choice(["Ahmedabad", "Mumbai"])
    sub_department_name = fake.job()[:50] 
    joining_date = fake.date_between_dates(date_start=datetime(2010, 1, 1), date_end=datetime(2023, 12, 31))
    end_date = fake.date_between_dates(date_start=joining_date + timedelta(days=1), date_end=datetime(2023, 12, 31))

    insert_statement = "INSERT INTO attrition_data (EmployeeCode, FirstName, Gender, DepartmentName, DesignationName, EmploymentStatus, IsDelete, LocationName, SubDepartmentName, JoiningDate, EndDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    values = (employee_code, first_name, gender, department_name, designation_name, employment_status, is_delete, location_name, sub_department_name, joining_date, end_date)

    cursor.execute(insert_statement, values)

conn.commit()
conn.close()
