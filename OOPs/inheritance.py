class Employee:
    raise_percent=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    
    def apply_raise(self):
         self.pay=int(self.pay*self.raise_percent)
    

class Developer(Employee):
    raise_percent=2
    
    #want to add a new parameter to inherited class and to keep all the old ones also
    def __init__(self, first, last, pay,lang):
        super().__init__(first, last, pay)
        self.lang=lang

dev_1=Developer("Yash","Verma",50000,"python")
dev_2=Employee("Yash2","Verma2",60000)
print(dev_1.pay)
print(dev_1.lang)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)