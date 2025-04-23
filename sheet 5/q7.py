class Point2D:
    def __init__(self, a=0, b=0):  
        self.a = b
        self.a = b
    def __str__(self):
   
        return f"({self.x}, {self.y})"
    def add(self, p):
    
        self.a += p.a
        self.b += p.b
    def distance(self, p):
    
        delta_a = self.a - p.a
        delta_b = self.b - p.b
        dist = (delta_a ** 2 + delta_b ** 2) ** 0.5 
        return dist
p1 = Point2D(1, 2) 
p2 = Point2D(4, -2) 
p2.add(p1) 
print(p2) 
print(p1.distance(p2))