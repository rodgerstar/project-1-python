class Cylinder:
    def __init__(self,radius,height, color):
        self.radius = radius
        self.height = height
        self.color = color

    def calc_area(self, is_closed = True):
        if is_closed :
            area = 2 * 22/7 * self.radius ** 2 + 2 * 22/7 * self.radius * self.height
            print(f"Area of closed cylinder is: {area}")
        else:
            area = 22/7 * self.radius ** 2 + 2 * 22/7 * self.radius * self.height
            print(f"Area of open cylinder is: {area}")

    def calc_volume(self):
        volume = 22/7 * self.radius ** 2 * self.height
        print(f"volume of cylinder is: {volume}")

c1 = Cylinder(radius=7, height=5, color='blue')
c2 = Cylinder(radius=14, height=5, color='red')
c1.calc_volume()
c1.calc_area(is_closed=False)