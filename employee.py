global id_counter
id_counter = 0
class Employee:
    _id: int 
    name:str
    def __init__(self, name, _id: int):
        self._id = _id
        self.name  = name

    def print_emp(self):
        print("name"  , self.name)
        return True

class Register:

    register:[Employee]
    def __init__(self):
        self.register = []

    def addEmployee(self, e:Employee)->bool:
        self.register.append(e)
        return True

    def deleteEmployee(self, _id: int)->bool:
        for i in range(len(self.register)):
            if self.register[i]._id == _id:
                #print("deleting ", el.print_emp())
                self.register[i] = None
                return True

    def updateEmployee(self, e: Employee):
        for el in self.register:
            if el._id == _id:
                el = e
                return True


    def getEmployee(self, _id:int)->Employee:
        for el in self.register:
            if el._id == _id:
                return el


    def getAllEmployees(self)->[Employee]:
        return self.register



register = Register()
emp1 = Employee("a", id_counter)
id_counter+=1
register.addEmployee(emp1)
emp2 = Employee("b" , id_counter)
id_counter+=1
register.addEmployee(emp2)
for el in register.getAllEmployees():
    print(el._id, " ", el.name)

emp3 = Employee("c" , id_counter)
id_counter+=1

register.addEmployee(emp3)
register.deleteEmployee(0)

for el in register.getAllEmployees():
    if el==None:
        continue
    print(el._id, " ", el.name)

print(register.getAllEmployees())

