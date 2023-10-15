# Declare the Rectangle class to calculate the area
class Rectangle:
    def __init__(self, vertical, horizontal):
        self.vertical = vertical
        self.horizontal = horizontal
        
    # Calculate the area of the rectangle
    def calc_area(self):
        area = self.vertical * self.horizontal
        return area

# Declare the Rectangular class to calculate the area
class Rectangular(Rectangle):
    def __init__(self, vertical, horizontal, height):
        super().__init__(vertical, horizontal)
        self.height = height
        
    # Calculate the volume of the rectangular solid
    def calc_volume(self):
        area = super().calc_area()
        volume = area * self.height
        return volume


# Create three instances of Rectangular with specified dimensions
def create_instances():
    squares = []
    squares.append(Rectangular(3, 4, 5))
    squares.append(Rectangular(50, 60, 70))
    squares.append(Rectangular(333, 444, 555))
    return squares


# Calculate and print the area and volume for each instance
def play():
    instances = create_instances()
    for instance in instances:
        area = instance.calc_area()
        volume = instance.calc_volume()
        print(f"Area is {area}")
        print(f"Volume is {volume}")

play()
