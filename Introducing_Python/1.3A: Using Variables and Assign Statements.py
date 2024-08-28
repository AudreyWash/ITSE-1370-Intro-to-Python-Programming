import sys 

distance_miles = 60
time_hours = 3
distance_feet = distance_miles * 5280
time_seconds = time_hours * 3600
speed_mph = distance_miles / time_hours
speed_knots = speed_mph / 1.15078
speed_feetps = distance_feet / time_seconds

print("The speed in knots is: " + str(speed_knots))
print("The speed in miles per hour is: " + str(speed_mph))
print("The speed in feet per second is: " + str(speed_feetps))