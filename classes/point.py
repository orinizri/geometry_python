class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_into_rectangle(self, rectangle):
        return (
            rectangle.bottom_left.x < self.x < rectangle.top_right.x
            and rectangle.bottom_left.y < self.x < rectangle.top_right.y
        )

    def calculate_distance(self, point):
        return abs((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
