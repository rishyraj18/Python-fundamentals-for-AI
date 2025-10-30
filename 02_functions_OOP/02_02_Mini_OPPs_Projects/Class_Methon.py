class company:
    company_name = "TechCorp"

    def __init__(self, employee_name):
        self.emp_name = employee_name
    
    @classmethod
    def ch_company(cls, new_name):
        cls.company_name = new_name

    def show(self):
        print(f"Employee : {self.emp_name}, Company : {company.company_name}")

emp1 = company("Rishy Raj")
emp2 = company(" Rocky")

emp1.show()
emp2.show()

company.ch_company("RR")

emp1.show()
emp2.show()
