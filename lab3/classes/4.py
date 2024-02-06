
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_0 = x
        self.y_0 = y

    def show(self):
        print(f"Coordinate x: {self.x}, and y: {self.y}")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self):
        return pow( ( pow((self.x - self.x_0), 2) + pow((self.y - self.y_0), 2) ), 0.5)
    

x, y = map(int, input().split())

some = Point(x, y)

some.show()

x1, y1 = map(int, input().split())
some.move(x1, y1)

some.show()

print("\nTheir dist =", some.dist())


