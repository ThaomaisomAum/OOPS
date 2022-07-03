class Geograhhic:
    def setcordinate(self,lat,long):
        self.latitude = lat
        self.longitude = long

    def getcordinate(self):
        return f'Latitude: {self.latitude}\nLongtitude: {self.longitude}'
    
    def gettimezone(self):
        timezone = round(self.longitude/12-1)
        if timezone > 0:
            return f'Timezone + {timezone}'#timezone+7
        else:
            return f'Timezone{timezone}' #timezone-12
    
    def getclimate(self):
        if self.latitude <= -66.5 or self.latitude >= 66.5:
            return 'Polar zone'
        elif self.latitude <= -23.5 or self.latitude >= 23.5:
            return 'Temperate zone'
        else:
            return 'Tropical zone'



