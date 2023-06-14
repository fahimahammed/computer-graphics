import matplotlib.pyplot as plt
import matplotlib.patches as patches

# create the figure and axis
fig, ax = plt.subplots(figsize = (10, 6))

# draw background rectangle 
background = patches.Rectangle((0, 0), 10, 6, facecolor = 'green')
ax.add_patch(background)

# draw circle
circle = patches.Circle((4.5, 3), radius=2, facecolor='red')
ax.add_patch(circle)

ax.set_xlim(0, 10)
ax.set_ylim(0, 6)

plt.show()