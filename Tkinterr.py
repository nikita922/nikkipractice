import tkinter as tk
import sqlite3

# Create a SQLite database and a table for student management
conn = sqlite3.connect('student.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (username TEXT, rollno TEXT, grade TEXT)''')
conn.commit()

# Function to insert a student record into the database
def insert_student():
    student_username = username_entry.get()
    student_rollno = rollno_entry.get()
    student_grade = grade_entry.get()

    if student_username and student_rollno and student_grade:
        cursor.execute("INSERT INTO students VALUES (?, ?, ?)", (student_username, student_rollno, student_grade))
        conn.commit()

        # Show a success message
        message_label.config(text="Student added successfully", fg="green")

        username_entry.delete(0, tk.END)
        rollno_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)
    else:
        # Show an error message
        message_label.config(text="Please fill in all fields", fg="red")

# Function to show all students
def show_students():
    student_listbox.delete(0, tk.END)  # Clear the listbox
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for student in students:
        student_listbox.insert(tk.END, student)


# Login function
def login():
    if login_username_entry.get() == 'admin' and login_password_entry.get() == 'admin':
        login_frame.pack_forget()  # Hide login frame
        main_frame.pack()  # Show the main frame
    else:
        login_error_label.config(text="Invalid credentials")

# Create the main window with larger dimensions
root = tk.Tk()
root.title("Student Management System")
root.geometry("800x600")  # Set the initial window size

# Create a login frame
login_frame = tk.Frame(root)
login_frame.pack()

login_label = tk.Label(login_frame, text="Login")
login_label.pack()

login_username_label = tk.Label(login_frame, text="Username")
login_username_label.pack()
login_username_entry = tk.Entry(login_frame)
login_username_entry.pack()

login_password_label = tk.Label(login_frame, text="Password")
login_password_label.pack()
login_password_entry = tk.Entry(login_frame, show="*")
login_password_entry.pack()

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack()

login_error_label = tk.Label(login_frame, text="", fg="red")
login_error_label.pack()

# Create a main frame with larger dimensions
main_frame = tk.Frame(root, width=100, height=100)
main_frame.pack()

username_label = tk.Label(main_frame, text="Username")
username_label.pack()
username_entry = tk.Entry(main_frame)
username_entry.pack()

rollno_label = tk.Label(main_frame, text="Roll No")
rollno_label.pack()
rollno_entry = tk.Entry(main_frame)
rollno_entry.pack()

grade_label = tk.Label(main_frame, text="Grade")
grade_label.pack()
grade_entry = tk.Entry(main_frame)
grade_entry.pack()

add_student_button = tk.Button(main_frame, text="Add Student", command=insert_student)
add_student_button.pack()

show_students_button = tk.Button(main_frame, text="Show Students", command=show_students)
show_students_button.pack()

message_label = tk.Label(main_frame, text="", fg="green")
message_label.pack()
student_listbox = tk.Listbox(main_frame)
student_listbox.pack()
main_frame.pack()
main_frame.pack_forget()  # Hide the main frame initially
root.mainloop()
