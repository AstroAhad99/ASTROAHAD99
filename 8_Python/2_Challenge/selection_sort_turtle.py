
import turtle
import time

# Setup the screen
screen = turtle.Screen()
screen.title("Selection Sort Visualization")
screen.bgcolor("white")
screen.setup(width=600, height=400)

# Create the turtle object to draw bars
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(-250, -150)

# Function to draw bars based on the array values
def draw_bars(array, colors):
    pen.clear()
    for i, value in enumerate(array):
        pen.goto(-250 + i * 40, -150)
        pen.fillcolor(colors[i])
        pen.begin_fill()
        pen.setheading(90)  # Face upwards
        pen.forward(value)
        pen.right(90)
        pen.forward(30)
        pen.right(90)
        pen.forward(value)
        pen.right(90)
        pen.forward(30)
        pen.end_fill()

# Selection sort with visualization
def selection_sort(array):
    for i in range(len(array)):
        # Assume the current position is the minimum
        min_index = i
        colors = ["gray"] * len(array)
        colors[i] = "blue"  # Mark the current position in blue
        
        # Find the minimum element in the remaining array
        for j in range(i + 1, len(array)):
            colors[j] = "red"  # Mark the current comparison element in red
            draw_bars(array, colors)
            time.sleep(0.5)
            
            if array[j] < array[min_index]:
                min_index = j
            
            colors[j] = "gray"  # Reset comparison bar back to gray

        # Swap the found minimum element with the first element
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
        
        colors[i] = "green"  # Mark the sorted position in green
        draw_bars(array, colors)
        time.sleep(0.5)

# Test data
array = [80, 120, 40, 90, 160, 20, 60]

# Run the selection sort and visualize the sorting process
draw_bars(array, ["gray"] * len(array))  # Initial drawing
time.sleep(1)  # Pause before starting the sort
selection_sort(array)

# Keep the window open until clicked
screen.exitonclick()
