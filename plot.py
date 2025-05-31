import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
from collections import defaultdict
import math
import random
import csv

def visualize(csv_path):
    edges = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header
        for row in reader:
            if len(row) >= 2:
                edges.append((row[0].strip(), row[1].strip()))
    
    adj = defaultdict(list)
    nodes = set()
    for src, dst in edges:
        adj[src].append(dst)
        nodes.add(src)
        nodes.add(dst)
    nodes = list(nodes)

    angle_gap = 2 * math.pi / len(nodes)
    positions = {}
    for i, node in enumerate(nodes):
        angle = i * angle_gap
        x = math.cos(angle)
        y = math.sin(angle)
        positions[node] = (x, y)

    node_colors = plt.cm.rainbow([i / len(nodes) for i in range(len(nodes))])
    edge_colors = plt.cm.viridis([i / len(edges) for i in range(len(edges))])
    random.shuffle(edge_colors)

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_facecolor("#1e1e2f")
    fig.patch.set_facecolor("#1e1e2f")

    for i, (src, dst) in enumerate(edges):
        x1, y1 = positions[src]
        x2, y2 = positions[dst]
        dx = x2 - x1
        dy = y2 - y1
        dist = math.hypot(dx, dy)
        shrink = 0.12
        x1 += dx / dist * shrink
        y1 += dy / dist * shrink
        x2 -= dx / dist * shrink
        y2 -= dy / dist * shrink

        arrow = FancyArrowPatch((x1, y1), (x2, y2),
                                arrowstyle='-', color=edge_colors[i],
                                mutation_scale=15, linewidth=2)
        ax.add_patch(arrow)

    for i, (node, (x, y)) in enumerate(positions.items()):
        circle = Circle((x, y), 0.125, color=node_colors[i], ec='white', lw=2, zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, node, fontsize=10, ha='center', va='center', fontweight='bold',
                color='white', zorder=3)

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title("Social Network Graph", fontsize=16, fontweight='bold', color='white')
    plt.tight_layout()
    plt.show()
