class myclass:
    def __init__(self, color,radius):
        self.radius = radius
        self.color = color

    def add_radius(self,r):
        self.radius += r
        print(self.radius)
obj1 = myclass("red", 10)
obj1.add_radius(10)