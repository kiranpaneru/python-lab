print("--- DICTIONARY DEMONSTRATION ---")

student = {
    'name': 'Alice',
    'age': 22,
    'major': 'Computer Science',
    'gpa': 3.8
}
print("Original Dictionary:", student)

print("Student's Name:", student['name'])

print("Student's GPA using get():", student.get('gpa'))
print("Missing key using get():", student.get('graduation_year', 'Not Specified'))

student['graduation_year'] = 2026
student['gpa'] = 3.9
print("After adding/updating:", student)

student.update({'age': 23, 'honors': True})
print("After update() method:", student)

print("Dictionary Keys:", student.keys())
print("Dictionary Values:", student.values())
print("Dictionary Items:", student.items())

removed_major = student.pop('major')
print("Removed Major:", removed_major)

removed_item = student.popitem()
print("Removed last item:", removed_item)

student.clear()
print("Dictionary after clear():", student)
