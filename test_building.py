'''
module for testing class building and all it's methods
'''
from building import *

classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
classroom_008 = Classroom('008', 25, ['PC', 'projector'])
classrooms = [classroom_016, classroom_007, classroom_008]
building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
print("Result of print(building.address): ", building.address)
print("\nResult of cycle for print(room): ")
for room in building.classrooms:
    print(room)
print("\nResult of print(building): ")
print(building)
print("Total equipment: ")
print(building.total_equipment())