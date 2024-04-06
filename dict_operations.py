# Create a dictionary for 5 students
students = {
    'student1': {
        'name': 'Nikita',
        'address': '123 Mumbai',
        'age': 18,
        'class': '12th',
        'marks': {
            'math': 85,
            'science': 92,
            'history': 78,
            'english': 88,
            'art': 95
        }
    },
    'student2': {
        'name': 'Pavitra',
        'address': '456 Mumbai',
        'age': 17,
        'class': '11th',
        'marks': {
            'math': 90,
            'science': 88,
            'history': 76,
            'english': 91,
            'art': 84
        }
    },
    'student3': {
        'name': 'Huda',
        'address': '789 Mumbai',
        'age': 19,
        'class': '12th',
        'marks': {
            'math': 78,
            'science': 85,
            'history': 92,
            'english': 80,
            'art': 89
        }
    },
    'student4': {
        'name': 'Muskan',
        'address': '101 Mumbai',
        'age': 17,
        'class': '11th',
        'marks': {
            'math': 92,
            'science': 84,
            'history': 76,
            'english': 90,
            'art': 82
        }
    },
    'student5': {
        'name': 'Sanya',
        'address': '202 Mumbai',
        'age': 18,
        'class': '12th',
        'marks': {
            'math': 88,
            'science': 90,
            'history': 85,
            'english': 87,
            'art': 91
        }
    }
}

print("Details of All the Students :")
# Display the information for each student
for student_id, student_info in students.items():
    print(f"Student ID: {student_id}")
    print(f"Name: {student_info['name']}")
    print(f"Address: {student_info['address']}")
    print(f"Age: {student_info['age']}")
    print(f"Class: {student_info['class']}")
    print("Marks:")
    for subject, marks in student_info['marks'].items():
        print(f"{subject}: {marks}")
    print()

# Search for a student by ID
search_id = 'student3'
if search_id in students:
    print(f"Student ID: {search_id}")
    student_info = students[search_id]
    print(f"Name: {student_info['name']}")
else:
    print(f"Student with ID '{search_id}' not found")

# Delete a student by ID
delete_id = 'student4'
if delete_id in students:
    del students[delete_id]
    print(f"Student with ID '{delete_id}' deleted from the dictionary")
else:
    print(f"Student with ID '{delete_id}' not found in the dictionary")
