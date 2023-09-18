class Employee:
    def __init__(self, n, id):
        self.name = n
        self.ID = id

    def get_name(self):
        return self.name

    def get_ID(self):
        return self.ID

    def set_name(self,new_name):
        if isinstance(new_name,str):
            self.name = new_name

        else:
            print("Cannot update the name")

    def get_monthly_pay(self):
        return 100.00

    def get_annual_pay(self):
        return 1200.00
