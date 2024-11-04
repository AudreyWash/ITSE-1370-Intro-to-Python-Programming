import random


def number_randomizer(num):
    return [random.randint(0, 100) for _ in range(num)]


if __name__ == '__main__':
    print(number_randomizer(2))
    print(number_randomizer(4))
    print(number_randomizer(6))