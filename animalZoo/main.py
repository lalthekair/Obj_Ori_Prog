from Zoo.herbivore import Herbivore
from Zoo.carnivore import Carnivore
from Employees.hourlyEmployee import HourlyEmployee
from Employees.SalariedEmployee import SalariedEmployee


def main():
    hourly_emp = HourlyEmployee("Nader", 10, 12, 10)
    salaried_emp = SalariedEmployee("Salem", 12, 4000)
    carnivore = Carnivore(2018, 2019)
    herbivore = Herbivore(2018,2019)
    print(hourly_emp.get_monthly_pay())
    print(salaried_emp.get_monthly_pay())
    carnivore.eat()
    herbivore.eat()
    print(carnivore.get_year_born())
    print(carnivore.get_year_brought_to_zoo())
    print("age is" , carnivore.calculate_age_when_brought_to_zoo())








main()