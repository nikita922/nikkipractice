# Input marks for 3 subjects
subject1 = float(input("Enter marks for Subject 1 out of 100: "))
subject2 = float(input("Enter marks for Subject 2 out of 100: "))
subject3 = float(input("Enter marks for Subject 3 out of 100: "))

# Calculate the average marks
average_marks = (subject1 + subject2 + subject3) / 3

# Calculate the grade
if average_marks >= 90:
    grade = 'A+'
elif 80 <= average_marks < 90:
    grade = 'A'
elif 70 <= average_marks < 80:
    grade = 'B'
elif 60 <= average_marks < 70:
    grade = 'C'
elif 50 <= average_marks < 60:
    grade = 'D'
else:
    grade = 'F'

# Display the result
print("Grade: ", grade)
