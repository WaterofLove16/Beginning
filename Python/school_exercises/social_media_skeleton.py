'''
Tutorial Test Week 10 - Question 3 (Extra/Advanced)
Social Media Connection Analyzer

@Author: Alok More
'''


class SocialNetwork:
    """
    Analyzes a social network to find connection patterns and 
    analyze the small-world phenomenon.
    Combines ordered data structures with graph algorithms.
    """
    
    def __init__(self):
        """Initialize an empty social network"""
        # TODO: Initialize your data structures here
        # Hint: You'll need to store users and their friendships (graph)
        # Consider using a dictionary/adjacency list for the graph
        pass
    
    def add_user(self, username):
        """
        Add a user to the network.
        
        Args:
            username (str): The username to add
        
        Returns:
            str: Confirmation message
        """
        # TODO: Implement adding user
        # Return format: "User {username} added."
        # Or: "User {username} already exists."
        pass
    
    def add_friendship(self, user1, user2):
        """
        Create a bidirectional friendship between two users.
        
        Args:
            user1 (str): First username
            user2 (str): Second username
        
        Returns:
            str: Confirmation or error message
        """
        # TODO: Implement adding friendship (bidirectional)
        # Return format: "Friendship created between {user1} and {user2}."
        # Or: "User {username} does not exist."
        # Or: "Friendship already exists."
        pass
    
    def get_friends(self, username):
        """
        Get all friends of a given user, sorted alphabetically.
        
        Args:
            username (str): The username to query
        
        Returns:
            list: Sorted list of friend usernames
        """
        # TODO: Implement getting friends list
        # Return empty list if user has no friends or doesn't exist
        pass
    
    def find_connection_path(self, user1, user2):
        """
        Find the shortest path connecting user1 to user2 using BFS.
        
        Args:
            user1 (str): Starting username
            user2 (str): Target username
        
        Returns:
            list: List of usernames representing the path from user1 to user2
                  Empty list if no path exists or users don't exist
        """
        # TODO: Implement breadth-first search for shortest path
        # Return format: [user1, intermediate_user, ..., user2]
        # Hint: Use a queue for BFS, track visited nodes and parents
        pass
    
    def degrees_of_separation(self, user1, user2):
        """
        Calculate degrees of separation between two users.
        
        Args:
            user1 (str): First username
            user2 (str): Second username
        
        Returns:
            int: Number of degrees of separation
                 0 if same user
                 1 if direct friends
                 2 if friend-of-friend
                 -1 if no connection or user doesn't exist
        """
        # TODO: Implement degrees calculation
        # Hint: Use find_connection_path and calculate path length - 1
        pass
    
    def get_users_within_n_degrees(self, username, n):
        """
        Get all users within n degrees of separation from username.
        
        Args:
            username (str): The username to start from
            n (int): Maximum degrees of separation
        
        Returns:
            list: Sorted list of usernames (excludes username itself)
        """
        # TODO: Implement finding users within n degrees
        # Hint: Use BFS with depth tracking
        # Return empty list if user doesn't exist
        pass
    
    def average_separation(self, username):
        """
        Calculate average degrees of separation from username to all 
        other connected users.
        
        Args:
            username (str): The username to analyze
        
        Returns:
            float: Average degrees of separation (0.0 if no connections)
        """
        # TODO: Implement average separation calculation
        # Hint: Calculate separation to all reachable users and average
        # Ignore unreachable users in the calculation
        # Return 0.0 if user doesn't exist or has no connections
        pass
    
    def count_users(self):
        """
        Get the total number of users in the network.
        
        Returns:
            int: Number of users
        """
        # TODO: Implement user count
        pass


# Simple testing code
if __name__ == "__main__":
    print("Testing SocialNetwork Class")
    print("=" * 50)
    
    network = SocialNetwork()
    
    # Test 1: Add users
    print("\n1. Adding users:")
    print(network.add_user("Alice"))
    print(network.add_user("Bob"))
    print(network.add_user("Charlie"))
    print(network.add_user("Diana"))
    print(network.add_user("Eve"))
    
    # Test 2: Add duplicate user
    print("\n2. Adding duplicate user:")
    print(network.add_user("Alice"))
    
    # Test 3: Add friendships
    print("\n3. Adding friendships:")
    print(network.add_friendship("Alice", "Bob"))
    print(network.add_friendship("Bob", "Charlie"))
    print(network.add_friendship("Charlie", "Diana"))
    print(network.add_friendship("Alice", "Eve"))
    
    # Test 4: Add friendship with non-existent user
    print("\n4. Adding friendship with non-existent user:")
    print(network.add_friendship("Alice", "Frank"))
    
    # Test 5: Get friends
    print("\n5. Getting friends:")
    print(f"Alice's friends: {network.get_friends('Alice')}")
    print(f"Bob's friends: {network.get_friends('Bob')}")
    
    # Test 6: Count users
    print("\n6. User count:")
    print(f"Total users: {network.count_users()}")
    
    # Test 7: Find connection path
    print("\n7. Finding connection paths:")
    print(f"Alice to Diana: {network.find_connection_path('Alice', 'Diana')}")
    print(f"Eve to Charlie: {network.find_connection_path('Eve', 'Charlie')}")
    
    # Test 8: Degrees of separation
    print("\n8. Degrees of separation:")
    print(f"Alice to Bob: {network.degrees_of_separation('Alice', 'Bob')}")
    print(f"Alice to Diana: {network.degrees_of_separation('Alice', 'Diana')}")
    print(f"Alice to Alice: {network.degrees_of_separation('Alice', 'Alice')}")
    
    # Test 9: Users within n degrees
    print("\n9. Users within 2 degrees of Alice:")
    print(network.get_users_within_n_degrees("Alice", 2))
    
    # Test 10: Average separation
    print("\n10. Average separation from Alice:")
    print(f"Average: {network.average_separation('Alice'):.2f}")
    
    # Test 11: Small world demonstration
    print("\n11. Small World Demonstration:")
    print("Adding more users and connections...")
    network.add_user("Frank")
    network.add_user("Grace")
    network.add_friendship("Diana", "Frank")
    network.add_friendship("Frank", "Grace")
    network.add_friendship("Eve", "Grace")
    
    print(f"Alice to Grace path: {network.find_connection_path('Alice', 'Grace')}")
    print(f"Degrees: {network.degrees_of_separation('Alice', 'Grace')}")
    print(f"Average separation from Alice: {network.average_separation('Alice'):.2f}")
    
    print("\n" + "=" * 50)
    print("Testing complete!")
