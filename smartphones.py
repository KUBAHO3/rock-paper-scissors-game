
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
# Instance creator by appending new data to an existing smartphones array
def create_phone():
    global smartphones
    smartphones.append(Phone('Android', 60, 'red'))
    smartphones.append(Phone('iPhone', 50, 'Blue'))
    smartphones.append(Phone('Android', 70, 'White'))
    smartphones.append(Phone('Android', 50, 'Black'))
    smartphones.append(Phone('Android', 60, 'Purple'))
    smartphones.append(Phone('iPhone', 60, 'Black'))
    smartphones.append(Phone('Android', 50, 'Green'))
    smartphones.append(Phone('iPhone', 70, 'Yellow'))
    smartphones.append(Phone('iPhone', 80, 'Purple'))
    smartphones.append(Phone('Android', 60, 'Yellow'))

# All instamce displayer by looping through smartphones array
def show_smart_phones():
    for phone in smartphones:
        phone.info()
# Main function of the program to connect methods and Phone class
def play():
    create_phone()
    show_smart_phones()

play() # program initializer