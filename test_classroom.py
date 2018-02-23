'''
module for testing class classroom and all it's methods
'''
from classroom import *

classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
print(classroom_007)
print(classroom_016)
print("IsLarger: ", classroom_016.is_larger(classroom_007))
print("Differences: " ,classroom_016.equipment_differences(classroom_007))