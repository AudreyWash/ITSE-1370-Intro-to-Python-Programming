# Class definition goes here
class TabletComputer:
    def __init__(self, screen_size, storage, os):
        self.screen_size = screen_size
        self.storage = storage
        self.os = os




uPad = TabletComputer(12.9, "1TB", "uPadOS 13.5.1")
rootProX = TabletComputer(13.0, "512GB", "Glass 10 Home")


print(f"The new uPad has a {uPad.screen_size}"
  f" inch display. A maximum {uPad.storage} of storage and runs on"
    f" the latest version of {uPad.os}. Its biggest competitor is"
    f" the Root Pro X which holds a similar {rootProX.screen_size}"
    f" inch display, with a maximum storage capacity of {rootProX.storage} and runs {rootProX.os}."
      )
