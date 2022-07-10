class Horse:
    def __init__(self, max_height:float, name:str, color:str) -> None:
        super().__init__(max_height, name, color)
        self.max_height = "200"
        self.name = "Khan Khan"
        self.color = "Grey"


    def run(self):
        self.run = "Khan Khan is running"
        return(f'run: {self.run}')

    def show_name(self):
        return f'Name: {self.name}'

    def show_info(self):
        print(f'Name: {self.name}')
        print(f'Color: {self.color}')
        print(f'Max Height: {self.max_height}')