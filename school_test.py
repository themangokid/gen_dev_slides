class School:
    def __init__(self):
        self.student_list = []
        self.parent_list = []
        self.teacher_list = []
        self.schedule = {}
        self.grades = {}
        self.ews = {}

    def enroll_student(self, student, parent):
        self.student_list.append(student)
        self.parent_list.append(parent)
        print(f'{student} has been enrolled in the school.')

    def add_parent(self, parent):
        self.parent_list.append(parent)
        print(f'{parent} has been added to the school\'s parent list.')

    def hire_teacher(self, teacher):
        self.teacher_list.append(teacher)
        print(f'{teacher} has been hired as a new teacher.')

    def expand(self):
        print('Expansion process has begun.')

    def order_office_supply(self, supply):
        print(f'{supply} has been ordered.')

    def deliver_office_supply(self, supply):
        print(f'{supply} has been delivered.')

    def create_schedule(self):
        print('Schedule has been created.')

    def update_schedule(self):
        print('Schedule has been updated.')

    def grading(self, student, grade):
        self.grades[student] = grade
        print(f'{student} has been graded.')

    def grades(self):
        print(self.grades)

    def ews(self):
        print('Early Warning System alerts have been generated.')

    def meetings(self):
        print('Meetings have been scheduled.')

    def marketing(self):
        print('Marketing campaigns have been launched.')


# Example usage:
school = School()

# Enrolling new students
student = "John Doe"
parent = "Jane Doe"
school.enroll_student(student, parent)
school.add_parent(parent)

# Hiring new teachers
teacher = "Mr. Smith"
school.hire_teacher(teacher)

# Expanding the school
school.expand()

# Ordering office supplies
supply = "paper"
school.order_office_supply(supply)
school.deliver_office_supply(supply)

# Creating a schedule
school.create_schedule()
school.update_schedule()

# Grading and reporting
school.grading("John Doe", "A")

# Holding meetings
school.meetings()

# Marketing
school.marketing()