#class  template or blueprint
#objects or instances - copies created based off of class definition


'''
student1 = Student()
student2 = Student()

print(student1)
print(student2)

#Instance variables contain data that are unique to each instance or object
student1.first = 'Jane'
student1.last = 'Doe'
student1.email = 'janedoe@gmail.com'
student1.score = 85

student2.first = 'John'
student2.last = 'Doe'
student2.email ='johndoe@gmail.com'
student2.score = 93

print(student1.email)
print(student2.email)
'''
#Don't assign manually, assign when created
class  Student():
    def __init__(self, first, last, score):
        #self refers to the instance/object being created
        self.first = first
        self.last = last
        self.email = f'{first}{last}@gmail.com'
        self.score = score

    def getfullname(self):
        return f'{self.first} {self.last}'

student1 = Student('Jane', 'Doe', 85)
student2 = Student('John', 'Doe', 93)
print(student1.email)
print(student2.email)
print(student2.getfullname())
#getfullname is a METHOD, a function defined in a class that is passed on to instances.