class Student:
    students_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.students_list.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def lecturer_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course not in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] = [grade]
            else:
                lecturer.lecturer_grades[course].append(grade)
        else:
            print('Ошибка!')

    def __str__(self):
        values_sum = 0
        grades_count = 0
        for val in self.grades.values():
            for value in val:
                values_sum += value
                grades_count += 1
        average_sum = values_sum / grades_count
        student_info = f'''Имя: {self.name}\nФамилия: {self.surname}
Средняя оценка за домашнее задание: {average_sum}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершённые курсы: {", ".join(self.finished_courses)}'''
        return student_info


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturers_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}
        Lecturer.lecturers_list.append(self)

    def __average_grades_sum(self, grades):
        values_sum = 0
        grades_count = 0
        for val in grades.values():
            for value in val:
                values_sum += value
                grades_count += 1
        average_grades_sum = values_sum / grades_count
        return average_grades_sum

    def __str__(self):
        lecturer_info = f'''Имя: {self.name}\nФамилия: {self.surname}
Средняя оценка за лекции: {self.__average_grades_sum(self.lecturer_grades)}'''
        return lecturer_info

    def __lt__(self, second):
        if not isinstance(second, Lecturer):
            return
        return self.__average_grades_sum(self.lecturer_grades) < second.__average_grades_sum(second.lecturer_grades)

    def __eq__(self, second):
        if not isinstance(second, Lecturer):
            return
        return self.__average_grades_sum(self.lecturer_grades) == second.__average_grades_sum(second.lecturer_grades)

    def __le__(self, second):
        if not isinstance(second, Lecturer):
            return
        return self.__average_grades_sum(self.lecturer_grades) <= second.__average_grades_sum(second.lecturer_grades)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        reviewer_info = f'Имя: {self.name}\nФамилия: {self.surname}'
        return reviewer_info

def average_course_grade(course):
    values_sum = 0
    grades_count = 0
    for student in Student.students_list:
        if course not in student.grades:
            continue
        for val in student.grades[course]:
            values_sum += int(val)
            grades_count += 1
    average_sum = round(values_sum / grades_count, 2)
    return average_sum

def average_lecturers_grade(course):
    values_sum = 0
    grades_count = 0
    for lecturer in Lecturer.lecturers_list:
        if course not in lecturer.lecturer_grades:
            continue
        for val in lecturer.lecturer_grades[course]:
            values_sum += int(val)
            grades_count += 1
    average_sum = round(values_sum / grades_count, 2)
    return average_sum

cool_lecturer = Lecturer('Patrick', 'Wigare')
cool_lecturer.courses_attached += ['Python']

not_cool_lecturer = Lecturer('Fargick', 'Gooblestone')
not_cool_lecturer.courses_attached += ['Git']

not_best_student = Student('Gregory', 'House', 'male')
not_best_student.courses_in_progress += ['Python', 'Git']
not_best_student.finished_courses += ['Введение в программирование']
not_best_student.lecturer_grade(cool_lecturer, 'Python', 5)
not_best_student.lecturer_grade(cool_lecturer, 'Python', 6)
not_best_student.lecturer_grade(not_cool_lecturer, 'Git', 2)

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']
best_student.lecturer_grade(cool_lecturer, 'Python', 8)
best_student.lecturer_grade(cool_lecturer, 'Python', 9)
best_student.lecturer_grade(not_cool_lecturer, 'Git', 3)

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 9)

not_cool_reviewer = Reviewer('Some', 'Buddy')
not_cool_reviewer.courses_attached += ['Python']
not_cool_reviewer.rate_hw(not_best_student, 'Python', 5)
not_cool_reviewer.rate_hw(not_best_student, 'Python', 3)
not_cool_reviewer.rate_hw(not_best_student, 'Python', 3)

print('----')
print(best_student.grades)
print(cool_lecturer.lecturer_grades)
print('----')
print(best_student)
print('----')
print(cool_lecturer)
print('----')
print(cool_reviewer)
print('----')
print(not_cool_lecturer < cool_lecturer)
print(cool_lecturer == not_cool_lecturer)
print('----')
print(f"{average_course_grade('Python')}")
print('----')
print(average_lecturers_grade('Python'))