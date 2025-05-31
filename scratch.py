# Breadth-First Search (BFS) – used in shortest_path and detect_communities
# Degree Centrality – used in most_connected_users
# Intersection (for mutual nodes) – used in mutual_friends
# Common Neighbors heuristic – used in recommend_friends

from collections import defaultdict, deque
import csv,math
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.cm as cm

class SocialNetwork:
    def __init__(self):
        self.graph = defaultdict(set)

    def load_from_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                a, b = row['source'], row['target']
                self.graph[a].add(b)
                self.graph[b].add(a)

    def visualize(self):
        print("Graph:")
        for user, friends in self.graph.items():
            print(f"{user}: {', '.join(friends)}")

    def mutual_friends(self, u1, u2):
        return self.graph[u1].intersection(self.graph[u2])

    def most_connected_users(self, top_n=5):
        degrees = [(user, len(friends)) for user, friends in self.graph.items()]
        degrees.sort(key=lambda x: -x[1])
        return degrees[:top_n]

    def shortest_path(self, start, end):
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            current, path = queue.popleft()
            if current == end:
                return path

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None

    def recommend_friends(self, user):
        direct = self.graph[user]
        recommendations = defaultdict(int)

        for friend in direct:
            for fof in self.graph[friend]:
                if fof != user and fof not in direct:
                    recommendations[fof] += 1

        return sorted(recommendations.items(), key=lambda x: -x[1])

    def detect_communities(self):
        visited = set()
        components = []

        for user in self.graph:
            if user not in visited:
                q = deque([user])
                component = []

                while q:
                    u = q.popleft()
                    if u not in visited:
                        visited.add(u)
                        component.append(u)
                        q.extend(self.graph[u] - visited)

                components.append(component)

        return components
