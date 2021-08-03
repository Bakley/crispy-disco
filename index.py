class Grade: 
  def __init__(self, start, to, gradeName): 
    self.start = start 
    self.to = to 
    self.gradeName = gradeName

  def grading(self, marks):
    if marks >= self.start and marks <= self.to:
      return self.gradeName
  
  def binaryGrading(self, marks):
    return

class Student: 
  def __init__(self, name, marks): 
    self.name = name 
    self.marks = marks

  def super_students(grades, students):
    res = []
    for student in students:   #n
      for grade in grades:   #m
        if grade.grading(student.marks) == 'A' or grade.grading(student.marks) == 'B':
          res.append(student.name)
    print(res)
    return res

  def binarySearch(grade, students):
    n = len(students)
    mid = (0 + n-1) // 2
    res = []
    for i in range(mid, n):
      if students[i].marks >= grade:
        res.append(students[i].name)
    return res
