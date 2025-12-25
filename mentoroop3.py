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
        """Вычисление средней оценки за домашние задания"""
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
        """Вычисление средней оценки за лекции"""
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


#  задание № 2
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка  
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка

print(lecturer.grades)  # {'Python': [7]}

#  задание № 3
print("\n=== ТЕСТ ЗАДАНИЯ № 3 ===")

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress = ['Python', 'Git']
some_student.finished_courses = ['Введение в программирование']
some_student.grades = {'Python': [10, 9, 10], 'Git': [8, 9]}

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.grades = {'Python': [9, 10, 9], 'C++': [8, 9]}

some_reviewer = Reviewer('Some', 'Buddy')

print("\nПроверяющий:")
print(some_reviewer)

print("\nЛектор:")
print(some_lecturer)

print("\nСтудент:")
print(some_student)


student1 = Student('Иван', 'Петров', 'М')
student1.grades = {'Python': [8, 9, 7]}

student2 = Student('Мария', 'Сидорова', 'Ж')
student2.grades = {'Python': [9, 10, 9]}

lecturer1 = Lecturer('Алексей', 'Иванов')
lecturer1.grades = {'Python': [8, 8, 9]}

lecturer2 = Lecturer('Ольга', 'Смирнова')
lecturer2.grades = {'Python': [9, 10, 9]}

print(f"\nСравнение студентов:")
print(f"student1 < student2: {student1 < student2}")
print(f"student1 > student2: {student1 > student2}")
print(f"student1 == student2: {student1 == student2}")

print(f"\nСравнение лекторов:")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")