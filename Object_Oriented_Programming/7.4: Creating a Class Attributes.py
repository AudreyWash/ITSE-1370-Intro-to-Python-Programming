# Write your Package class here
class Package:
    # Class attribute for maximum item capacity
    max_capacity = 6


    def __init__(self, items):
        if items > Package.max_capacity:
            excess_items = items - Package.max_capacity
            self.items = Package.max_capacity
            print(f"Limit exceeded by {excess_items} items. Initializing package with {self.items} items.")
        else:
            self.items = items
            print(f"Package initialized with {self.items} items.")


# This is to test your code
if __name__ == '__main__':
    morepackages = True
    while morepackages:
        items = int(input("How many items are in the package?: "))
        package = Package(items)
        yn = input('Ship more packages? Y/N ')
        morepackages = yn == 'y' or yn == 'Y'