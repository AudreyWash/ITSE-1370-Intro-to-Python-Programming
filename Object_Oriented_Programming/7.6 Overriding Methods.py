class Bird:
  # init method to initialize all values
  def __init__(self,wingspan,lifespan,speed):
    self.wingspan = wingspan # wingspan value initialized
    self.lifespan_in_years = lifespan # lifespan_in_years value initialized
    self.speed_in_mph = speed # speed_in_mph value initialized


  # str method defined
  def __str__(self):
    # string returned
    return f"The {type(self).__name__.lower()} "\
    f"has a wingspan up to {self.wingspan}ft,"\
    f" has a lifespan of {self.lifespan_in_years} years and "\
    f"can fly at a maximum speed of {self.speed_in_mph}mph."


# class eagle that inherits bird class
class Eagle(Bird):
  # init method overrided of Bird class
  def __init__(self,wingspan,lifespan,speed,clutch=3):
    self.wingspan = wingspan # wingspan value initialized
    self.lifespan_in_years = lifespan # lifespan_in_years value initialized
    self.speed_in_mph = speed # speed_in_mph value initialized
    self.clutch = clutch # clutch value initialized


  # str method overrided
  def __str__(self):
    # custom string returned
    return f"The {type(self).__name__.lower()} "\
    f"has a wingspan up to {self.wingspan}ft,"\
    f" has a lifespan of {self.lifespan_in_years} years and "\
    f"can fly at a maximum speed of {self.speed_in_mph}mph. "\
    f"It also has a clutch size up to {self.clutch}."


# main class
if __name__ == '__main__':
  # object of eagle class with values to constructor
  eagle = Eagle(7.5,20,99)
  # print eagle object which prints the built in __str__ method
  print(eagle)