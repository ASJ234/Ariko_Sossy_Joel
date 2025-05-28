class Person:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.id_number}"

    def role(self):
        return "Person"


class Student(Person):
    def __init__(self, name, age, id_number, student_id, major):
        super().__init__(name, age, id_number)
        self.student_id = student_id
        self.major = major

    def display_info(self):  # Method overriding
        base_info = super().display_info()
        return f"{base_info}, Student ID: {self.student_id}, Major: {self.major}"

    def role(self):
        return "Student"


class Lecturer(Person):
    def __init__(self, name, age, id_number, employee_id, department):
        super().__init__(name, age, id_number)
        self.employee_id = employee_id
        self.department = department

    def display_info(self):  # Method overriding
        base_info = super().display_info()
        return f"{base_info}, Employee ID: {self.employee_id}, Department: {self.department}"

    def role(self):
        return "Lecturer"


class Staff(Person):
    def __init__(self, name, age, id_number, employee_id, job_title):
        super().__init__(name, age, id_number)
        self.employee_id = employee_id
        self.job_title = job_title

    def display_info(self):  # Method overriding
        base_info = super().display_info()
        return f"{base_info}, Employee ID: {self.employee_id}, Job Title: {self.job_title}"

    def role(self):
        return "Staff"


# Example usage
if __name__ == "__main__":
    # Create instances
    student = Student("Alice", 20, "P123", "S001", "Computer Science")
    lecturer = Lecturer("Dr. Smith", 45, "P456", "L001", "Engineering")
    staff = Staff("John", 35, "P789", "S002", "Admin Assistant")

    # Display information
    print(f"Role: {student.role()}")
    print(student.display_info())
    print(f"\nRole: {lecturer.role()}")
    print(lecturer.display_info())
    print(f"\nRole: {staff.role()}")
    print(staff.display_info())