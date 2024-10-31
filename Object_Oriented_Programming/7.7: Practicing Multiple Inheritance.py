class TabletCamera:
    def __init__(self, pixel):
        self.pixel = pixel


    # get_pixel() function to return pixel
    def get_pixel(self):
        return self.pixel




class Facial_recognition:


    # scan_face method
    def scan_face(self):
        print("Scanning Face...")




# BIoTablet class derived from TabletCamera and Facial_recognition classes
class BioTablet(TabletCamera, Facial_recognition):
    # constructor initializing base class constructor
    def __init__(self, pixel):
        # passing value into base class constructor
        TabletCamera.__init__(self, pixel)




# main method
def main():
    # create an instance of BioTablet class
    obj = BioTablet("12MP")


    # calling scan_face method
    obj.scan_face()


    # printing pixel
    print(obj.get_pixel())




# calling main()
main()
