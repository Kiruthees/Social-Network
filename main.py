from scratch import SocialNetwork
from plot import visualize
sn = SocialNetwork()
sn.load_from_csv("data/sample_graph.csv")

# sn.visualize()
visualize("data/sample_graph.csv")

print("\nTop Influencers:")
for user, deg in sn.most_connected_users():
    print(f"{user} with {deg} connections")

print("\nMutual friends of Alice and Charlie:")
print(sn.mutual_friends("Kishore", "Srinidhi"))

print("\nShortest path from Sanch to Athi:")
print(sn.shortest_path("Sanch", "Athi"))

print("\nFriend recommendations for Kishore:")
print(sn.recommend_friends("Kishore"))

print("\nCommunities detected:")
for i, group in enumerate(sn.detect_communities(), 1):
    print(f"Community {i}: {group}")
