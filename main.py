## Data Representation: For this exercise, represent the social network using a dictionary where keys are user IDs and values are lists of friends’ IDs.; For instance: social_network = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 5], 4: [2], 5: [3]}; This indicates: User 1 is friends with Users 2 and 3. User 2 is friends with Users 1, 3, and 4. … and so on.; Example: Using the social_network representation above: Input: start_user = 1, end_user = 5; Output: [1, 3, 5]; This indicates User 1 is connected to User 5 through User 3.

from collections import deque
import unittest


# Code Skeleton for BFS-based Social Network Connections

class SocialNetwork:
    def __init__(self, connections):
        self.network = connections

    def find_shortest_connection(self, start_user, end_user):
        """
        Use BFS to find the shortest chain of mutual friends between start_user and end_user.
        If they're not connected, return an empty list.
        """
        if start_user == end_user:
            return [start_user]

        # Initialize the queue for BFS
        queue = deque([(start_user, [start_user])])
        visited = set()

        while queue:
            current_user, path = queue.popleft()

            # Check if the current user is the target user
            if current_user == end_user:
                return path

            # Check if the current user has been visited
            if current_user in visited:
                continue

            # Mark the current user as visited
            visited.add(current_user)

            # Explore friends of the current user
            for friend in self.network.get(current_user, []):
                if friend not in visited:
                    queue.append((friend, path + [friend]))

        # If no connection is found
        return []


# Unittests
class TestSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.network_data = {
            1: [2, 3],
            2: [1, 3, 4],
            3: [1, 2, 5],
            4: [2],
            5: [3]
        }
        self.social_network = SocialNetwork(self.network_data)

    def test_direct_connection(self):
        self.assertEqual(self.social_network.find_shortest_connection(1, 3), [1, 3])

    def test_indirect_connection(self):
        self.assertEqual(self.social_network.find_shortest_connection(1, 5), [1, 3, 5])

    def test_no_connection(self):
        self.assertEqual(self.social_network.find_shortest_connection(1, 6), [])

    def test_same_user(self):
        self.assertEqual(self.social_network.find_shortest_connection(1, 1), [1])


if __name__ == "__main__":
    social_network_data = {
        1: [2, 3],
        2: [1, 3, 4],
        3: [1, 2, 5],
        4: [2],
        5: [3]
    }

    social_network = SocialNetwork(social_network_data)

    start_user = 1
    end_user = 5

    result = social_network.find_shortest_connection(start_user, end_user)

    print(f"Using the social network representation:")
    print(f"Input: start_user = {start_user}, end_user = {end_user}")
    print(f"Output: {result}")