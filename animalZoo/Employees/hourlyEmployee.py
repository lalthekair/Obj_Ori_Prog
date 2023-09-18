from Employees.employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, n, id, hr_week, pay_hr):
        super().__init__(n, id)
        self.hours_per_week = hr_week
        self.pay_per_hour = pay_hr

    def get_monthly_pay(self):
        return self.hours_per_week * self.pay_per_hour * 4

