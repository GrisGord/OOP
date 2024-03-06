import statistics

                        # Задания 1, 2, 3.
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_sw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached\
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"\nРецензент\nИмя: {self.name}\nФамилия: {self.surname}\n"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_lr = []

    def avg_lec_rate(self):
        for k, v in self.grades.items():
            self.avg_lr.append(statistics.mean(v))
        for el in self.avg_lr:
            return statistics.mean(self.avg_lr)

    def __str__(self):
        return f"\nЛектор\nИмя: {self.name}\nФамилия: {self.surname}\
        \nСредняя оценка за лекции: {self.avg_lec_rate()}"

    def __lt__(self, other):
        if self.avg_lec_rate() < other.avg_lec_rate():
            print(f'Средние оценки {self.name} {self.surname} меньше средних оценок'
                  f' {other.name} {other.surname}')
        else:
            print(f'Средние оценки {self.name} {self.surname} больше средних оценок'
                  f' {other.name} {other.surname}')

    def __eq__(self, other):
        if self.avg_lec_rate() == other.avg_lec_rate(): print('Средние оценки лекторов равны')
        else: print('Средние оценки лекторов отличаются')

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_stu_rate_list = []

    def rate_lec_work(self, lecturer, course, grade: int):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached\
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else: lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_stu_rate(self):
        for k, v in self.grades.items():
            self.avg_stu_rate_list.append(statistics.mean(v))
        for el in self.avg_stu_rate_list:
            return statistics.mean(self.avg_stu_rate_list)

    def __str__(self):
        return (f"\nСтудент\nИмя: {self.name}\nФамилия: {self.surname}\
        \nСредняя оценка за домашние задания: {self.avg_stu_rate()}\
        \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\
        \nЗавершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        if self.avg_stu_rate() < other.avg_stu_rate():
            print(f'Средние оценки {self.name}a {self.surname}a меньше средних оценок'
                    f' {other.name}a {other.surname}a')
        else:
            print(f'Средние оценки {self.name}a {self.surname}a больше средних оценок'
                    f' {other.name}a {other.surname}a')

    def __eq__(self, other):
        if self.avg_stu_rate() == other.avg_stu_rate():
            print('Средние оценки студентов равны')
        else:
            print('Средние оценки студентов отличаются')


                            # Экземпляры
rev_1 = Reviewer('Vasily', 'Pupkin')
rev_1.courses_attached += ['Python', 'PHP', 'SQL']

rev_2 = Reviewer("Valera", 'Ivanov')
rev_2.courses_attached += ['Python', 'JS', 'SQL']

lec_1 = Lecturer('Fedor', 'Dostoevsky')
lec_1.courses_attached += ['PHP', 'SQL', 'Python']

lec_2 = Lecturer('Alexander', 'Pushkin')
lec_2.courses_attached += ['Python', 'JS', 'SQL']

stu_1 = Student('Ivan', 'Petrov', 'male')
stu_1.courses_in_progress += ['Python', 'JS', 'PHP', 'SQL']
stu_1.finished_courses += ['Java', 'C+']

stu_2 = Student('Stanislav', 'Ivanov', 'male')
stu_2.courses_in_progress += ['Python', 'SQL', 'JS']
stu_2.finished_courses += ['Java', 'C+']


                            # студенты выставляют оценки лекторам по курсам
stu_1.rate_lec_work(lec_1, 'SQL', 10)
stu_1.rate_lec_work(lec_1, 'Python', 10)

stu_1.rate_lec_work(lec_2, 'Python', 9)
stu_1.rate_lec_work(lec_2, 'SQL', 10)

stu_2.rate_lec_work(lec_1, 'SQL', 7)
stu_2.rate_lec_work(lec_1, 'Python', 9)

stu_2.rate_lec_work(lec_2, 'SQL', 6)
stu_2.rate_lec_work(lec_2, 'Python', 8)



                            # Ревьюверы выставляют оценки студентам по курсам
rev_1.rate_sw(stu_1, 'Python', 10)
rev_2.rate_sw(stu_1, 'Python', 9)
#
rev_1.rate_sw(stu_1, 'SQL', 9)
rev_2.rate_sw(stu_1, 'SQL', 8)

rev_1.rate_sw(stu_2, 'SQL', 5)
rev_2.rate_sw(stu_2, 'SQL', 6)

rev_1.rate_sw(stu_2, 'Python', 7)
rev_2.rate_sw(stu_2, 'Python', 8)


                             # Проверка задания 3
print(rev_1, rev_2)
print(lec_1, lec_2)
print(stu_1, stu_2)

Lecturer.__lt__(lec_1, lec_2)
Lecturer.__eq__(lec_1, lec_2)
Student.__lt__(stu_1, stu_2)
Student.__eq__(stu_1, stu_2)


                             # Задание 4 - функции
# Для студентов
stu_list = [stu_1, stu_2]

def get_avg_rate_scw(stu_list, course):
    stu_rate = []
    for students in stu_list:
        for rate in students.grades[course]:
            stu_rate.append(rate)
    print(f'Средняя оценка для всех студентов по курсу {course}: {sum(stu_rate) / len(stu_rate)}')


# проверка
get_avg_rate_scw(stu_list, 'Python')
get_avg_rate_scw(stu_list, 'SQL')


# Для лекторов
lec_list = [lec_1, lec_2]

def get_avg_rate_lcw(lec_list, course):
    lec_rate = []
    for lecturers in lec_list:
        for rate in lecturers.grades[course]:
                lec_rate.append(rate)
    print(f'Средняя оценка по всем лекторам курса {course}: {sum(lec_rate) / len(lec_rate)}')

# проверка
get_avg_rate_lcw(lec_list, 'Python')
get_avg_rate_lcw(lec_list, 'SQL')