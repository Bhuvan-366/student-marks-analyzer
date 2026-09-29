import csv
import os

def read_students(file_path):
    students = []

    os.makedirs("reports",exist_ok=True)
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append({
                "name": row["Name"],
                "marks": int(row["Marks"])
            })

    return students


def calculate_average(students):
    total_marks = sum(student["marks"] for student in students)
    return total_marks / len(students)


def find_topper(students):
    return max(students, key=lambda student: student["marks"])


def main():
    students = read_students("data/students.csv")

    average = calculate_average(students)
    topper = find_topper(students)

    report = f"""Student Marks Report
====================

Average Marks: {average:.2f}

Topper:
{topper['name']} - {topper['marks']}

Total Students:
{len(students)}
"""

    with open("reports/report.txt", "w") as file:
        file.write(report)

    print("Report Generated Successfully")

if __name__ == "__main__":
    main()