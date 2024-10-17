# Base University Class
class University:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"\n{'-'*10} University Info {'-'*10}")
        print(f"University Name: {self.name}")
        print(f"{'-'*35}\n")


# Human Class inheriting University
class Human(University):
    def __init__(self, name):
        super().__init__(name)
        self.list_of_labor = []
        self.list_of_teacher = []
        self.list_of_student = []
        self.list_of_librarian = []

    def add_labor(self, labor):
        self.list_of_labor.append(labor)

    def add_teacher(self, teacher):
        self.list_of_teacher.append(teacher)

    def add_student(self, student):
        self.list_of_student.append(student)

    def add_librarian(self, librarian):
        self.list_of_librarian.append(librarian)

    def show_human_resources(self):
        print(f"\n{'-'*10} Human Resources {'-'*10}")
        print(f"Labor: {', '.join(self.list_of_labor)}")
        print(f"Teachers: {', '.join(self.list_of_teacher)}")
        print(f"Students: {', '.join(self.list_of_student)}")
        print(f"Librarians: {', '.join(self.list_of_librarian)}")
        print(f"{'-'*35}\n")


# Campus Class inheriting University
class Campus(University):
    def __init__(self, name):
        super().__init__(name)
        self.list_of_campus = []

    def add_campus(self, campus_name):
        self.list_of_campus.append(campus_name)

    def show_campuses(self):
        print(f"\n{'-'*10} University Campuses {'-'*10}")
        print(f"Campuses: {', '.join(self.list_of_campus)}")
        print(f"{'-'*35}\n")


# Library Class inheriting University
class Library(University):
    def __init__(self, name):
        super().__init__(name)
        self.list_of_books = []
        self.list_of_categories = []

    def add_book(self, book_name):
        self.list_of_books.append(book_name)

    def add_category(self, category_name):
        self.list_of_categories.append(category_name)

    def show_library(self):
        print(f"\n{'-'*10} Library Info {'-'*10}")
        print(f"Books: {', '.join(self.list_of_books)}")
        print(f"Categories: {', '.join(self.list_of_categories)}")
        print(f"{'-'*35}\n")


# Classes Class for listing Class A, Class B, Class C
class Classes:
    def __init__(self):
        self.list_of_classes = ["Class A", "Class B", "Class C"]

    def show_classes(self):
        print(f"\n{'-'*10} Classes Info {'-'*10}")
        print(f"Available Classes: {', '.join(self.list_of_classes)}")
        print(f"{'-'*35}\n")


# Student Class inheriting Classes
class Student(Classes):
    def __init__(self, student_name, student_roll_no, student_subject, student_teacher, student_CR=False):
        super().__init__()
        self.student_name = student_name
        self.student_roll_no = student_roll_no
        self.student_subject = student_subject
        self.student_teacher = student_teacher
        self.student_CR = student_CR

    def show_student_info(self):
        cr_status = "Yes" if self.student_CR else "No"
        print(f"\n{'-'*10} Student Info {'-'*10}")
        print(f"Student Name: {self.student_name}")
        print(f"Roll No: {self.student_roll_no}")
        print(f"Subject: {self.student_subject}")
        print(f"Teacher: {self.student_teacher}")
        print(f"Class Representative: {cr_status}")
        print(f"{'-'*35}\n")


# Teacher Class inheriting Classes
class Teacher(Classes):
    def __init__(self, teacher_name, teacher_number, teacher_subject, teacher_of_classes, teacher_head_of_department=False):
        super().__init__()
        self.teacher_name = teacher_name
        self.teacher_number = teacher_number
        self.teacher_subject = teacher_subject
        self.teacher_of_classes = teacher_of_classes
        self.teacher_head_of_department = teacher_head_of_department

    def show_teacher_info(self):
        hod_status = "Yes" if self.teacher_head_of_department else "No"
        print(f"\n{'-'*10} Teacher Info {'-'*10}")
        print(f"Teacher Name: {self.teacher_name}")
        print(f"Teacher Number: {self.teacher_number}")
        print(f"Subject: {self.teacher_subject}")
        print(f"Classes: {', '.join(self.teacher_of_classes)}")
        print(f"Head of Department: {hod_status}")
        print(f"{'-'*35}\n")


# Example Usage
if __name__ == "__main__":

    print("------------Create University------")
    # Create University
    university = University("Panaversity University of Technology")
    university.show_info()

    print("-------------- Human Resources--------")
    # Human Resources
    human_resources = Human("Panaversity University of Technology")
    human_resources.add_labor("Waris")
    human_resources.add_teacher("Sir Zia Khan")
    human_resources.add_student("Faizan")
    human_resources.add_librarian("Arooba")
    human_resources.show_human_resources()

    print("---------------Campus Management------")
    # Campus Management
    university_campus = Campus("Panaversity University of Technology")
    university_campus.add_campus("Electronic")
    university_campus.add_campus("Computer")
    university_campus.add_campus("Civil")
    university_campus.show_campuses()

    print("----------- Library Management-----------")
    # Library Management
    cs_library = Library("Panaversity Library")
    cs_library.add_book("Data Structures in Python")
    cs_library.add_category("Programming")
    cs_library.show_library()

    print("------------Classes Info----------")
    # Classes Info
    available_classes = Classes()
    available_classes.show_classes()

    print("-----------Student Info-----------")
    # Student Info
    student1 = Student("Ali", "112233", "CS101", "Sir Zia Khan", student_CR=True)
    student1.show_student_info()

    print("-------------Teacher Info------------")
    # Teacher Info
    teacher1 = Teacher("Sir Zia Khan", "T-101", "CS101", ["Class A", "Class B"], teacher_head_of_department=True)
    teacher1.show_teacher_info()
