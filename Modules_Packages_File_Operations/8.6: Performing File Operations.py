def create_file():
    with open('newfile.txt', 'w') as file:
        file.write("I enjoy learning to code in Python")  # Ensure the string matches exactly


if __name__ == '__main__':
    create_file()
