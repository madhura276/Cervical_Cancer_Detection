import csv

def authenticate_user(email, password):
    csv_file = "reg.csv"
    """
    Authenticate user by checking if the provided email and password
    match any record in the CSV file.

    Args:
        email (str): The email to search for.
        password (str): The password to search for.
        csv_file (str): Path to the CSV file.

    Returns:
        bool: True if email and password match, False otherwise.
    """
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['email'] == email and row['password'] == password:
                    return True
        return False
    except FileNotFoundError:
        print(f"Error: The file {csv_file} does not exist.")
        return False
    except KeyError:
        print(f"Error: The file {csv_file} must have 'email' and 'password' columns.")
        return False
import csv
import os

def add_user(email, password, county, name, csv_file):
    """
    Adds a new user to the CSV file if the email is not already present.

    Args:
        email (str): The email of the user.
        password (str): The password of the user.
        county (str): The county of the user.
        name (str): The name of the user.
        csv_file (str): Path to the CSV file.

    Returns:
        str: A message indicating if the user was added or already exists.
    """
    user_found = False

    # Ensure the file exists before processing
    if os.path.exists(csv_file):
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['email'] == email:
                    user_found = True
                    break

    if user_found:
        return "User already exists in the CSV file."

    # Append the new user to the CSV file
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode='a', newline='') as file:
        fieldnames = ['email', 'password', 'county', 'name']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header if the file is new
        if not file_exists or os.stat(csv_file).st_size == 0:
            writer.writeheader()

        writer.writerow({'email': email, 'password': password, 'county': county, 'name': name})
    
    return "User added successfully."

# # Example usage:
# csv_path = "reg.csv"
# email_input = "new.user@example.com"
# password_input = "mypassword"
# county_input = "Germany"
# name_input = "New User"

# message = add_user(email_input, password_input, county_input, name_input, csv_path)
# print(message)
import csv
import csv

def get_user_activity(email):
    # List to store all activities of the user
    activities = []
    
    # Open and read the activity.csv file
    with open('activity.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['email'] == email:
                # Append activity row to the list
                activities.append({
                    'login': row['login'],
                    'last_click': row['last_click'],
                    'logout': row['logout']
                })
    
    # Return the list of activities for the given email
    return activities if activities else None

    return None  # Return None if the email is not found
import csv
import csv

def get_user_history(email):
    user_data = []
    # Open and read the history.csv file
    with open('history.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['email'] == email:
                user_data.append(row)
    return user_data

import csv
from datetime import datetime

def insert_data_to_csv(email, name, age, num_partners, first_intercourse, num_pregnancies,
                       smokes, packs_per_year, hormonal_contraceptives, contraceptives_years,
                       stds, stds_hpv, stds_diagnosis, dx_cin, dx_hpv, schiller,biopsy):
    # Current timestamp for the time field
    time = datetime.now().strftime('%Y-%m-%d')
    
    # Open the CSV file and append the data
    with open('history.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Insert the parameters as a row
        writer.writerow([email, name, time, age, num_partners, first_intercourse, num_pregnancies,
                         smokes, packs_per_year, hormonal_contraceptives, contraceptives_years, stds,
                         stds_hpv, stds_diagnosis, dx_cin, dx_hpv, schiller,biopsy])
    
    print(f"Data for {name} has been added to the CSV file.")
import csv
from datetime import datetime

# Function to insert email and login time (only adds login)
def insert_login_time(email):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Add the new login time to the CSV (no checking of email, simply appending)
    with open('activity.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([email, current_time, "", ""])
    
    print(f"Login time for {email} has been added at {current_time}.")

# Function to update the last click time for the given email (updates last row only)
def update_last_click_time(email):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    updated = False
    
    # Read the existing data
    with open('activity.csv', mode='r', newline='') as file:
        rows = list(csv.reader(file))
    
    # Check if the last row's email matches and update the last click time
    if rows and rows[-1][0] == email:
        rows[-1][2] = current_time  # Update last_click field
        updated = True
    
    # Write the updated rows back to the CSV
    if updated:
        with open('activity.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Last click time for {email} has been updated to {current_time}.")
    else:
        print(f"Email {email} not found in the last row to update last click time.")

# Function to update the logout time for the given email (updates last row only)
def update_logout_time(email):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    updated = False
    
    # Read the existing data
    with open('activity.csv', mode='r', newline='') as file:
        rows = list(csv.reader(file))
    
    # Check if the last row's email matches and update the logout time
    if rows and rows[-1][0] == email:
        rows[-1][3] = current_time  # Update logout field
        updated = True
    
    # Write the updated rows back to the CSV
    if updated:
        with open('activity.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Logout time for {email} has been updated to {current_time}.")
    else:
        print(f"Email {email} not found in the last row to update logout time.")


def getmail():
    file_path="user.csv"
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            em = next(reader)  
            return em[0]  
    except FileNotFoundError:
        return {"error": "File not found"}
    except Exception as e:
        return {"error": str(e)}

def set_mail(mail):
    file_path="user.csv"
    try:
        
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([mail])  

        print(f"CSV file has been cleared and updated with email: {mail}")
    
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print(f"Error: {str(e)}")
        