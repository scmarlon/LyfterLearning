import csv

# This function exports the student data to a CSV file named 'students.csv'. It includes the student's name, group, and their grades for each course. The grades are formatted as "course: grade" pairs, separated by semicolons.
def export_data_CSV():
    from actions import student_list
    if not student_list or student_list == [{}]:
        print("No students to export.")
        return
    try:
        with open('students.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Group', 'Grades'])
            for student in student_list:
                grades_str = '; '.join([f"{course}: {grade}" for course, grade in student['grades'].items()])
                writer.writerow([student['name'], student['group'], grades_str])
        print("\nStudent data exported successfully to students.csv.")
    except Exception as e:
        print(f"An error occurred while exporting data to CSV: {e}")


# This function imports student data from a CSV file named 'students.csv'. If the file does not exist, it handles the FileNotFoundError and returns an empty list.
def import_data_CSV():
    student_list = []
    try:
        with open('students.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                group = row['Group']
                grades_str = row['Grades']
                grades = {}
                for course_grade in grades_str.split(';'):
                    course, grade = course_grade.split(':')
                    grades[course.strip()] = int(grade.strip())
                student_list.append({'name': name, 'group': group, 'grades': grades})
        print("\nStudent data imported successfully from students.csv.")
        print("Current student list:\n", student_list)
    except FileNotFoundError:
        print("\nNo existing student data CSV file found.")
        return []