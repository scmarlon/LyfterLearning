import csv

# This function exports the student data to a CSV file named 'students.csv'. It includes the student's name, group, and their grades for each course. The grades are formatted as "course: grade" pairs, separated by semicolons.
def export_data_CSV():
    from actions import student_list
    with open('students.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Group', 'Grades'])
        for student in student_list:
            grades_str = '; '.join([f"{course}: {grade}" for course, grade in student['grades'].items()])
            writer.writerow([student['name'], student['group'], grades_str])
            
export_data_CSV()