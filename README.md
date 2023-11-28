# Social Network Connections

### Overview
This Python program represents a social network using a dictionary where keys are user IDs, and values are lists of friends' IDs. The social network class, SocialNetwork, provides a method, find_shortest_connection, which utilizes Breadth-First Search (BFS) to find the shortest chain of mutual friends between two users in the network.

### Usage
Data Representation:
* Represent the social network using a dictionary, e.g., social_network = {1: [2, 3], 2: [1, 3, 4], ...}.
Finding Shortest Connection:
* Create an instance of the SocialNetwork class with the social network data.
* Call the find_shortest_connection method with the start user ID and end user ID.
* The method returns a list representing the shortest chain of mutual friends.

 Happy coding!
