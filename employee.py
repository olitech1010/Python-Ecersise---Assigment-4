class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
        
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    def getSalary(self):
        return self.__salary
    
    def setName(self, name):
        self.__name = name
    
    def setSalary(self, salary):
        self.__salary = salary
    
    
        