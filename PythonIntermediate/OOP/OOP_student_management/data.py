import csv
from actions import student_exists
from actions import Student

# This function exports the student data to a CSV file named 'students.csv'. It includes the student's name, group, and their grades for each course. The grades are formatted as "course: grade" pairs, separated by semicolons.
def export_data_CSV(student_list):
    print("\nExporting student data to CSV...")
    if not student_list:
        print("No students to export.")
        return
    try:
        with open('students.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Group', 'Spanish', 'English', 'Science', 'Social Studies'])
            # Loop through each student in the student list and write their data to the CSV file, including their name, group, and grades for each course.
            for student in student_list:
                print(f"Exporting student: {student.name}, Group: {student.group}")
                grades = student.grades
                writer.writerow([
                    student.name, 
                    student.group, 
                    grades["spanish"], 
                    grades["english"], 
                    grades["science"], 
                    grades["social_studies"]
                ])
        print("\nStudent data exported successfully to students.csv.")
    except Exception as e:
        print(f"An error occurred while exporting data to CSV: {e}")

# This function imports student data from a CSV file named 'students.csv'. If the file does not exist, it handles the FileNotFoundError and returns an empty list.
def import_data_CSV(student_list):
    print("\nImporting student data from CSV...")
    try:
        with open('students.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            # Loop through each row in the CSV file and create a Student object for each student. Also checks if the student already exists... them to avoid duplicates.
            for row in reader:
                name = row['Name']
                group = row['Group']
                spanish = row['Spanish']
                english = row['English']
                science = row['Science']
                social_studies = row['Social Studies']
                student = Student(
                    name,
                    group,
                    {
                        'spanish': int(spanish) if spanish.isdigit() else 'N/A', # Convert the grade to an integer if it's a digit, otherwise set it to 'N/A'.
                        'english': int(english) if english.isdigit() else 'N/A',
                        'science': int(science) if science.isdigit() else 'N/A',
                        'social_studies': int(social_studies) if social_studies.isdigit() else 'N/A'
                    }
                )
                if not student_exists(name, group, student_list, check_coming = True):
                    student_list.append(student)
                else:
                    print(f"Student {name} from group {group} already exists. Skipping import for this student.")
        print("Student data imported successfully from students.csv.")
    except FileNotFoundError:
        print("File 'students.csv' not found.")
    except Exception as e:
        print(f"An error occurred while importing data from CSV: {e}")