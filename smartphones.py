
smartphones = []
# Phone class to blueprint instances
class Phone:
    # Constructor function which contain all the instances attributes with self indicator
    def __init__(self, type, size, color):
        self.type = type
        self.size = size
        self.color = color
    # Instance(Phones) display function by accessing constructor and prints its attributes
    def info(self):
        print('Type: ' + self.type + ' Size: ' + str(self.size) + ' Color: ' + self.color)
# Instance creator and assign them into global variable smartphone
def create_phone():
    global smartphones
    Phone1 = Phone('Android', 60, 'red')
    Phone2 = Phone('iPhone', 50, 'Blue')
    Phone3 = Phone('Android', 70, 'White')
    Phone4 = Phone('Android', 50, 'Black')
    Phone5 = Phone('Android', 60, 'Purple')
    Phone6 = Phone('iPhone', 60, 'Black')
    Phone7 = Phone('Android', 50, 'Green')
    Phone8 = Phone('iPhone', 70, 'Yellow')
    Phone9 = Phone('iPhone', 80, 'Purple')
    Phone10 = Phone('Android', 60, 'Yellow')
    smartphones = [Phone1, Phone2, Phone3, Phone4, Phone5, Phone6, Phone7, Phone8, Phone9, Phone10]
# All instamce displayer by looping through smartphones array
def show_smart_phones():
    for phone in smartphones:
        phone.info()
# Main function of the program to connect methods and Phone class
def play():
    create_phone()
    show_smart_phones()

play() # program initializer