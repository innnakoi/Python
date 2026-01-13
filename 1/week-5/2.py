import json

with open("22.json", "r", encoding="utf-8") as file:
    students = json.load(file)

for student in students:
    grades = student["grades"]
    student["average_grade"] = sum(grades) / len(grades)

with open("students_updated.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)
