# Rectangle and Point GUI Drawing with Turtle Library

Python project to draw rectangles and points on a canvas using Turtle graphics library.

## Table of Contents

-   [About](#about)
-   [Getting Started](#getting-started)
-   [Usage](#usage)
-   [Class Descriptions](#class-descriptions)

## About <a name = "about"></a>

This Python project provides functionality to draw rectangles and points on a canvas using the Turtle graphics library. It consists of four classes: Rectangle, GuiRectangle, Point, and GuiPoint.

## Getting Started <a name = "getting-started"></a>

These instructions will guide you to set up the project on your local machine.

### Prerequisites

Ensure you have Python installed on your system.

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/orinizri/geometry_python.git
    ```

Usage <a name="usage"></a>
Running the Code:

Execute the main script:
python main.py

Expected Output:
A Turtle graphics window will open displaying a rectangle and a point drawn on a canvas.

### <h1>Class Descriptions</h1> <a name="class-descriptions"></a>

### <strong>Rectangle</strong>
Represents a rectangle with bottom-left and top-right points.
Provides methods to calculate area and check if a point falls inside the rectangle.
Area Calculation Method: area()

### <strong>GuiRectangle</strong>

Extends the Rectangle class for GUI representation.
Includes a method to draw the rectangle on a Turtle canvas.

### <strong>Point</strong>

Represents a point in 2D space with x and y coordinates.
Provides a method to calculate the distance between two points.

### <strong>GuiPoint</strong>

Extends the Point class for GUI representation.
Includes a method to draw the point on a Turtle canvas.
