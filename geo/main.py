class Quadrilaterral():

    def __init__(self, sides):
        self.sides = sides

    def display(self):
        print(self.sides)


class Parallelogram(Quadrilaterral):
    def __init__(self, sides, parallel_lines, congruent_angles, congruent_sides):
        super().__init__(sides)
        self.parallel_lines = parallel_lines
        self.congruent_angles = congruent_angles
        self.congruent_sides = congruent_sides

    def display(self):
        print(self.sides, "Sides")
        print(self.parallel_lines, "Parallel lines")
        print(self.congruent_angles, "Congruent angles")
        print(self.congruent_sides, "Congruent sides")

    def checkShape(self):
        if self.sides == 4:
            print("This is a QUADRILATERAL!")
        elif self.sides < 4 or self.sides > 4:
            print("This is not a quadrilateral but IS a POLYGON")
        if self.sides == 4 and self.parallel_lines == 4:
            print("PARALLELOGRAM!")
        if self.sides == 4 and self.parallel_lines == 4 and self.congruent_angles == 4:
            print("RECTANGLE!")
        if self.sides == 4 and self.parallel_lines == 4 and self.congruent_sides == 4:
            print("RHOMBUS")
        if self.sides == 4 and self.parallel_lines == 4 and self.congruent_angles == 4 and self.congruent_sides == 4:
            print("SQUARE!")
        

class Polygon(Quadrilaterral):
    def __init__(self, sides, parallel_lines, congruent_angles, congruent_sides):
        super().__init__(sides)
        self.parallel_lines = parallel_lines
        self.congruent_angles = congruent_angles
        self.congruent_sides = congruent_sides
    def checkShape(self):
        if self.sides == 4:
            print("This is a QUADRILATERAL!")
        elif self.sides < 4 or self.sides > 4:
            print("This is not a quadrilateral but IS a POLYGON")
        if self.sides == 4 and self.parallel_lines == 2:
            print("Trapezoid")
        if self.sides == 4 and self.parallel_lines == 2 and self.congruent_sides == 2:
            print("Isosceles Trapezoid!")
        if self.sides == 4 and self.parallel_lines == 0 and self.congruent_sides == 4:
            print("KITE!")


rectangle = Parallelogram(4, 4, 4, 0)
rectangle.checkShape()

print("======================================================")

rhombus = Parallelogram(4, 4, 0, 4)
rhombus.checkShape()

print("======================================================")

square = Parallelogram(4,4,4,4)
square.checkShape()

print("======================================================")

trapezoid = Polygon(4, 2, 0, 0)
trapezoid.checkShape()

print("======================================================")

isoTrap = Polygon(4, 2, 0, 2)
isoTrap.checkShape()

print("======================================================")

kite = Polygon(4, 0, 0, 4)
kite.checkShape()