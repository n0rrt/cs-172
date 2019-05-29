#Tim Harris tlh339 - Main script
from Node import Node
from LinkedList import LinkedList
from Employee import Employee
employeeList = LinkedList()

#custom error handler
class invalidError(Exception):
    pass
#creates new employee
def makeNewEmp(idNum, rate):
    newEmp = Employee(idNum, rate)
    employeeList.append(newEmp)
    validate()
#validates that all values are acceptable
def validate():
    index = 1
    for x in range(len(employeeList)):
        for y in range(index, len(employeeList) - x): #goes through each employee object following the current and compares ids
            if (employeeList[x].getId() == employeeList[y].getId()):
                raise invalidError
            index += 1
        if int(employeeList[x].getRate()) < 6: #validates rate
            raise invalidError
        if int(employeeList[x].getHours()) < 0: #validates hours
            raise invalidError
        
'''
a. new employee
b. set hours
c. display payroll
d. update rate
e. remove employee
f. quit
'''
if __name__ == "__main__":
    options = 'abcdef'
    options_string = "a. new employee\nb. set hours\nc. display payroll\nd. update rate\ne. remove employee\nf. quit\n"
    userIn = input(options_string)
    if userIn.lower() not in options:
        print('invalid option')
        userIn = input(options_string)
    while userIn.lower() != 'f':
        if userIn.lower() == 'a':
            print('add employee')
            try:
                idNum = input('Enter ID num: ')
                rate = input("Enter hourly rate: ")
                makeNewEmp(idNum, rate)
            except(invalidError, ValueError):
                print("Id number already assigned to employee")
        elif userIn.lower() == 'b':
            print("set hours")
            for emp in range(len(employeeList)):
                try:
                    newHours = int(input("Enter hours for {}: ".format(employeeList[emp].getId())))
                    employeeList[emp].setHours(newHours)
                    employeeList[emp].setWage(int(employeeList[emp].getHours()) * int(employeeList[emp].getRate()))
                    validate()
                except(invalidError, ValueError):
                    print("invalid input")
        elif userIn.lower() == 'c':
            print('display payroll')
            print(str(employeeList[0]).split())
            for emp in range(len(employeeList)):
                print("ID: {}\nHours: {}\nRate: ${:.2f}\nWages: ${:.2f}\n".format(employeeList[emp].getId(), employeeList[emp].getHours(), int(employeeList[emp].getRate()), employeeList[emp].getWage()))
        elif userIn.lower() == 'd':
            print('change rate')
            newid = input('Enter the id: ')
            found = False
            for emp in range(len(employeeList)):
                if employeeList[emp].getId() == str(newid):
                    try:
                        newrate = input("Enter the new rate: $")
                        employeeList[emp].setRate(newrate)
                        validate()
                    except(invalidError, ValueError):
                        print('invalid input')
                    found = True
                    break
            if not found:
                print('ID not found')
        elif userIn.lower() == 'e':
            print('remove employee')
            newid = input('Enter the id: ')
            found = False
            for emp in range(len(employeeList)):
                if employeeList[emp].getId() == str(newid):
                    employeeList.remove(employeeList[emp])
                    found = True
                    break
            if not found:
                print('ID not found')
        userIn = input(options_string)
        if userIn.lower() not in options:
            print('invalid option')
            userIn = input(options_string)



