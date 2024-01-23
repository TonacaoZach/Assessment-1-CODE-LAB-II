#Exercise 4

import matplotlib.pyplot as plt

def main():
    # Line 1
    x1, y1 = [1, 6], [2, 8]

    # Line 2
    x2, y2 = [1, 2, 6, 8], [3, 8, 1, 10]

    # Plotting
    plt.plot(x1, y1, label='Line 1', marker='o')
    plt.plot(x2, y2, label='Line 2', linestyle='dotted', marker='x')

    # Adding labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Graph')

    # Adding legend
    plt.legend()

    # Display the graph
    plt.show()

if __name__ == "__main__":
    main()


#Exercise 5
import json
import os

def write_to_json(student_data, filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, 'w') as file:
        json.dump(student_data, file, indent=4)

def read_from_json(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, 'r') as file:
        student_data = json.load(file)
        return student_data

def main():
    filename = 'StudentJson.json'

    # Task 1: Write to JSON
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    course = input("Enter course: ")

    student_data = {
        "Name": student_name,
        "ID": int(student_id),
        "course": course
    }

    write_to_json(student_data, filename)
    print("Student details written to JSON file.")

    # Task 2: Read from JSON
    read_data = read_from_json(filename)

    # Displaying individual values
    print("\nDetails of the Student are")
    print(f"Name: {read_data['Name']}")
    print(f"ID: {read_data['ID']}")
    print(f"course: {read_data['course']}")

    # Task 3: Append and Update JSON
    course_details = {
        "CourseDetails": {
            "Group": input("Enter Group: "),
            "Year": int(input("Enter Year: "))
        }
    }

    read_data.update(course_details)
    write_to_json(read_data, filename)

    # Displaying updated individual values
    print("\nDetails of the Student are")
    print(f"Name: {read_data['Name']}")
    print(f"ID: {read_data['ID']}")
    print(f"course: {read_data['course']}")
    print(f"Group: {read_data['CourseDetails']['Group']}")
    print(f"Year: {read_data['CourseDetails']['Year']}")

if __name__ == "__main__":
    main()
