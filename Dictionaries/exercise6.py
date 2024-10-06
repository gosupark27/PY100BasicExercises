# Check whether the keys 'name' and 'grade' exist in the following dictionary:
student = {
    'id': 123,
    'grade': 'B',
}
print(f'Name: {student.get('name')}')
print(f'Grade: {student.get('grade')}')
# LS answer
print('name' in student)
print('grade' in student)