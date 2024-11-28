import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.animation import FuncAnimation
import random
import time

# Define conveyor and box parameters
conveyor_width = 200  # Width of conveyor in pixels
conveyor_height = 600  # Height of conveyor in pixels
exit_position = 600  # Position where boxes exit the conveyor
lanes_y = [0, 150, 300, 450]  # Y-positions for each lane
gap = 40  # Required gap between tail of one box and head of the next box in pixels


# Box class representing each parcel
class Box:
    last_box_id = 0
    def __init__(self, ax, lane_y, conveyor_id, initial_x, priority):
        Box.last_box_id = Box.last_box_id + 1
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
        self.box_id = Box.last_box_id
        
        self.create_box()

    def __repr__(self):
        return (f"Box_id= {self.box_id} X_pos={self.x_pos}, Priority={self.priority}")

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
                print(f"First Condition box: {self.box}")
                self.interface.register_box(self.box)
                self.interface.assign_priorities()
                print(f"No priority assigned: {self.box}")

            if self.box.get_left_edge() < exit_position and self.box.get_left_edge() > 0:
                print(f"Second Condition box: {self.box}")
                next_box = self.interface.get_next_priority_box(self.box.priority)
                if next_box:
                    distance_to_next_box = next_box.get_left_edge() - self.box.get_right_edge()
                    self.box.speed = 1 if distance_to_next_box < gap else 2
                    print(f"next box: {next_box}")
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
                if self.box.box_id == 1:
                    print(f"box move only: {self.box}")



# Conveyor interface to manage interactions between conveyors
class ConveyorInterface:
    def __init__(self):
        self.boxes = []
        self.conveyors = {}
        self.distances = [0, 0, 0, 0]
        self.priority = None 

    def __repr__(self) -> str:
        return f"Conveyors: {self.conveyors}"

    def register_conveyor(self, conveyor):
        self.conveyors[conveyor.conveyor_id] = conveyor

    def register_box(self, box):
        if box not in self.boxes:  # Avoid duplicates
            self.boxes.append(box)

    def unregister_box(self, box):
        if box in self.boxes:
            self.boxes.remove(box)

    def interface_boxes(self):
        return self.boxes

    def get_next_priority_box(self, current_priority):
        # Get the next lower-priority box
        lower_priority_boxes = [box for box in self.boxes if box.priority > current_priority]
        if lower_priority_boxes:
            prior = min(lower_priority_boxes, key=lambda b: b.priority)
            return prior
        return None

    def reinitialize_boxes(self):
        # Clear all existing boxes
        self.boxes.clear()
        # Reinitialize each conveyor with a new box at a random position
        for conveyor in self.conveyors.values():
            conveyor.initialize_box()


    def assign_priorities(self):
        # Dynamically adjust the size of the distances list to match the number of boxes
        self.distances = [0] * len(self.boxes)

        # Calculate distances for each box
        for index, box in enumerate(self.boxes):
            dist = exit_position - box.get_right_edge()  # Distance to the exit
            self.distances[index] = dist

        # Sort boxes by distance to the exit in ascending order
        sorted_indices = sorted(range(len(self.distances)), key=lambda x: self.distances[x])

        # Assign priorities based on sorted indices
        for rank, index in enumerate(sorted_indices, start=1):
            self.boxes[index].priority = rank
            self.boxes[index].text.set_text(str(rank))  # Update displayed priority


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
    # Check if there is space available on any conveyor between -100 and 0
    for conveyor in conveyors:
        if conveyor.box is None:
            # Create a box if the conveyor is empty
            initial_x = random.randint(-100, 0)
            #print(initial_x)
            conveyor.box = Box(
                conveyor.ax, conveyor.lane_y, conveyor.conveyor_id + 1, initial_x, 0
            )
            #interface.register_box(conveyor.box)
            break
        else:
            # Check if there's space on the conveyor
            left_edge = conveyor.box.get_left_edge()
            if left_edge > 0:  # Space available
                initial_x = random.randint(-100, 0)
                if abs(initial_x - left_edge) > gap:  # Ensure no overlap
                    conveyor.box = Box(
                        conveyor.ax, conveyor.lane_y, conveyor.conveyor_id + 1, initial_x, 0
                    )
                    #print(initial_x)
                    #interface.register_box(conveyor.box)
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
                  
