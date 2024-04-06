from classes.rectangle import Rectangle
import turtle

class GuiRectangle(Rectangle):
    def draw(self, canvas):
        # Go to point bottom left
        canvas.penup()
        canvas.goto(self.bottom_left.x, self.bottom_left.y)
        canvas.pendown()
        
        canvas.forward(self.top_right.x - self.bottom_left.x)
        canvas.left(90)
        canvas.forward(self.top_right.y - self.bottom_left.y)
        canvas.left(90)
        canvas.forward(self.top_right.x - self.bottom_left.x)
        canvas.left(90)
        canvas.forward(self.top_right.y - self.bottom_left.y)
        turtle.done()

