import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.animation import FuncAnimation
import random
import time
import heapq

# Define conveyor and box parameters
conveyor_width = 200  # Width of conveyor in pixels
conveyor_height = 600  # Height of conveyor in pixels
exit_position = 600  # Position where boxes exit the conveyor
lanes_y = [0, 150, 300, 450]  # Y-positions for each lane
gap = 40  # Required gap between tail of one box and head of the next box in pixels

# Box class representing each parcel
class Box:
    def __init__(self, ax, lane_y, conveyor_id, initial_x, priority):
        self.ax = ax
        self.lane_y = lane_y + 60
        self.conveyor_id = conveyor_id
        self.priority = priority
        self.x_pos = initial_x
        self.left_edge = 0
        self.right_edge = 0
        self.width = 30 #random.randint(30, 50)
        self.height = 30 #random.randint(30, 50) 
        self.rotation_angle = 0 #np.radians(random.uniform(0, 0))
        self.speed = 2
        self.create_box()

    def __repr__(self):
        return (f"X_pos={self.x_pos}")

    def create_box(self):
    # Calculate the rotated corners of the box
        self.corners = np.array([
            [-self.width / 2, -self.height / 2],
            [self.width / 2, -self.height / 2],
            [self.width / 2, self.height / 2],
            [-self.width / 2, self.height / 2]
        ])
        #print(self.corners)
        rotation_matrix = np.array([
            [np.cos(self.rotation_angle), -np.sin(self.rotation_angle)],
            [np.sin(self.rotation_angle), np.cos(self.rotation_angle)]
        ])
        #print(rotation_matrix)
        centered_y = (self.lane_y - 20) - self.height / 2
        rotated_corners = self.corners.dot(rotation_matrix) + [self.x_pos, self.lane_y]
        #print(rotated_corners)
        self.rect = patches.Polygon(rotated_corners, closed=True, edgecolor="black", facecolor="lightgrey")
        self.text = ax.text(self.x_pos + self.width / 4, centered_y + self.height / 4, str(self.priority),
                        ha='center', va='center', fontsize=8, color='black')
        self.ax.add_patch(self.rect)

        # Marking left and right edges as points
        self.left_edge_marker, = self.ax.plot([], [], 'bo', label="Left Edge")
        self.right_edge_marker, = self.ax.plot([], [], 'ro', label="Right Edge")
        self.update_edge_markers()

    def move(self):
        self.x_pos += self.speed
        translation = np.array([self.x_pos, self.lane_y]) - np.array([self.rect.xy[0, 0], self.rect.xy[0, 1]])
        self.rect.xy += translation
        self.text.set_x(self.x_pos + self.width / 4)
        self.update_edge_markers()

    def get_right_edge(self):
        self.right_edge = np.max(self.rect.xy[:, 0])
        return self.right_edge

    def get_left_edge(self):
        self.left_edge = np.min(self.rect.xy[:, 0])
        return self.left_edge

    def update_edge_markers(self):
        left_edge_x = self.get_left_edge()
        right_edge_x = self.get_right_edge()
        self.left_edge_marker.set_data([left_edge_x], [self.lane_y])
        self.right_edge_marker.set_data([right_edge_x], [self.lane_y])

    def remove(self):
        self.rect.remove()
        self.text.remove()
        self.left_edge_marker.remove()
        self.right_edge_marker.remove()

# Conveyor class to manage a single box on a single lane
class Conveyor:
    def __init__(self, ax, lane_y, conveyor_id, interface):
        self.ax = ax
        self.lane_y = lane_y
        self.conveyor_id = conveyor_id
        self.interface = interface  # Interface to interact with other conveyors
        self.box = None  # Initialize without a box
        self.speed = 2

    def __repr__(self) -> str:
        return str(self.conveyor_id)

    def update_position(self):
        if self.box:
            if self.box.get_left_edge() > 0 and self.box.priority == 0:
                self.interface.register_box(self.box)
                self.interface.assign_priorities()

            if self.box.get_left_edge() < exit_position and self.box.get_left_edge() > 0:
                next_box = self.interface.get_next_priority_box(self.box.priority)
                if next_box:
                    distance_to_next_box = next_box.get_left_edge() - self.box.get_right_edge()
                    self.box.speed = 1 if distance_to_next_box < gap else 2
                else:
                    self.box.speed = 2

                self.box.move()

            elif self.box.get_left_edge() >= exit_position:
                print(f"Box {self.box} exited at {self.box.get_left_edge()}")
                self.box.remove()
                self.interface.unregister_box(self.box)
                self.box = None
            else:
                self.box.move()


# Conveyor interface to manage interactions between conveyors
class ConveyorInterface:
    def __init__(self):
        self.priority_queue = []  # Min-heap for priority-based scheduling
        self.box_to_priority = {}  # Map boxes to their priorities
        self.conveyors = {}
        self.distances = []

    def register_conveyor(self, conveyor):
        self.conveyors[conveyor.conveyor_id] = conveyor

    def register_box(self, box):
        if box not in self.box_to_priority:  # Avoid duplicates
            distance = exit_position - box.get_right_edge()
            heapq.heappush(self.priority_queue, (distance, box))
            self.box_to_priority[box] = distance

    def unregister_box(self, box):
        if box in self.box_to_priority:
            del self.box_to_priority[box]
            # Rebuild the heap to remove the box
            self.priority_queue = [
                (distance, b) for distance, b in self.priority_queue if b != box
            ]
            heapq.heapify(self.priority_queue)

    def assign_priorities(self):
        self.priority_queue = []  # Clear the queue
        self.box_to_priority = {}  # Reset the mapping
        for conveyor in self.conveyors.values():
            if conveyor.box:
                box = conveyor.box
                distance = exit_position - box.get_right_edge()
                heapq.heappush(self.priority_queue, (distance, box))
                self.box_to_priority[box] = distance

    def get_next_priority_box(self, current_priority):
        if self.priority_queue:
            return heapq.heappop(self.priority_queue)[1]
        return None


# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(-100, conveyor_height + 100)
ax.set_ylim(0, conveyor_height)
ax.axis('on')

# Draw conveyor lane borders
for lane_y in lanes_y:
    ax.plot([-100, conveyor_height + 100], [lane_y, lane_y], color='gray', linestyle='-', linewidth=2)


# Add vertical lines at x = 0 and x = 600
ax.axvline(x=0, color='red', linestyle='--', linewidth=2, label="Start Line")
ax.axvline(x=600, color='blue', linestyle='--', linewidth=2, label="Exit Line")


# Create ConveyorInterface and Conveyor objects and then we will be changing its propertiesl later
interface = ConveyorInterface()

conveyors = []
for idx, lane_y in enumerate(lanes_y):
    conveyor = Conveyor(ax, lane_y, idx, interface)
    conveyors.append(conveyor)
    interface.register_conveyor(conveyor)

#print(interface)
#print(len(conveyors))

def box_generator(interface):
    for conveyor in conveyors:
        # Check if the conveyor has no box
        if conveyor.box is None:
            initial_x = random.randint(-100, 0)
            conveyor.box = Box(
                conveyor.ax, conveyor.lane_y, conveyor.conveyor_id + 1, initial_x, 0
            )
            print(f"New box created on empty conveyor {conveyor.conveyor_id + 1} at X: {initial_x}")
            break
        else:
            # Check if there's enough space to add another box
            last_box_right_edge = conveyor.box.get_right_edge()
            if last_box_right_edge < 0:  # Check if the last box is far enough from the start
                initial_x = random.randint(-100, 0)
                if abs(initial_x - last_box_right_edge) > gap:  # Ensure no overlap
                    conveyor.box = Box(
                        conveyor.ax, conveyor.lane_y, conveyor.conveyor_id + 1, initial_x, 0
                    )
                    print(f"Additional box created on conveyor {conveyor.conveyor_id + 1} at X: {initial_x}")
                    break



# Update function for animation
def update(frame):
    # Generate boxes only if needed
    box_generator(interface)

    # Update positions for all conveyors
    for conveyor in conveyors:
        conveyor.update_position()








# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)
plt.show()
                  
