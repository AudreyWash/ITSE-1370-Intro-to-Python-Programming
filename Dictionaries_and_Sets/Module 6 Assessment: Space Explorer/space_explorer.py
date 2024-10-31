from random import seed, sample, choice
from os import linesep
from string import punctuation
from math import sqrt
from itertools import product




SEED_NUMBER = 1024
seed(SEED_NUMBER)
MAP_SIZE = 100
all_possible_symbols = frozenset(punctuation+'GSFT ')




def define_possible_objects(choices=punctuation):
   chars = choices
   chars += 'G'
   chars += 'T'*3
   chars += 'F'*3
   return chars


def generate_object(itera, available_coordinates, occupied_coordinates):
   symbol = sample(itera, 1)
   coordinates = choice(available_coordinates)
   available_coordinates.remove(coordinates)
   occupied_coordinates.append(coordinates)
   return symbol, coordinates


def set_up():
   symbols1 = define_possible_objects(punctuation)
   symbols2 = define_possible_objects('^&*'*5)
   return symbols1, symbols2


def generate_available_coordinates(map_size):
   map = []
   print(map_size)
   for x in range(map_size) :
       for y in range(map_size) :
           coord = (x, y)
           map.append(coord)
   return map


def generate_empty_map(available_coordinates):
   map = {}
   for coord in available_coordinates :
       if coord != (0,0) :
           map[coord] = " "
       else :
           map[coord] = "S"
   return map




def get_unique_objects(galaxy_map):
   unique = set()
   for item in galaxy_map.values() :
       if item not in unique :
           unique.add(item)
   return frozenset(unique)


def symbols_not_used_in_galaxy(symbols_in_galaxy):
   return all_possible_symbols.difference(symbols_in_galaxy)


def common_objects_encountered(galaxy_1_objects, galaxy_2_objects):
   return galaxy_1_objects.intersection(galaxy_2_objects)


def objects_encountered_in_galaxy1_not_galaxy2(galaxy_1_objects, galaxy_2_objects):
   return galaxy_1_objects.difference(galaxy_2_objects)




def objects_encountered_in_galaxy2_not_galaxy1(galaxy_1_objects, galaxy_2_objects):
   return galaxy_2_objects.difference(galaxy_1_objects)




def objects_encountered_in_both_galaxys(galaxy1_objects, galaxy2_objects):
   return galaxy1_objects.union(galaxy2_objects)


def calculate_path_to_goal(sorted_object_list):
   path = []
   for x in sorted_object_list :
       if x[2][0] in 'FT' :
           path.append(x)
       elif x[2][0] in 'G' :
           path.append(x)
           break
   return path


def display_galaxy(galaxy_map):
   map = ''
   for x in range(MAP_SIZE) :
       for y in range(MAP_SIZE) :
           map += galaxy_map[(x, y)]
       map += linesep
   return map


def calculate_euclidean_distance(coordinates):
   x, y = coordinates
   return (int)(sqrt(x**2 + y**2))


def populate_galaxy_map(available_symbols, available_coordinates, occupied_coordinates, galaxy_map):
   objects_encountered_list = list()
   while True:
       symbol, coordinates = generate_object(available_symbols, available_coordinates, occupied_coordinates)
       distance = calculate_euclidean_distance(coordinates)
       object_encountered = distance, coordinates, symbol
       objects_encountered_list.append(object_encountered)
       galaxy_map[coordinates] = symbol[0]
       if symbol[0] == 'G':
           break
   return sorted(objects_encountered_list)


def run_exploration():
   available_symbols1, available_symbols2 = set_up()




   available_coordinates1 = generate_available_coordinates(MAP_SIZE)
   available_coordinates2 = generate_available_coordinates(MAP_SIZE)
   occupied_coordinates1 = list()
   occupied_coordinates2 = list()




   galaxy_map_1 = generate_empty_map(available_coordinates1)
   galaxy_map_2 = generate_empty_map(available_coordinates2)




   explorer1_list = populate_galaxy_map(available_symbols1, available_coordinates1, occupied_coordinates1, galaxy_map_1)
   explorer2_list = populate_galaxy_map(available_symbols2, available_coordinates2, occupied_coordinates2, galaxy_map_2)




   print(explorer1_list)
   print(explorer2_list)




   path_list1 = calculate_path_to_goal(explorer1_list)
   print(path_list1)




   path_list2 = calculate_path_to_goal(explorer2_list)
   print(path_list2)




   display_galaxy(galaxy_map_1)
   display_galaxy(galaxy_map_2)
   galaxy2_symbols = get_unique_objects(galaxy_map_2)
   galaxy1_symbols = get_unique_objects(galaxy_map_1)
   print(galaxy1_symbols)
   print(galaxy2_symbols)


if __name__ == '__main__':
   run_exploration()
