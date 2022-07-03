from cgi import print_form
from os import popen
from sunau import Au_read
from unicodedata import name
from geographic import Geographic
from temperature import Temperature

class Country(Geographic,Temperature):
    def __init__(self) -> None:
        #super().__init__()
        Geographic.__init__(self)
        Temperature.__init__(self)
        self.name = name
        self.area = area
        self.population = pop
    
    def getpopulation_density(self):
        return self.population / self.area

    def show_detail(self):
        #ชื่อประเทศ
        print(f'Country: {self.name}')

        #แสดงที่ตั้ง latitude , longtitude
        print(self.getcordinte())

        #แสดงขนาดพื้นที่ ,จำนวนประชากร และความหนาแน่นของประชากร
        print(f'Area: {self.area,.2f}')
        print(f'Population: {self.population}Millino()')
        print(f'Density:{self.getpopulation_density()}')

        #Time Zone, Climate,Teperrature, Weather
        print(f'Timezone: {self.gettimezone()}')
        print(f'Climate: {self.getclimate()}')
        print(f'Temperature(C): {self.celsius}')
        print(f'Temperature(F): {self.getfahrenheit()}')
        print(f'Weather: {self.getweather()}')
        print()


