# ------------------------------------------------------------
# TITLE: GradeBook Analyzer
# Author: ARTH RANA
# Date: 04 November 2025
# ------------------------------------------------------------

print("======================================")
print("   Welcome to the GradeBook Analyzer   ")
print("======================================")

print("\nMenu:")
print("1. Enter student data manually")
print("2. Exit")

marks = {}  
num_students = int(input("\nEnter number of students: "))

for i in range(num_students):
    name = input(f"Enter name of student {i+1}: ")
    score = float(input(f"Enter marks of {name}: "))
    marks[name] = score

print("\nAll student data stored successfully!")
print("Marks Dictionary:", marks)

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    sorted_scores = sorted(marks_dict.values())
    n = len(sorted_scores)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
    else:
        return sorted_scores[mid]

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())

print("\n--- Statistics ---")
print(f"Average Marks: {calculate_average(marks):.2f}")
print(f"Median Marks: {calculate_median(marks):.2f}")
print(f"Highest Marks: {find_max_score(marks)}")
print(f"Lowest Marks: {find_min_score(marks)}")

grades = {}

for name, mark in marks.items():
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "F"
    grades[name] = grade

grade_counts = {g: list(grades.values()).count(g) for g in set(grades.values())}

print("\n--- Grade Summary ---")
for g, count in grade_counts.items():
    print(f"{g}: {count} student(s)")
passed_students = [name for name, m in marks.items() if m >= 40]
failed_students = [name for name, m in marks.items() if m < 40]

print("\n--- Pass/Fail Summary ---")
print(f"Passed Students ({len(passed_students)}): {passed_students}")
print(f"Failed Students ({len(failed_students)}): {failed_students}")
while True:
    print("\n=== GradeBook Analyzer ===")
    print("1. Enter student data and analyze")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":

        print("\n--- Final Results ---")
        print(f"{'Name':<10}{'Marks':<10}{'Grade':<10}")
        print("-" * 30)

        for name in marks:
            print(f"{name:<10}{marks[name]:<10}{grades[name]:<10}")
            
    elif choice == "2":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")






