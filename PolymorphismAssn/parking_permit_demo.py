from permit.facultyParking import FacultyStaffParking
from permit.studentParking import StudentParking
from parking_permit import ParkingPermit

print("Calling issue_permit() function in the parent class")
parking = ParkingPermit(198010, "01-15-2021", 485)
parking.issue_permit()
print()
print("Calling issue_permit() function in the StudentParking class")
std_p = StudentParking(198010, "01-15-2021", 485, "permanent", "spring")
std_p.issue_permit()
print()
print("Calling issue_permit() function in the FacultyStaffParking class")
faculty_permit = FacultyStaffParking(1910, "01-15-2021", 205, "Full Time Faculty", 2021)
faculty_permit.issue_permit()
