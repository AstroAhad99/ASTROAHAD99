import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.animation import FuncAnimation
import random

# Define conveyor and box parameters
conveyor_width = 200  # Width of conveyor in pixels
conveyor_height = 600  # Height of conveyor in pixels
exit_position = 600  # Position where boxes exit the conveyor
lanes_y = [0, 150, 300, 450]  # Y-positions for each lane
gap = 40  # Required gap between tail of one box and head of the next box in pixels


class Box:
    def __init__(self, ax, lane_y, box_id, initial_x, priority, width, height):
        self.ax = ax
        self.lane_y = lane_y
        self.box_id = box_id
        self.priority = priority
        self.x_pos = initial_x
        self.width = width
        self.height = height
        self.speed = 2  # Initial speed
        self.rect = patches.Rectangle(
            (self.x_pos, lane_y + (150 - self.height) / 2),
            self.width,
            self.height,
            edgecolor="black",
            facecolor="lightgrey",
        )
        self.text = ax.text(
            self.x_pos + self.width / 2,
            lane_y + 75,
            str(self.priority),
            ha="center",
            va="center",
            fontsize=8,
            color="black",
        )
        self.ax.add_patch(self.rect)

    def move(self):
        self.x_pos += self.speed
        self.rect.set_x(self.x_pos)
        self.text.set_x(self.x_pos + self.width / 2)

    def remove(self):
        self.rect.remove()
        self.text.remove()

    def get_right_edge(self):
        return self.x_pos + self.width

    def get_left_edge(self):
        return self.x_pos


class Conveyor:
    def __init__(self, ax, lane_y, conveyor_id, interface, box):
        self.ax = ax
        self.lane_y = lane_y
        self.conveyor_id = conveyor_id
        self.interface = interface
        self.box = box  # Initialize with a box

    def update_position(self):
        if self.box:
            if self.box.get_right_edge() < exit_position:
                next_box = self.interface.get_next_priority_box(self.box.priority)
                if next_box:
                    distance_to_next_box = next_box.get_left_edge() - self.box.get_right_edge()
                    if distance_to_next_box < gap:
                        self.box.speed = 1  # Slow down if gap is less
                    else:
                        self.box.speed = 2  # Speed up if gap is sufficient
                self.box.move()
            else:
                self.box.remove()
                self.interface.unregister_box(self.box)
                self.box = None

        if not any(conveyor.box for conveyor in self.interface.conveyors.values()):
            Builder(self.interface)


class ConveyorInterface:
    def __init__(self):
        self.boxes = []
        self.conveyors = {}

    def register_conveyor(self, conveyor):
        self.conveyors[conveyor.conveyor_id] = conveyor

    def register_box(self, box):
        self.boxes.append(box)

    def unregister_box(self, box):
        if box in self.boxes:
            self.boxes.remove(box)

    def get_next_priority_box(self, current_priority):
        lower_priority_boxes = [box for box in self.boxes if box.priority > current_priority]
        if lower_priority_boxes:
            return min(lower_priority_boxes, key=lambda b: b.priority)
        return None


def Builder(interface):
    x_positions = [random.randint(0, 20) for _ in range(4)]
    widths = [random.randint(40, 80) for _ in range(4)]
    heights = [random.randint(40, 80) for _ in range(4)]

    # Calculate distances for priority assignment
    distances = [
        x_positions[i] + widths[i] for i in range(len(x_positions))
    ]  # Use the right edge for priority
    sorted_indices = sorted(range(len(distances)), key=lambda x: distances[x])
    priorities = [0] * len(distances)
    for rank, index in enumerate(sorted_indices, start=1):
        priorities[index] = len(distances) - rank + 1

    # Create boxes with assigned priorities
    boxes = []
    for i in range(4):
        box = Box(ax, lanes_y[i], i + 1, x_positions[i], priorities[i], widths[i], heights[i])
        interface.register_box(box)
        interface.conveyors[i].box = box
        boxes.append(box)
    return boxes


# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(-100, conveyor_height)
ax.set_ylim(-100, conveyor_height + 100)
ax.axis("on")

# Initialize ConveyorInterface and Conveyors
interface = ConveyorInterface()
conveyors = []
for i, lane_y in enumerate(lanes_y):
    conveyor = Conveyor(ax, lane_y, i, interface, None)
    conveyors.append(conveyor)
    interface.register_conveyor(conveyor)

# Generate initial boxes
Builder(interface)

# Draw conveyor lane borders
for lane_y in lanes_y:
    ax.plot([-100, conveyor_height], [lane_y, lane_y], color="gray", linestyle="-", linewidth=2)

# Update function for animation
def update(frame):
    for conveyor in conveyors:
        conveyor.update_position()


# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)
plt.show()
