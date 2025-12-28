import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle, Circle

# Load data from file
data = np.loadtxt('lqr_cartpend_data.csv', delimiter=',')
t = data[:, 0]
x = data[:, 1]
theta = data[:, 2]

# Animation parameters
cart_width = 0.3
cart_height = 0.2
pendulum_length = 1.0  # Adjust to match your system
fps = 30
frame_skip = max(1, len(t) // (fps * (t[-1] - t[0])))  # Skip frames to match real-time

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(x.min() - 2, x.max() + 2)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.axhline(y=-cart_height/2, color='k', linewidth=2)  # Ground line

# Create objects
cart = Rectangle((0, -cart_height), cart_width, cart_height, 
                 fill=True, color='blue', ec='darkblue', linewidth=2)
wheel1 = Circle((0, -cart_height/2), 0.05, color='black')
wheel2 = Circle((0, -cart_height/2), 0.05, color='black')
pendulum_line, = ax.plot([], [], 'r-', linewidth=3)
pendulum_bob = Circle((0, 0), 0.08, color='red')
pivot = Circle((0, 0), 0.04, color='orange')

# Add objects to plot
ax.add_patch(cart)
ax.add_patch(wheel1)
ax.add_patch(wheel2)
ax.add_patch(pendulum_bob)
ax.add_patch(pivot)

# Text display
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, 
                    fontsize=12, verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

def init():
    """Initialize animation"""
    cart.set_xy((0, -cart_height))
    wheel1.center = (0, -cart_height/2)
    wheel2.center = (0, -cart_height/2)
    pendulum_line.set_data([], [])
    pendulum_bob.center = (0, 0)
    pivot.center = (0, 0)
    time_text.set_text('')
    return cart, wheel1, wheel2, pendulum_line, pendulum_bob, pivot, time_text

def animate(frame):
    """Animation function"""
    i = frame * frame_skip
    if i >= len(t):
        i = len(t) - 1
    
    # Update cart position
    cart_x = x[i] - cart_width/2
    cart.set_xy((cart_x, -cart_height))
    
    # Update wheels
    wheel1.center = (x[i] - cart_width/3, -cart_height/2)
    wheel2.center = (x[i] + cart_width/3, -cart_height/2)
    
    # Update pivot
    pivot_x = x[i]
    pivot_y = 0
    pivot.center = (pivot_x, pivot_y)
    
    # Calculate pendulum position (theta = pi is upright)
    pendulum_x = pivot_x + pendulum_length * np.sin(theta[i])
    pendulum_y = pivot_y - pendulum_length * np.cos(theta[i])
    
    # Update pendulum
    pendulum_line.set_data([pivot_x, pendulum_x], [pivot_y, pendulum_y])
    pendulum_bob.center = (pendulum_x, pendulum_y)
    
    # Update text
    angle_deg = (theta[i] - np.pi) * 180 / np.pi
    time_text.set_text(f'Time: {t[i]:.3f} s\n'
                      f'Cart x: {x[i]:.3f} m\n'
                      f'Angle: {theta[i]:.3f} rad ({angle_deg:.1f}° from upright)')
    
    return cart, wheel1, wheel2, pendulum_line, pendulum_bob, pivot, time_text

# Create animation
num_frames = len(t) // frame_skip
ani = animation.FuncAnimation(fig, animate, init_func=init,
                            frames=num_frames, interval=1000/fps,
                            blit=True, repeat=True)

plt.xlabel('Position (m)')
plt.ylabel('Height (m)')
plt.title('Cart-Pendulum System with LQR Control')
plt.tight_layout()

# To save the animation (optional)
# ani.save('cart_pendulum.mp4', writer='ffmpeg', fps=fps, dpi=100)
# ani.save('cart_pendulum.gif', writer='pillow', fps=fps)

plt.show()