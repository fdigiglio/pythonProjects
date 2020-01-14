class Quadrilaterral():

    def __init__(self, sides):
        self.sides = 4

    def display(self):
        print(self.sides)


class Parallelogram(Quadrilaterral):
    def __init__(self, sides, parallel_lines, congruent_angles, congruent_sides):
        super().__init__(sides)
        self.parallel_lines = parallel_lines
        self.congruent_angles = congruent_angles
        self.congruent_sides = congruent_sides

    def display(self):
        print(self.sides)
        print(self.parallel_lines)
        print(self.congruent_angles)
        print(self.congruent_sides)

    
        



class Polygon(Quadrilaterral):
    def __init__(self, sides, parallel_lines, congruent_angles, congruent_sides):
        super().__init__()





z = Parallelogram(4, 2, 4, 3)
print("This Parallelogram has", z.parallel_lines, "parallel lines,", z.congruent_angles, "congruent angles,", z.congruent_sides, "congruent sides.")
print(z.parallel_lines)
z.display()

#write if and else statement checking if it has the specific needed amount of properties in order to be a parallelogram or just a polygon that is also a quadrilaterall        