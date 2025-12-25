class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'
        if course not in self.courses_in_progress:
            return 'Ошибка'
        if course not in lecturer.courses_attached:
            return 'Ошибка'
        if grade < 1 or grade > 10:
            return 'Ошибка'
        
        if course in lecturer.grades:
            lecturer.grades[course] += [grade]
        else:
            lecturer.grades[course] = [grade]
    
    def get_average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0
    
    def __str__(self):
        avg_grade = self.get_average_grade()
        in_progress = ', '.join(self.courses_in_progress) if self.courses_in_progress else 'Нет курсов'
        finished = ', '.join(self.finished_courses) if self.finished_courses else 'Нет курсов'
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {avg_grade:.1f}\n" \
               f"Курсы в процессе изучения: {in_progress}\n" \
               f"Завершенные курсы: {finished}"
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()
    
    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() <= other.get_average_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def get_average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0
    
    def __str__(self):
        avg_grade = self.get_average_grade()
        return f"{super().__str__()}\nСредняя оценка за лекции: {avg_grade:.1f}"
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()
    
    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() <= other.get_average_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() == other.get_average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if not isinstance(student, Student):
            return 'Ошибка'
        if course not in self.courses_attached:
            return 'Ошибка'
        if course not in student.courses_in_progress:
            return 'Ошибка'
        if grade < 1 or grade > 10:
            return 'Ошибка'
        
        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]


def calculate_average_hw_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    
    if not total_grades:
        return 0
    
    return sum(total_grades) / len(total_grades)


def calculate_average_lecture_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    
    if not total_grades:
        return 0
    
    return sum(total_grades) / len(total_grades)



# Задача № 2
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))
print(student.rate_lecture(lecturer, 'Java', 8))
print(student.rate_lecture(lecturer, 'С++', 8))
print(student.rate_lecture(reviewer, 'Python', 6))

print(lecturer.grades)

# Задание № 3
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress = ['Python', 'Git']
some_student.finished_courses = ['Введение в программирование']
some_student.grades = {'Python': [10, 9, 10], 'Git': [8, 9]}

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.grades = {'Python': [9, 10, 9], 'C++': [8, 9]}

some_reviewer = Reviewer('Some', 'Buddy')

print(some_reviewer)
print(some_lecturer)
print(some_student)

student1 = Student('Иван', 'Петров', 'М')
student1.grades = {'Python': [8, 9, 7]}

student2 = Student('Мария', 'Сидорова', 'Ж')
student2.grades = {'Python': [9, 10, 9]}

lecturer1 = Lecturer('Алексей', 'Иванов')
lecturer1.grades = {'Python': [8, 8, 9]}

lecturer2 = Lecturer('Ольга', 'Смирнова')
lecturer2.grades = {'Python': [9, 10, 9]}

print(f"student1 < student2: {student1 < student2}")
print(f"student1 > student2: {student1 > student2}")
print(f"student1 == student2: {student1 == student2}")

print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")

# Задача № 4 
student_a = Student('Иван', 'Петров', 'М')
student_a.courses_in_progress = ['Python', 'Git']
student_a.finished_courses = ['Введение в программирование']

student_b = Student('Мария', 'Сидорова', 'Ж')
student_b.courses_in_progress = ['Python', 'C++']

lecturer_a = Lecturer('Алексей', 'Иванов')
lecturer_a.courses_attached = ['Python', 'Git']

lecturer_b = Lecturer('Ольга', 'Смирнова')
lecturer_b.courses_attached = ['Python', 'Java']

reviewer_a = Reviewer('Дмитрий', 'Кузнецов')
reviewer_a.courses_attached = ['Python', 'Git']

reviewer_b = Reviewer('Екатерина', 'Попова')
reviewer_b.courses_attached = ['Python', 'C++']

reviewer_a.rate_hw(student_a, 'Python', 9)
reviewer_a.rate_hw(student_a, 'Python', 10)
reviewer_a.rate_hw(student_a, 'Python', 8)
reviewer_a.rate_hw(student_a, 'Git', 9)

reviewer_b.rate_hw(student_b, 'Python', 7)
reviewer_b.rate_hw(student_b, 'Python', 9)
reviewer_b.rate_hw(student_b, 'C++', 8)

student_a.rate_lecture(lecturer_a, 'Python', 9)
student_a.rate_lecture(lecturer_a, 'Python', 10)
student_b.rate_lecture(lecturer_a, 'Python', 8)

student_a.rate_lecture(lecturer_b, 'Python', 7)
student_b.rate_lecture(lecturer_b, 'Python', 9)

# Маг Мет
print(student_a)
print(lecturer_a)
print(reviewer_a)

# Сравнение
print(f"student_a < student_b: {student_a < student_b}")
print(f"lecturer_a < lecturer_b: {lecturer_a < lecturer_b}")

# Новые функции
students_list = [student_a, student_b]
lecturers_list = [lecturer_a, lecturer_b]

avg_hw_python = calculate_average_hw_grade(students_list, 'Python')
avg_lecture_python = calculate_average_lecture_grade(lecturers_list, 'Python')

print(avg_hw_python)
print(avg_lecture_python)