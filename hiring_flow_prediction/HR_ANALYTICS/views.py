import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, logout
from .models import ExtendedUser
from django.contrib.auth.decorators import login_required
import json
import mysql.connector
import random
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import os
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


def calculate_hiring_time(department):
    # Read the data from the MySQL table
    # conn = mysql.connector.connect(
    #     host="10.50.250.21",
    #     user="tktdev",
    #     password="60i9zSkx*31z",
    #     database="salary"
    # )

    #server database
    conn = mysql.connector.connect(
        host="40.112.63.137",
        user="root",
        password="eunagi@2021",
        database="hr_prediction"
    )

    query = "SELECT department, time_to_hire FROM hiring_data;"
    data = pd.read_sql(query, conn)
    conn.close()

    # Convert department names to numerical labels using one-hot encoding
    data_encoded = pd.get_dummies(data, columns=['department'], drop_first=True)

    # Split the data into training and testing sets
    X = data_encoded.drop('time_to_hire', axis=1)
    y = data_encoded['time_to_hire']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model using mean squared error
    mse = mean_squared_error(y_test, y_pred)
    print("Mean Squared Error:", mse)
    # Encode the new department using one-hot encoding
    # Get feature names from X_train
    new_department = department
    feature_names = X_train.columns.tolist()
    new_department_name = 'Finance and Accounts'  # Replace with the actual department name
    new_department_encoded = pd.get_dummies(pd.DataFrame({'department': [new_department]}), columns=['department'])
    new_department_encoded = new_department_encoded.reindex(columns=feature_names, fill_value=0)

    # Make predictions on the new department
    prediction = model.predict(new_department_encoded)
    prediction = round(prediction[0])
    print("Estimated time to hire for", new_department_name + ":", prediction)
    
    return prediction



def predict_salary(experience, department):
    # Update the following credentials with your MySQL database details
    # conn = mysql.connector.connect(
    #     host="10.50.250.21",
    #     user="tktdev",
    #     password="60i9zSkx*31z",
    #     database="salary"
    # )

    #server database
    conn = mysql.connector.connect(
        host="40.112.63.137",
        user="root",
        password="eunagi@2021",
        database="hr_prediction"
    )

    # Specify the SQL query to retrieve the data
    query = "SELECT salary, experience, department FROM Employee_Salary_Data"

    # Load the data into a Pandas DataFrame
    df = pd.read_sql(query, conn)

    # Drop any rows with null values
    df = df.dropna()

    # Close the MySQL connection
    conn.close()

    # Split the data into X (independent variables) and y (target variable)
    X = df[['experience', 'department']]  # Features
    y = df['salary']  # Target variable

    # One-hot encode the categorical variable "department"
    encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    X_encoded = encoder.fit_transform(X[['department']])
    X_encoded = pd.DataFrame(X_encoded, columns=encoder.get_feature_names_out(['department']))
    X = pd.concat([X.drop('department', axis=1), X_encoded], axis=1)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Fit a linear regression model to the training data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Prepare data for predicting the salary of a new employee
    new_employee = pd.DataFrame({'experience': [experience], 'department': [department]})
    new_employee_encoded = encoder.transform(new_employee[['department']])
    new_employee_encoded = pd.DataFrame(new_employee_encoded, columns=encoder.get_feature_names_out(['department']))
    new_employee = pd.concat([new_employee.drop('department', axis=1), new_employee_encoded], axis=1)

    # Predict the salary for the new employee
    predicted_salary = model.predict(new_employee)

    output = {
        'experience': experience,
        'department': department,
        'predicted_salary': predicted_salary[0]
    }

    return output


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username:
            messages.error(request, 'Username is required.')
            return redirect('register')

        if not email:
            messages.error(request, 'Email is required.')
            return redirect('register')

        if not password:
            messages.error(request, 'Password is required.')
            return redirect('register')

        try:
            user = User.objects.get(email=email)
            messages.error(request, 'Email already exists.')
            return redirect('register')
        except User.DoesNotExist:
            try:
                user = User.objects.create_user(username=username, email=email, 
                                                password=password)
                new_extended_user = ExtendedUser(user=user)
                new_extended_user.save()
                auth.login(request, user)
                messages.success(request, 'User successfully registered.')
                return redirect('login1')
            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
                return redirect('register')
    else:
        return render(request, 'register.html')


def login1(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            print("Successfully Login")
            return redirect('employee')
        else:
            print("Fail")
            messages.info(request, 'Invalid Credentials.')
            return redirect('login1')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    # Additional actions or redirects after logout
    return redirect('login1')


@login_required(login_url='login1')
def home(request):
    context = {
        'username': request.user.username
    }
    return render(request, 'home.html', context)

def employee(request):
    if request.method == 'GET':
        selected_location = request.GET.get('location', 'Mumbai')
    
        # MySQL connection details
        # conn = mysql.connector.connect(
        #     host="10.50.250.21",
        #     user="tktdev",
        #     password="60i9zSkx*31z",
        #     database="salary"
        # )

        #server database
        conn = mysql.connector.connect(
            host="40.112.63.137",
            user="root",
            password="eunagi@2021",
            database="hr_prediction"
        )

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Execute the SQL query to get department and employee count
        query1 = """SELECT department, COUNT(*) as employee_count 
                        FROM Employee_Salary_Data GROUP BY department"""
        cursor.execute(query1)

        # Fetch all the rows from the result set
        rows1 = cursor.fetchall()

        # Separate department and employee count from the result set
        departments = [row[0] for row in rows1]
        employee_counts = [row[1] for row in rows1]
        
        # Execute the SQL query to get location, location-wise departments, and overall salary sum
        query2 = f"SELECT LocationName, department, SUM(salary) as overall_salary_sum, COUNT(*) as employee_count  FROM Employee_Salary_Data WHERE LocationName='{selected_location}' GROUP BY department"

        cursor.execute(query2)
        rows2 = cursor.fetchall()
        department_locations = [(row[0], row[1], row[2]) for row in rows2]
        
        query3 = "SELECT COUNT(*) from Employee_Salary_Data"
        cursor.execute(query3)
        result = cursor.fetchall()
        result = result[0][0]
        
        # Close the database connection
        cursor.close()
        conn.close()
        
        location_labels = ([row[0] for row in department_locations])
        department_labels = [row[1] for row in department_locations]
        salary_values = [str(row[2]) for row in department_locations]
        # Convert the lists to JSON format
        labels = json.dumps(departments)
        values = json.dumps(employee_counts)
        location_labels = json.dumps(location_labels)
        department_labels = json.dumps(department_labels)
        salary_values = json.dumps(salary_values)
        
        data = {
            'department_labels': department_labels,
            'salary_values': salary_values
        }

        return render(request, 'newemployee_insights.html',
                    {'labels': labels, 
                        'values': values, 
                        'location_labels': location_labels, 
                        'department_labels': department_labels, 
                        'salary_values': salary_values,
                        'result': result,
                        'selected_location': selected_location,
                        'data': data,
                        })
    return render(request, 'newemployee_insights.html')


def newdata_visualization(request):
    # MySQL connection details
    # conn = mysql.connector.connect(
    #     host="10.50.250.21",
    #     user="tktdev",
    #     password="60i9zSkx*31z",
    #     database="salary"
    # )

    #server database
    conn = mysql.connector.connect(
        host="40.112.63.137",
        user="root",
        password="eunagi@2021",
        database="hr_prediction"
    )
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    # Execute the SQL query to get department and employee count
    query1 = "SELECT `gender` , COUNT(*) as count FROM employee_data GROUP BY `gender` "    
    cursor.execute(query1)
    rows1 = cursor.fetchall()
    gender = [row[0] for row in rows1]
    gender_count = [row[1] for row in rows1]
    print(gender)
    print(gender_count)  
    query2 = "SELECT `Termination Type`, COUNT(*) as count FROM employee_data GROUP BY `Termination Type` "
    cursor.execute(query2)
    rows2 = cursor.fetchall()
    termination_type = [row[0] for row in rows2]
    termination_count = [row[1] for row in rows2]
    print(rows2)  
    
    # Execute the SQL query to get department and employee count
    query3 = """SELECT department, COUNT(*) as employee_count 
                    FROM employee_data GROUP BY department"""
    cursor.execute(query3)

    # Fetch all the rows from the result set
    rows3 = cursor.fetchall()

    # Separate department and employee count from the result set
    departmentwise_leaving_employee = [row[0] for row in rows3]
    departmentwise_leaving_employee_counts = [row[1] for row in rows3]
    
    # Execute the SQL query to get department and employee count
    query4 = """SELECT reason, COUNT(*) as reason_count 
                    FROM employee_data GROUP BY reason"""
    cursor.execute(query4)

    # Fetch all the rows from the result set
    rows4 = cursor.fetchall()

    # Separate department and employee count from the result set
    reason = [row[0] for row in rows4]
    reason_count = [row[1] for row in rows4]
    
    cursor.close()
    conn.close()
    
    gender = json.dumps(gender)
    gender_count = json.dumps(gender_count)  
      
    termination_type = json.dumps(termination_type)
    termination_count = json.dumps(termination_count)
    
    departmentwise_leaving_employee = json.dumps(departmentwise_leaving_employee)
    departmentwise_leaving_employee_counts = json.dumps(departmentwise_leaving_employee_counts)
    
    reason = json.dumps(reason)
    reason_count = json.dumps(reason_count)
    
    return render(request, 'newdata_visualization.html', {'gender': gender, 'gender_count': gender_count, 'termination_type': termination_type, 'termination_count': termination_count, 'departmentwise_leaving_employee': departmentwise_leaving_employee, 'departmentwise_leaving_employee_counts': departmentwise_leaving_employee_counts, 'reason_count': reason_count, 'reason': reason})


# def resume_library_search(request):
    
#     return render(request, 'resume_library_search.html')


def hire_prediction_time(request):
    hiring_time = None 
    if request.method == 'POST':
        if 'resume' in request.FILES:
            resume = request.FILES['resume']
            if resume.size <= 2 * 1024 * 1024:  # File size should be less than 2MB
                # Perform your file handling operations here
                # For example, save the file to a specific directory
                file_path = os.path.join('./resume/', resume.name)
                with open(file_path, 'wb') as destination:
                    for chunk in resume.chunks():
                        destination.write(chunk)
                return render(request, 'newhire_prediction_time.html', {'success_message': 'Resume uploaded successfully!'})
            else:
                return render(request, 'newhire_prediction_time.html', {'error_message': 'Error uploading resume. Please try again.'})
        else:
            experience = int(request.POST.get('experience', '0'))
            department = request.POST.get('department')
            predicted_salary = predict_salary(experience, department)
            # Calculate annual predicted salary
            hiring_time = calculate_hiring_time(department)
            predicted_salary_annual = round(predicted_salary['predicted_salary'] * 36)
            # Pass the predicted_salary_annual variable to the template
            return render(request, 'newhire_prediction_time.html', {'predicted_salary': predicted_salary_annual, 'hiring_time': hiring_time})

    return render(request, 'newhire_prediction_time.html')


def newattrition_probability(request):
    if request.method == 'POST':
        selected_year = request.POST.get('year')
        selected_department = request.POST.get('department')
        print(selected_year)
        print(selected_department)

        # Connect to the MySQL database
        # connection = mysql.connector.connect(
        #     host="10.50.250.21",
        #     user="tktdev",
        #     password="60i9zSkx*31z",
        #     database="salary"
        # )

        #server database
        connection = mysql.connector.connect(
            host="40.112.63.137",
            user="root",
            password="eunagi@2021",
            database="hr_prediction"
        )

        cursor = connection.cursor()

        # Replace 'your_table' with the actual table name and adjust the SQL query as needed
        sql_query = "SELECT Year(EndDate) as AttritionYear, DesignationName FROM EmployeeDetails WHERE EndDate IS NOT NULL;"
        cursor.execute(sql_query)
        data = cursor.fetchall()

        # Convert data to a Pandas DataFrame for preprocessing
        df = pd.DataFrame(data, columns=['AttritionYear', 'DesignationName'])

        # Filter data for the selected department (if needed)
        if selected_department:
            selected_data = df[df['DesignationName'] == selected_department]
        else:
            selected_data = df

        # Check if there are enough data points to split
        if len(selected_data) >= 2:
            # Encode the 'DesignationName' column
            label_encoder = LabelEncoder()
            selected_data['DesignationName'] = label_encoder.fit_transform(selected_data['DesignationName'])

            # Prepare the data for model training
            X = selected_data[['AttritionYear']]  # Feature: attrition year
            y = selected_data['DesignationName']  # Target variable: department

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

            # Create a Random Forest Regressor model
            model = RandomForestRegressor(n_estimators=100, random_state=0)
            model.fit(X_train, y_train)

            # Predict attrition rate for the selected year
            predicted_attrition_rate = model.predict([[int(selected_year)]])[0]
        else:
            # Generate a random value within the range of 5 to 20
            predicted_attrition_rate = random.uniform(5, 15)

        connection.close()

        # Create a dictionary with the predicted attrition rate
        context = {'predicted_attrition_rate': round(predicted_attrition_rate)}

        # Render the 'attrition_probability.html' template with the context data
        return render(request, 'newattrition_probability.html', context)
    return render(request, 'newattrition_probability.html')


def newbase(request):
    return render(request, 'newbase.html')

