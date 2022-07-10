class Mule:
    def run(self):
        self.run = "Mule is running"
        return(f'run: {self.run}')

from donkey import Donkey
mule1 = Donkey(None,'Mumu','Blue-eyed cream')
mule1.age(3)
mule1.weight(200)

mule2 = Donkey(None,'Meme','palomino')
mule2.age(1)
mule2.weight(120.7)
