class SchoolManagement:
    def __init__(self, school_name, address, contact_number, medium_of_study):
        self.school_name = school_name
        self.address = address
        self.contact_number = contact_number
        self.medium_of_study = medium_of_study

class Classroom:
    def __init__(self, class_id, class_name, teacher_id, student_count, equipment_id):
        self.class_id = class_id
        self.class_name = class_name
        self.teacher_id = teacher_id
        self.student_count = student_count
        self.equipment_id = equipment_id

class Student:
    def __init__(self, student_id, student_name, class_id, section, bus_id):
        self.student_id = student_id
        self.student_name = student_name
        self.class_id = class_id
        self.section = section
        self.bus_id = bus_id

class Department:
    def __init__(self, department_id, department_name, incharge_name, member_list):
        self.department_id = department_id
        self.department_name = department_name
        self.incharge_name = incharge_name
        self.member_list = member_list

class Teacher:
    def __init__(self, employee_id, employee_name, salary, department_id):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.salary = salary
        self.department_id = department_id

# Creating instances
school = SchoolManagement("ABC School", "123 Main St", "123-456-7890", "English")
classroom = Classroom(1, "Class 10A", 101, 30, 1)
student = Student(1001, "John Doe", 1, "A", 1)
department = Department(1, "Science", "Dr. Smith", ["Teacher1", "Teacher2"])
teacher = Teacher(101, "Ms. Johnson", 50000, 1)

# Printing information
print(f"School Name: {school.school_name}")
print(f"Classroom Name: {classroom.class_name}")
print(f"Student Name: {student.student_name}")
print(f"Department Name: {department.department_name}")
print(f"Teacher Name: {teacher.employee_name}")
