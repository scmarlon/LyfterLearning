import csv
from actions import student_exists

# This function exports the student data to a CSV file named 'students.csv'. It includes the student's name, group, and their grades for each course. The grades are formatted as "course: grade" pairs, separated by semicolons.
def export_data_CSV(student_list):
    if not student_list:
        print("No students to export.")
        return
    try:
        with open('students.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Group', 'Spanish', 'English', 'Science', 'Social Studies'])
            
            for student in student_list:
                grades = student["grades"]
                writer.writerow([
                    student['name'], 
                    student['group'],
                    grades.get('spanish', 'N/A'),
                    grades.get('english', 'N/A'),
                    grades.get('science', 'N/A'),
                    grades.get('social_studies', 'N/A')
                ])
        print("\nStudent data exported successfully to students.csv.")
    except Exception as e:
        print(f"An error occurred while exporting data to CSV: {e}")


# This function imports student data from a CSV file named 'students.csv'. If the file does not exist, it handles the FileNotFoundError and returns an empty list.
def import_data_CSV(student_list):
    try:
        with open('students.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                group = row['Group']
                spanish = row['Spanish']
                english = row['English']
                science = row['Science']
                social_studies = row['Social Studies']
                if not student_exists(name, group, student_list, check_coming = True):
                    student_list.append({
                        'name': name, 
                        'group': group, 
                        'grades': {
                            'spanish': int(spanish) if spanish.isdigit() else 'N/A', # This line checks if the Spanish grade is a digit before converting it to an integer. If it's not a digit, it assigns 'N/A' to indicate that the grade is not available or invalid.
                            'english': int(english) if english.isdigit() else 'N/A',
                            'science': int(science) if science.isdigit() else 'N/A',
                            'social_studies': int(social_studies) if social_studies.isdigit() else 'N/A'
                        }
                    })
                else:
                    print(f"Student {name} from group {group} already exists. Skipping import for this student.")
        print("\nStudent data imported successfully from students.csv.")
        return student_list
    except FileNotFoundError:
        print("\nNo existing student data CSV file found.")
        return student_list