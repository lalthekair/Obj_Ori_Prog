from Employees.employee import Employee


class SalariedEmployee(Employee):
    def __init__(self,n, id, mnthly_pay):
        super().__init__(n, id)
        self.monthly_pay = mnthly_pay

    def get_monthly_pay(self):
        return self.monthly_pay
