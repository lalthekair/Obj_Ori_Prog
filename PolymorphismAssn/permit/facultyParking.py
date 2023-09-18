from parking_permit import ParkingPermit


class FacultyStaffParking(ParkingPermit):

    def __init__(self, id, issueDate, cost, group, year):
        super().__init__(id, issueDate, cost)
        self.__group = group
        self.__year = year

    def get_group(self):
        return self.__group

    def get_year(self):
        return self.__year

    def set_group(self, new_group):
        self.__group = new_group

    def set_year(self, new_year):
        self.__year = new_year

    def issue_permit(self):
        print("Show this permit to the security guard in the parking lot!")
        print("This permit is issued for a:", self.__group, "in", int(self.__year))
        print("ID:", self.get_id())