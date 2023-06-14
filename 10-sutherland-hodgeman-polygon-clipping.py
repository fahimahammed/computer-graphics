import matplotlib.pyplot as plt

def clip_polygon(frame, polygon):
    def inside(p, clip_edge):
        return (clip_edge[1][0] - clip_edge[0][0]) * (p[1] - clip_edge[0][1]) > (clip_edge[1][1] - clip_edge[0][1]) * (p[0] - clip_edge[0][0])

    def intersect(p1, p2, clip_edge):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        t = (clip_edge[0][1] - p1[1]) * dx - (clip_edge[0][0] - p1[0]) * dy
        d = (clip_edge[1][0] - clip_edge[0][0]) * dy - (clip_edge[1][1] - clip_edge[0][1]) * dx

        if d == 0:
            return None  # Parallel or coincident

        t /= d
        if 0 <= t <= 1:
            return [p1[0] + t * dx, p1[1] + t * dy]
        else:
            return None

    output = polygon.copy()
    clip_edges = [(frame[i], frame[(i+1) % len(frame)]) for i in range(len(frame) - 1)]

    for clip_edge in clip_edges:
        input = output.copy()
        output = []
        s = input[-1]

        for p in input:
            if inside(p, clip_edge):
                if not inside(s, clip_edge):
                    intersect_point = intersect(s, p, clip_edge)
                    if intersect_point is not None:
                        output.append(intersect_point)
                output.append(p)
            elif inside(s, clip_edge):
                intersect_point = intersect(s, p, clip_edge)
                if intersect_point is not None:
                    output.append(intersect_point)
            s = p

    return output

# Example usage
frame = [(0, 0), (8, 0), (8, 8), (0, 8), (0, 0)]  # Frame vertices in clockwise order (including the last vertex to complete the box)
polygon = [(2, 2), (6, 2), (4, 6), (-2, 4), (10, 5)]  # Polygon vertices in any order

clipped_polygon = clip_polygon(frame, polygon)

# Plotting the results
frame_x, frame_y = zip(*frame)
polygon_x, polygon_y = zip(*polygon)
clipped_x, clipped_y = zip(*clipped_polygon)

plt.plot(frame_x, frame_y, 'r-', label='Frame')
plt.plot(polygon_x, polygon_y, 'b-', label='Original Polygon')
plt.plot(clipped_x, clipped_y, 'g-', label='Clipped Polygon')
for i, (x, y) in enumerate(polygon):
    plt.text(x, y, chr(97 + i), fontsize=12, ha='center', va='center')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sutherland-Hodgman Polygon Clipping')
plt.grid(True)
plt.show()