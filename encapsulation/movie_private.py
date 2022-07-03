class Movie:
    # protected data members
    _title = None
    _year = None
    _genre = None
    _rating = 6

    def __init__(self) -> None:
        pass
    def _add_movie(self,title:str,year:int,genre:str):
        self._title = title
        self._year = year
        self._genre = genre
        self._rating = rating

    def _get_movie_detail(self):
        print(f'Title = {self.__title}')
        print(f'Year = {self.__year}')
        print(f'Genre = {self.__genre}')
        print(f'Rating: {self.__rating}')

class Documentary(Movie):
    def __init__(self) -> None:
        Movie.__init__(self)
    
    def add_channel(self,ch:str):
        self.channel =  ch
    
    def print_detail(self):
        super().print_detail()
        print(f'Channal: {self.channel}')

if __name__ == '__main__':
