class ParkingPermit:

    def __init__(self, id, issueDate, cost):
        self.__id = id
        self.__issueDate = issueDate
        self.__cost = cost

    def get_id(self):
        return self.__id

    def get_issueDate(self):
        return self.__issueDate

    def get_cost(self):
        return self.__cost

    def set_id(self, new_id):
        self.__id = new_id

    def set_issueDate(self, new_issue_date):
        self.__issueDate = new_issue_date

    def set_cost(self, new_cost):
        self.__cost = new_cost

    def issue_permit(self):
        print("Show this permit to the security guard in the parking lot!")
        print("ID:", int(self.__id), "\nIssue Date:", self.__issueDate)
