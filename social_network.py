"""
Social Network Connection Analyzer

This module implements a social network analyzer using symbol tables (dictionaries)
and graph algorithms to find connections between users.

@Author: Alok More
"""

from collections import deque


class User:
    """Represents a user in the social network"""
    
    def __init__(self, username: str, name: str, interests: list):
        """
        Initialize a user with username, full name, and interests
        
        Args:
            username (str): Unique username identifier
            name (str): User's full name
            interests (list[str]): List of user's interests/hobbies
        """
        self.username = username
        self.name = name
        self.interests = interests.copy() if interests else []
    
    def __repr__(self):
        return f"User(username='{self.username}', name='{self.name}')"
    
    def __eq__(self, other):
        """Two users are equal if they have the same username"""
        if isinstance(other, User):
            return self.username == other.username
        return False


class SocialNetwork:
    """Social network with graph-based connection analysis"""
    
    def __init__(self):
        """
        Initialize an empty social network
        
        You need to use two symbol tables (dictionaries):
        1. Map username → User object (for looking up user information)
        2. Map username → list of connected usernames (for the graph structure)
        
        Think of it like:
        - A phone book mapping names to contact info (user dictionary)
        - A relationship map showing who is friends with whom (connections dictionary)
        """
        self.user = {}
        self.connections = {}
    
    def add_user(self, username: str, name: str, interests: list):
        """
        Add a new user to the network
        
        Args:
            username (str): Unique username
            name (str): User's full name
            interests (list[str]): List of interests
        """
        us = User(username, name, interests)
        self.user[username] = us
        self.connections[username] = []
    
    def add_connection(self, username1: str, username2: str):
        """
        Create a bidirectional friendship between two users
        
        Args:
            username1 (str): First user's username
            username2 (str): Second user's username
        
        A friendship is bidirectional - if A is friends with B, then B is friends with A.
        Add each user to the other's connections list.
        """
        if username1 and username2 in self.user:
            if not self.connections[username1]:
                self.connections[username1] = [username2]
            else:
                if username2 not in self.connections[username1]:
                    self.connections[username1].append(username2)
                else: return "Already know each other."

            if not self.connections[username2]:
                self.connections[username2] = [username1]
            else:
                if username1 not in self.connections[username2]:
                    self.connections[username2].append(username1)
                else: return "Already know each other."

        else: return "User not registered"
    
    def get_user(self, username: str):
        """
        Get user object for given username
        
        Args:
            username (str): Username to look up
        
        Returns:
            User: User object, or None if not found
        """
        if username in self.user:
            return self.user[username]
        else: return None
    
    def get_connections(self, username: str) -> list:
        """
        Get list of usernames connected to given user
        
        Args:
            username (str): Username to look up
        
        Returns:
            list[str]: List of connected usernames, empty list if user not found
        """
        if username in self.connections:
            return self.connections[username]
        else: return []
    
    def get_connection_count(self, username: str) -> int:
        """
        Get number of direct connections for a user
        
        Args:
            username (str): Username to look up
        
        Returns:
            int: Number of direct connections, 0 if user not found
        """
        if username in self.connections:
            return len(self.connections[username])
        else: return 0
    
    def find_path(self, start_username: str, end_username: str) -> list:
        """
        Find shortest path between two users using BFS (Breadth-First Search)
        
        Args:
            start_username (str): Starting user
            end_username (str): Target user
        
        Returns:
            list[str]: Shortest path as list of usernames, or None if no path exists
        
        BFS Algorithm for shortest path:
        1. Use a queue to track users to visit (start with start_username)
        2. Use a dictionary to track visited users and their parent in the path
        3. For each user, explore their connections
        4. When you reach end_username, reconstruct the path from start to end
        
        Think of it like:
        "Six Degrees of Kevin Bacon" - finding the shortest chain of connections
        between two people. BFS guarantees finding the shortest path.
        """
        # TODO: Handle edge cases - users don't exist, start == end
        
        # TODO: Initialize BFS data structures:
        # - queue (use collections.deque for efficiency)
        # - visited dictionary (maps username → parent username in path)
        # - Add start_username to queue and visited
        
        # TODO: BFS loop:
        # While queue is not empty:
        #   - Dequeue a user
        #   - If it's the target user, reconstruct path and return
        #   - For each connection of current user:
        #     - If not visited, add to queue and mark visited with current user as parent
        
        # TODO: If loop completes without finding target, return None (no path exists)
        
        # TODO: Path reconstruction:
        # Start from end_username, follow parent pointers back to start_username
        # Reverse the path to get start → end order
        if start_username or end_username in self.user:
            if start_username != end_username:
                queue = deque([start_username])
                visited = {start_username: None}

                while queue:
                    current = queue.popleft()

                    if current == end_username:
                        path = []
                        node = end_username

                        while node is not None:
                            path.append(node)
                            node = visited[node]
                        path.reverse()
                        return path
                    
                    for user in self.connections[current]:
                        if user not in visited:
                            visited[user] = current
                            queue.append(user)

                return None

            else: return [start_username]
        else: return None
    
    def get_degrees_of_separation(self, start_username: str, end_username: str) -> int:
        """
        Get number of connections in shortest path between two users
        
        Args:
            start_username (str): Starting user
            end_username (str): Target user
        
        Returns:
            int: Number of edges in shortest path, -1 if no path exists
        
        "Degrees of separation" means the number of friendship links in the path.
        If path is [alice, bob, carol, dave], there are 3 degrees of separation
        (alice→bob→carol→dave).
        """
        path = self.find_path(start_username, end_username)
        if path == None:
            return -1
        else:
            return len(path)-1
    
    def find_common_connections(self, username1: str, username2: str) -> list:
        """
        Find users connected to both given users
        
        Args:
            username1 (str): First user
            username2 (str): Second user
        
        Returns:
            list[str]: Usernames connected to both users (sorted alphabetically)
        
        Think of it like: "Who are our mutual friends?"
        """
        connect1 = self.connections[username1]
        connect2 = self.connections[username2]

        common = [c for c in connect1 if c in connect2]
        sort = sorted(common)
        return sort
    
    def get_users_by_interest(self, interest: str) -> list:
        """
        Find all users with a specific interest
        
        Args:
            interest (str): Interest to search for
        
        Returns:
            list[str]: Usernames of users with that interest (sorted alphabetically)
        """
        matching = []
        for us in self.user:
            likes = self.user[us].interests
            if interest in likes:
                matching.append(us)

        if matching:
            match_sort = sorted(matching)
            return match_sort
        else: return []
    
    def get_network_statistics(self) -> dict:
        """
        Calculate statistics about the social network
        
        Returns:
            dict: Dictionary with keys:
                - 'total_users': Total number of users
                - 'total_connections': Total number of friendships (count each once)
                - 'average_connections': Average connections per user
                - 'most_connected_user': Username with most connections
        
        Note: Each friendship should be counted once, not twice
        (even though stored bidirectionally in your data structure)
        """
        total_users = len(self.user)
        total_count = [len(self.connections[k]) for k in self.connections]
        total_connections = sum(total_count)//2

        connect = 0

        if total_connections and total_users:
            for us in self.connections:
                user = len(self.connections[us])
                connect += user

            avg = connect/total_users

        else: avg = 0

        max_connect = 0
        most_connected = None

        for person in self.connections:
            if len(self.connections[person]) > max_connect:
                max_connect = len(self.connections[person])
                most_connected = person

        stats = {"total_users":total_users, "total_connections":total_connections, "average_connections":avg, "most_connected_user": most_connected}
        return stats
    
    def get_total_users(self) -> int:
        """
        Get total number of users in the network
        
        Returns:
            int: Number of users
        """
        return len(self.user)
