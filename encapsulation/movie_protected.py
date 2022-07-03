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
    def _get_movie_detail(self):
        return print(f"title = {self._title}\nyear = {self._year}\ngenre = {self._genre}")


# derived class
class Documentary(Movie):
    def __init__(self) -> None:
        super().__init__()
    def add_channel(self,channel):
        self.channel =  channel
    def _getmovie_detail(self):
        Movie._getmovie_detail()
        print(f'Channel: {self.channel}')
        

#สร้างObject
if __name__ == '__main__':
    movie1 = Documentary()
    movie1._add_movie("My Octopus Teacher",2020,"Documentaty")
    movie1.add_channel("NetFliex")
    movie1._get_movie_detail() #ไม่มีข้อมูลของ channel
    print(f"channel = {movie1.channel}")
    print(f"rating = {movie1._rating}")