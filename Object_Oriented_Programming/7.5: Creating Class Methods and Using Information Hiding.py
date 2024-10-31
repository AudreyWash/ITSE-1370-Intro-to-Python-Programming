# class MoviePlayer
class MoviePlayer:
    # private movie list and public firmware version and current movie
    __movies = []
    firmware_version = 1.0
    current_movie = ""

    # default constructor which add some movies into movie list
    def __init__(self):
        self.__movies = ['Frozen', 'Finding Nemo', 'Toy Story']

    # Method to set current movie to first item of movie list
    def play(self):
        self.current_movie =  self.__movies[0]

    # method to return the movie list
    def list_movies(self):
        return self.__movies

    # Method to check if given version is latest or not
    # if it is latest then update tje firmware
    def update_firmware(self, n):
        if n > self.firmware_version:
            self.firmware_version = n


# The code below used for test your class
if __name__ == '__main__':
    player = MoviePlayer()
    print("Movies currently on device:", player.list_movies())

    player.update_firmware(2.0)
    print("Updated player firmware version to", player.firmware_version)

    player.play()
    print("Currently playing", f"'{player.current_movie}'")
