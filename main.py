from classes.point import Point
from classes.rectangle import Rectangle
from classes.gui_rectangle import GuiRectangle
from classes.gui_point import GuiPoint
from random import randint
import turtle
# Rectangle Points
rectangle_bottom_left = Point(1,1)
rectangle_top_right = Point(6,6)

# Create a rectangle and a point
rectangle = Rectangle(rectangle_bottom_left, rectangle_top_right)
point = Point(2,2)

# Calculate distance from point
point_distance = point.calculate_distance(Point(3, 2))

# Area
rectangle_area = rectangle.area()

# Check if rectangle and point overlaps
does_fall_into_rectangle = point.falls_into_rectangle(rectangle)

# print(does_fall_into_rectangle)

rectangle_bottom_left = Point(randint(0,100), randint(0,100))
rectangle_top_right = Point(randint(10,100), randint(10,100))
gui_rectangle = GuiRectangle(rectangle_bottom_left, rectangle_top_right)
gui_point = GuiPoint(point.x, point.y)
    

my_turtle = turtle.Turtle()
gui_rectangle.draw(canvas=my_turtle)
gui_point.draw(canvas=my_turtle)
turtle.done()
