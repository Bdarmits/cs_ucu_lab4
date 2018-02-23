class Classroom:
    #Class for classroom with room number capacity and list of equipment

    def __init__(self, number, capacity, equipment):
        #Initialises variables
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def is_larger(self, classroom2):
        #Checks if capacity of one room is bigger that the other's
        return True if self.capacity > classroom2.capacity else False

    def equipment_differences(self, classroom2):
        #Returns difference in equipment between 2 classrooms
        difference = []
        for i in self.equipment:
            if i not in classroom2.equipment:
                difference.append(i)
        return difference

    def __repr__(self):
        #Returns object in method's __repr__ format
        return 'Classroom(\'{0}\', {1}, {2}' \
               ')'.format(self.number, self.capacity, self.equipment)

    def __str__(self):
        #Is being used when object of a class is printed
        return 'Classroom {0} has a capacity of {1} persons and has the ' \
               'following equipment: {2}.'.format(self.number, self.capacity,
                                                  ', '.join(self.equipment))



