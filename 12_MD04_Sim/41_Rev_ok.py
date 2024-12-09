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
        self.boxes = []  # List of boxes on the conveyor
        self.speed = 2


    def __repr__(self):
        return f"Conveyor {self.conveyor_id} with {len(self.boxes)} boxes."


    def update_position(self):
        # Assign priorities to boxes with no priority
        for box in self.boxes[:]:  # Iterate over a copy of the list
            if self.interface.assign_counter < 2:
                if box.get_left_edge() > 0 and box.priority == 0:
                    self.interface.register_box(box)
                    self.interface.assign_priorities()
                    self.interface.assign_counter += 1

        # Adjust speed and update position for each box
        for i, box in enumerate(self.boxes[:]):
            if box.get_left_edge() < exit_position:
                # Handle box movement based on the next box in the priority order
                next_box = self.interface.get_next_priority_box(box.priority)
                if next_box:
                    # Calculate gap to the next box
                    distance_to_next_box = next_box.get_left_edge() - box.get_right_edge()

                    # Adjust speed for the current box
                    box.speed = 1 if distance_to_next_box < gap else 2

                    # Reset counter if the gap condition is satisfied
                    if distance_to_next_box == gap:
                        self.interface.assign_counter = 0
                elif box.priority == 0:
                    # If no priority is assigned, keep the box moving slowly
                    box.speed = 1
                else:
                    # Default speed for boxes with no immediate next box
                    box.speed = 2

                # Move the current box
                box.move()
            elif box.get_left_edge() >= exit_position:
                # Remove the box if it reaches the exit
                print(f"Box {box} exited at {box.get_left_edge()}")
                box.remove()
                self.interface.unregister_box(box)
                self.boxes.remove(box)  # Remove the box from the conveyor's list




# Conveyor interface to manage interactions between conveyors
class ConveyorInterface:
    def __init__(self):
        self.boxes = []
        self.conveyors = {}
        self.distances = [0, 0, 0, 0]
        self.priority = None
        self.total_boxes_generated = 0  # Counter for total generated boxes
        self.box_limit = 6  # Maximum number of boxes allowed
        self.first_prior = 0
        self.second_prior = 0
        self.assign_counter = 0
        self.gap_gen = False

    def __repr__(self) -> str:
        return f"Conveyors: {self.conveyors}"

    def register_conveyor(self, conveyor):
        self.conveyors[conveyor.conveyor_id] = conveyor

    def register_box(self, box):
        #if box not in self.boxes and self.total_boxes_generated < self.box_limit:
        if box not in self.boxes:  # Check box limit
            self.boxes.append(box)
            #self.total_boxes_generated += 1  # Increment the counter

    def unregister_box(self, box):
        if box in self.boxes:
            self.boxes.remove(box)

    def interface_boxes(self):
        return self.boxes

    def get_next_priority_box(self, current_priority):
        # Get the next lower-priority box
        lower_priority_boxes = [box for box in self.boxes if box.priority < current_priority]
        if lower_priority_boxes:
            prior = max(lower_priority_boxes, key=lambda b: b.priority)
            return prior
        return None

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



# Updated box_generator function to append boxes to a list in each conveyor
def box_generator(interface):
    if interface.total_boxes_generated >= interface.box_limit:
        return  # Stop generating boxes if the limit is reached

    for conveyor in conveyors:
        if not conveyor.boxes:  # If the conveyor has no boxes
            # Create a box and append it to the conveyor's box list
            initial_x = random.randint(-100, 0)
            new_box = Box(conveyor.ax, conveyor.lane_y, conveyor.conveyor_id + 1, initial_x, 0)
            conveyor.boxes.append(new_box)
            interface.total_boxes_generated += 1
            #interface.register_box(new_box)
            break
        else:
            # Check if there's space for a new box at the start of the conveyor
            last_box = conveyor.boxes[-1]  # Get the last box on the conveyor
            if last_box.get_left_edge() > 0:  # Space available
                initial_x = random.randint(-100, 0)
                if abs(initial_x - last_box.get_left_edge()) > gap:  # Ensure no overlap
                    new_box = Box(conveyor.ax, conveyor.lane_y, conveyor.conveyor_id + 1, initial_x, 0)
                    conveyor.boxes.append(new_box)
                    interface.total_boxes_generated += 1
                    #interface.register_box(new_box)
                    break


# ------------------------------------------------------------------------------------------------

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

# Update function for animation
def update(frame):
    # Generate boxes if needed
    box_generator(interface)

    # Update positions for all conveyors
    for conveyor in conveyors:
        conveyor.update_position()


#print(interface)
#print(len(conveyors))

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)
plt.show()