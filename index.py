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

