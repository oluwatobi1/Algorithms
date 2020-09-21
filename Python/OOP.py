class Student:
    '''
    The student object contains a lot of students

    Args:
        age(int): Age of student
        weight(float): Weight of student
        height (float): Height of student
        
    Attributes:
        BMI(float): This is a Body Max Index(BMI)(rounded to 2dp) of the student,
    '''
    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height
        self.BMI = None
        
    def info(self):
        '''Returns a tuple containing the age and Body Max Index(BMI)'''
        self.BMI = round(self.weight/(self.height**2), 2)
        return (self.age, self.BMI)
    
    
    
def average(stude):
    '''
    Returns the average age,weight and height of the students in the next 10 years
    
    
     Args:
        stude(list): Contains different instances of the student class
        
    Attributes:
        age_10 (list): Computes the age after 10 years
        weight_10 (list): Computes the weight after 10 years using the (compound interest) formula(x*(1+rate(%))**10)
        height_10 (list): Computes the weight after 10 years using the (compound interest) formula(x*(1+rate(%))**10)
        div(int): Stores the lenght of the input student list
    '''
    
    
    age_10 = []
    weight_10 = []
    height_10 = []
    div = len(stude)
    stude.age
    for each in stude:
        age_10.append(each.age)
        weight_10.append(each.weight*1.05**10)
        height_10.append(each.height*1.02**10)
    
    age_10 = sum(age_10)/div+10
    weight_10 = round(sum(weight_10)/div, 2)
    height_10 = round(sum(height_10)/div, 2)          
        
    return (age_10, weight_10, height_10)



Fortune=Student(23,45.67,7.6)
print(Fortune.info())
Joba=Student(22,40.01,8.3)
print(average([Fortune,Joba]))




"""
OOPs

Contrary to what the title implies, this task was not a mistake.
OOP==Object Oriented Programming
Create a class Student.
Every student has an age, weight and height
Create a constructor that takes in 3 parameters, a students age,weight and height(in that order)
and initializes them to those values
Create a function info() which when called by a student object RETURNS a tuple containing the age and Body Max Index(BMI)(rounded to 2dp) of the student
BMI=weight/(height**2)
The function info() will not take any parameters
Lastly create a function average() which takes a list of student objects and RETURNS a tuple containing the average age,weight and height(in that order) of the students in the next 10 years
i.e 10 years from now what would be their average age,weight and height(in that order)
Assume that weight increases by 5% each year and height increases by 2% each year.
NOTE:

•Age is an integer, weight and height are floats

•Ensure functions take parameters in the order given.

•Your float answers should be rounded to 2 dp

•Only assertion errors should be raised if necessary
Fortune=Student(23,45.67,7.6)
represents a student whose age is 23, weight is 45.67 and height is 7.6
Fortune.info() would return (23,0.79)
another student
Joba=Student(22,40.01,8.3)
average([Fortune,Joba]) would return (32.5,69.78,9.69)
e.g for weight in 10 years Joba will weigh 65.17 while Fortune will weigh 74.39 and the average of that is 69.78
Goodluck. Sorry for the long epistle.
"""



