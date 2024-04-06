import tkinter as tk
import sqlite3

# Function to validate login credentials
def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Establish a database connection
    conn = sqlite3.connect('user_credentials.db')
    cursor = conn.cursor()
    
    # Check if the entered credentials exist in the database
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    
    # Close the database connection
    conn.close()
    
    if user:
        # Destroy login window and open student info form
        login_window.destroy()
        open_student_info_form()
    else:
        error_label.config(text="Invalid username or password")

# Function to save student information to the database
def save_student_info():
    first_name = first_name_entry.get()
    roll_number = roll_number_entry.get()
    grade = grade_entry.get()
    
    # Establish a connection to the database
    conn = sqlite3.connect('user_credentials.db')
    cursor = conn.cursor()
    
    # Insert student information into the 'students' table
    cursor.execute("INSERT INTO students (first_name, roll_number, grade) VALUES (?, ?, ?)", (first_name, roll_number, grade))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    # Clear the entry fields after saving data
    first_name_entry.delete(0, tk.END)
    roll_number_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    
    print("Student information saved successfully!")

# Function to open student information form
def open_student_info_form():
    # Create a new window for student information form
    student_info_window = tk.Tk()
    student_info_window.title("Student Information Form")
    
    # Labels and entry fields for student information
    first_name_label = tk.Label(student_info_window, text="First Name:")
    first_name_label.pack()
    first_name_entry.pack()
    
    roll_number_label = tk.Label(student_info_window, text="Roll Number:")
    roll_number_label.pack()
    roll_number_entry.pack()
    
    grade_label = tk.Label(student_info_window, text="Grade:")
    grade_label.pack()
    grade_entry.pack()
    
    # Button to save student information
    save_button = tk.Button(student_info_window, text="Save", command=save_student_info)
    save_button.pack()
    
    # Start the main loop for student info form window
    student_info_window.mainloop()

# Create the main window for login
login_window = tk.Tk()
login_window.title("Login")

# Labels and entry fields for username and password
username_label = tk.Label(login_window, text="Username:")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

# Button to login
login_button = tk.Button(login_window, text="Login", command=validate_login)
login_button.pack()

# Error label for login validation messages
error_label = tk.Label(login_window, text="", fg="red")
error_label.pack()

# Entry fields for first name, roll number, and grade
first_name_label = tk.Label(login_window, text="First Name:")
first_name_label.pack()
first_name_entry = tk.Entry(login_window)
first_name_entry.pack()

roll_number_label = tk.Label(login_window, text="Roll Number:")
roll_number_label.pack()
roll_number_entry = tk.Entry(login_window)
roll_number_entry.pack()

grade_label = tk.Label(login_window, text="Grade:")
grade_label.pack()
grade_entry = tk.Entry(login_window)
grade_entry.pack()

# Start the main loop for login window
login_window.mainloop()
