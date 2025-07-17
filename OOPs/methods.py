#Instance variables
#Class variables


class Employee:

    #Class variable but can be used in an instance as well as if we access it from instance since it is not there it will
    #look for class variable
    #Class methods are used to alter class variables and alternative constructors
    raise_amount=1.04
    no_of_emps=0

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"@company.com"
        Employee.no_of_emps+=1
    
    def fullname(self):
        return ("{} {}".format(self.first,self.last))

    def raisePay(self):
        self.pay=int(self.pay*self.raise_amount)
        return self.pay

    @classmethod
    def raise_amt(cls,amount):
        cls.raise_amount=amount
    
    @staticmethod
    def calc(date):
        return date
    

emp_1=Employee("Yash","Verma",40000)
emp_2=Employee("Test","User",80000)
 
# print(emp_1.fullname())
# print(emp_1.email)
# print(Employee.fullname(emp_2))
# print(emp_1.raisePay())
# print(Employee.no_of_emps)
# print(Employee.__dict__)
# print(emp_1.__dict__)

emp_1.raise_amt(1.05)


print(Employee.raise_amount)
print(Employee.calc("SSS"))
