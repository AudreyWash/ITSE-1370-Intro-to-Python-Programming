import math


# Write your Wheel class here
class Wheel:
    def __init__(self, radius):
        self.radius = radius


    def wheel_area(self):
        return math.pi * self.radius ** 2


    def wheel_perimeter(self):
        return 2 * math.pi * self.radius


    def swap_radius(self, new_radius):
        self.radius = new_radius




# Use this to test your code
if __name__ == "__main__":
    wheel = Wheel(7)  # Initial radius of 7
    morewheels = True
    while morewheels:
        radius = float(input("Radius of wheel: "))
        wheel.swap_radius(radius)
        print("Surface area of wheel:", wheel.wheel_area())
        print("Perimeter of wheel:", wheel.wheel_perimeter())
        yn = input('More wheels? Y/N ')
        morewheels = yn.lower() == 'y'