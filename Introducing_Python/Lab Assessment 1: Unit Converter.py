def convert_kg(value):
    #converts kg to lbs and ounces
    lbs = value*2.20462
    oz = value*35.274
    #displays kg into lbs and ounces
    print(str(value) + " kg converted is " + str(lbs) + " pounds and " + str(oz) + " ounces.")

def convert_pounds(value):
    #converts bs to kg and ounces
    kg = value*0.453592
    oz = value*16
    #displays kg into lbs and ounces
    print(str(value) + " pounds converted is " + str(kg) + " kg and " + str(oz) + " ounces.")

def convert_ounces(value):
    #converts ounces to kg and pounds
    kg = value*0.0283
    lbs = value*0.0625
    #displays ounces into lbs an kg
    print(str(value) + " ounces converted is " + str(kg) + " kg and " + str(lbs) + " pounds.")