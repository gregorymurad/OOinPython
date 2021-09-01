print("Hello COP 4813")

class COP4813Student():
    minimum_grade = 93
    def __init__(self,first_name,last_name,pid,email,grade):
        self.first_name = first_name
        self.last_name = last_name
        self.pid = pid
        self.email = email
        self.grade = grade

    def current_grade(self):
        return "{0} {1}\'s current grade is {2}".format(self.first_name,
                                                       self.last_name,
                                                       self.grade)

    def grade_message(self):
        if self.minimum_grade < self.grade:
            return "{0} {1} will likely get " \
                   "an A in this course".format(self.first_name,
                                                self.last_name)
        else:
            return "{0} {1} will probably not get " \
                   "an A in this course".format(self.first_name,
                                                self.last_name)

alec = COP4813Student("Alec","Ramos",123456,"alec@fiu.edu",98)
andrius = COP4813Student("Andrius","Bubelis",12002,"andy@fiu.edu",92)

print(alec)
print(andrius.email)
print(alec.grade)
print(andrius.current_grade())
print(alec.current_grade())

print(COP4813Student.minimum_grade)
print(alec.minimum_grade,andrius.minimum_grade)

COP4813Student.minimum_grade = 94
print(alec.minimum_grade,andrius.minimum_grade)

print(alec.grade_message())
print(andrius.grade_message())

andrius.minimum_grade = 95
print(COP4813Student.minimum_grade)
print(alec.minimum_grade)
print(andrius.minimum_grade)