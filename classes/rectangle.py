class Rectangle:

    def __init__(self, bottom_left, top_right):
        self.bottom_left = bottom_left
        self.top_right = top_right
        
    
    def area(self):
        return (self.bottom_left.x - self.top_right.x) * \
        (self.bottom_left.y - self.top_right.y)



