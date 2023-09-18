from parking_permit import ParkingPermit


class StudentParking(ParkingPermit):

    def __init__(self, id, issueDate, cost, type, semester):
        super().__init__(id, issueDate, cost)
        self.__type = type
        self.__semester = semester

    def get_type(self):
        return self.__type

    def get_semester(self):
        return self.__semester

    def set_type(self, new_type):
        self.__type = new_type

    def set_semester(self, new_semester):
        self.__semester = new_semester

    def issue_permit(self):
        print("Show this permit to the security guard in the parking lot!")
        print("This permit is:", self.__type, "\nIssued for:", self.__semester, "student to whose information is"
                                                                                "shown below.")
        print("ID:", self.get_id(), "\nIssue Date:", self.get_issueDate())