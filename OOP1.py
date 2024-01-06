class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def avg_rate(self):
        all_grades = [int(grade) for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания:{self.avg_rate()}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        return self.avg_rate() < other.avg_rate()

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (
                course in self.courses_in_progress or course in self.finished_courses) and course in lecturer.courses_attached:
            if course in lecturer.dict_grade.keys():
                lecturer.dict_grade[course] += [grade]
            else:
                lecturer.dict_grade[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.dict_grade = {}

    def avg_rate_lect(self):
        all_grades = [int(grade) for grades in self.dict_grade.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции:{self.avg_rate_lect()}\n"

    def __lt__(self, other):
        return self.avg_rate_lect() < other.avg_rate_lect()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n"


best_student = Student('Ruoy', 'Eman', 'f')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['JS']

best_student_2 = Student('Tom', 'Tom', 'f')
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['Java']
best_student_2.finished_courses += ['JS']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Sam', 'Jonson')
reviewer_2.courses_attached += ['Java']

lecturer_1 = Lecturer('Anna', 'Smit')
lecturer_1.courses_attached += ['Java']

lecturer_2 = Lecturer('Bob', 'Pit')
lecturer_2.courses_attached += ['Python']

best_student.rate_lecture(lecturer_1, 'Java', 10)
best_student.rate_lecture(lecturer_1, 'Java', 5)

best_student.rate_lecture(lecturer_2, 'Python', 7)
best_student.rate_lecture(lecturer_2, 'Python', 5)

reviewer_1.rate_hw(best_student, 'Python', 10)
reviewer_1.rate_hw(best_student_2, 'Python', 5)

reviewer_2.rate_hw(best_student, 'Java', 5)
reviewer_2.rate_hw(best_student_2, 'Java', 5)

print(best_student)
print('---------------')
print(best_student_2)
print('---------------')

print(lecturer_1)
print('---------------')
print(lecturer_2)

print(reviewer_1)
print('---------------')
print(reviewer_2)
print('---------------')

print(lecturer_1 < lecturer_2)
print('---------------')
print(best_student > best_student_2)
print('---------------')


def get_avg_grade_course(list_students, course):
    grades = []
    for student in list_students:
        for courses, grade in student.grades.items():
            if courses == course:
                for i in grade:
                    grades.append(i)

    if len(grades) == 0:
        print('Оценок нет')
    else:
        return round(sum(grades) / len(grades), 1)


def get_avg_grade_course_lect(list_lect, course):
    grades = []
    for lecturer in list_lect:
        for courses, grade in lecturer.dict_grade.items():
            if courses == course:
                for i in grade:
                    grades.append(i)

    if len(grades) == 0:
        print('Оценок нет')
    else:
        return round(sum(grades) / len(grades), 1)


print(get_avg_grade_course([best_student, best_student_2], 'Python'))
print('---------------')
print(get_avg_grade_course([best_student, best_student_2], 'Java'))
print('---------------')

print(get_avg_grade_course_lect([lecturer_1, lecturer_2], 'Python'))
print('---------------')
print(get_avg_grade_course_lect([lecturer_1, lecturer_2], 'Java'))
