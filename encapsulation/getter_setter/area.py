from this import d


class Area:
    def __init__(self) -> None:
        self.__base = 0
        self.__high = 0
    # getter base
    @property 
    def base(self):
        return self.__base
    
    # setter base
    @base.setter
    def base(self,value):
        self.__base = value
    
    # getter high
    @property 
    def high(self):
        return self.__high
    
    # setter high
    @high.setter
    def high(self,value):
        self.__high = value #หรือ self.high = value

    def compute_area(self):
        return 0.5 * self.base * self.high
        #หรือ return 0.5 * self.__base * self.__high