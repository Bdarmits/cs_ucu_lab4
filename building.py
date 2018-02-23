from classroom import Classroom

class AcademicBuilding():
    #Class for Academic building with address and rooms

    def __init__(self, address, classrooms):
        #Initialises variables
        self.address = address
        self.classrooms = classrooms

    def total_equipment(self):
        #Adds equipment from all classrooms to 1 list and returns it
        total_equipment_count = []
        all_equipment_dict = {}
        for room in self.classrooms:
            for element in room.equipment:
                if element not in all_equipment_dict:
                    all_equipment_dict[element] = 1
                else:
                    all_equipment_dict[element] += 1
        for i in all_equipment_dict:
            total_equipment_count.append((i, all_equipment_dict[i]))
        return total_equipment_count

    def __str__(self):
        #Prints address and info abtotal_equipment_count classrooms
        print(self.address)
        for room in self.classrooms:
            print(room)
        return ''



