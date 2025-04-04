import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from robot import BrownianRobot  # Make sure robot.py is in the same folder

# Create a robot instance
robot = BrownianRobot()

# For tracking the robot’s path (optional)
x_vals, y_vals = [], []

# Setup the plot
fig, ax = plt.subplots()
ax.set_xlim(0, robot.arena_size)
ax.set_ylim(0, robot.arena_size)
ax.set_title("Brownian Motion Robot Simulation")
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")

# Draw the robot as a point
point, = plt.plot([], [], 'bo', markersize=6)

# Animation update function
def update(frame):
    robot.move()
    x, y = robot.get_position()
    x_vals.append(x)
    y_vals.append(y)
    point.set_data([x], [y])  # Important: wrap in list for blit=True
    return point,

# Create the animation
ani = FuncAnimation(fig, update, frames=500, interval=30, blit=True)

# Display the animation window
plt.show()

# Save the animation as a GIF
ani.save("brownian_motion.gif", writer="pillow", fps=30)
