class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check_point(self):
        match (self.x, self.y):
            case (0, 0):
                print("Origin")
            case (0, y):
                print(f"Y={y} line")
            case (x, 0):
                print(f"X={x} line")
            case (x, y):
                print(f"Point ({x}, {y})")
            case _:
                print("Not a point")