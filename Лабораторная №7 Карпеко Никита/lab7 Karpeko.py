class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        return f"имя: {self.name}, id: {self.id}"
    
class Manager(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department
    def manage_project():
        print("I'm manager, I manage")
class Technician(Employee):
    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization
    def perform_maintenance():
        print("I'm techic, I perform")
        
class TechManager(Manager, Technician):
    lst_of_emp = []
    def __init__(self, name, id, department, specialization):
        super().__init__(name, id, department, specialization)
    def manage_project():
        print("I'm TechManager, I can manage")
    def perform_maintenance():
        print("I'm TechManager, I can perform")
    def add_employee(Emp):
        lst_of_emp.append(Emp)
    def get_team_info():
        for i in lst_of_emp:
            print(i.get_info())

emp1 = Employee("David", "00001")
emp2 = Employee("Eoan", "00002")
emp3 = Employee("Frank", "00003")

manager1 = Manager("Vadim", "00004", "sellings")
technic1 = Technician("Ivan", "00005", "big_data")

tech_manager = TechManager("Alex", "00006", "production", "science")




















        
            
