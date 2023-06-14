import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Draw the background rectangle
background = patches.Rectangle((0, 0), 10, 6, facecolor='forestgreen')
ax.add_patch(background)

# Draw the red circle
circle = patches.Circle((4.5, 3), radius=2, facecolor='red')
ax.add_patch(circle)

# Set the limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)


# Display the flag
plt.show()