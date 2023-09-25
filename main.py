class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
      res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._get_average_grade()}\nКурсы в процессе изучения: {" ". join(some_student1.courses_in_progress)}\nЗавершенные курсы: {" ". join(some_student1.finished_courses)}'
      return res
    def __str2__(self): 
      res2 = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._get_average_grade()}\nКурсы в процессе изучения: {" ". join(some_student2.courses_in_progress)}\nЗавершенные курсы: {" ". join(some_student2.finished_courses)}'
      return res2
    
    def _get_average_grade(self):
      sum_ = 0
      count = 0
      for course in self.grades.values():
        sum_ += sum(course)
        count += len(course)
      return round(sum_ / count, 2)
   
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
   
class Reviewer(Mentor):
  def __str__(self):
    res = f'Имя: {self.name}\nФамилия: {self.surname}'
    return res

 
  def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.grades = {}

  def __str__(self):
    res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._get_average_grade()}'
    return res

  def __lt__(self, other_lecturer):
    if not isinstance(other_lecturer, Lecturer):
      print('Ошибка')
      return
    else:
      compare = self._get_average_grade() < other_lecturer._get_average_grade
      if compare:
        print(f'у {self.name} {self.surname} оценка хуже чем, у {other_lecturer.name} {other_lecturer.surname}')
      else:
        print(f'у {self.name} {self.surname} оценка лучше чем, у {other_lecturer.name} {other_lecturer.surname}')

  def _get_average_grade(self):
    sum_ = 0
    count = 0
    for course in self.grades.values():
      sum_ += sum(course)
      count += len(course)
    return round(sum_ / count, 2)

def get_avg_lect_grade(lecturers, course):
  sum_ = 0
  for lecturer in lecturers:
    sum_ += sum(lecturer.grades[course]) / len(lecturer.grades[course])
  return sum_ / len(lecturers)
    
some_reviewer1 = Reviewer('Some', 'Name')
some_reviewer1.courses_attached += ['Python']
some_reviewer2 = Reviewer('Piter', 'Pen')
some_reviewer2.courses_attached += ['Git']
print(some_reviewer1)
print(some_reviewer2)

some_lecturer1 = Lecturer('Name', 'Surname')
some_lecturer1.courses_attached += ['Python']
some_lecturer2 = Lecturer('Mikky', 'Mouse')
some_lecturer2.courses_attached += ['Git']

some_student1 = Student('Ruoy', 'Eman', 'your_gender')
some_student1.courses_in_progress += ['Python']
some_student1.courses_in_progress += ['Git']
some_student1.finished_courses += ['Введение в программирование']
some_student1.rate_lecturer(some_lecturer1, 'Python', 4)
some_student1.rate_lecturer(some_lecturer2, 'Git', 5)

some_student2 = Student('Din', 'Winhester', 'your_gender')
some_student2.courses_in_progress += ['Python']
some_student2.courses_in_progress += ['Git']
some_student2.finished_courses += ['Введение в программирование']
some_student2.rate_lecturer(some_lecturer1, 'Python', 5)
some_student2.rate_lecturer(some_lecturer2, 'Git', 5)

print(some_lecturer1)
print(some_lecturer2)

some_reviewer1.rate_student(some_student1, 'Python', 4)
some_reviewer2.rate_student(some_student2, 'Git', 3)
some_reviewer1.rate_student(some_student1, 'Python', 5)
some_reviewer2.rate_student(some_student2, 'Git', 4)

print(some_student1)
print(some_student2)

print(get_avg_lect_grade([some_lecturer1], 'Python'))
print(get_avg_lect_grade([some_lecturer2], 'Git'))

