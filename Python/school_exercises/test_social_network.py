"""
Unit Tests: Social Network Connection Analyzer

Tests symbol table operations and graph algorithms (BFS for shortest path).

@Author: Alok More
"""

import unittest
from social_network import SocialNetwork, User


class TestSocialNetwork(unittest.TestCase):
    """Test cases for Social Network System"""
    
    def setUp(self):
        """Set up a sample social network for testing"""
        self.network = SocialNetwork()
        
        # Add users
        self.network.add_user("alice", "Alice Smith", ["coding", "hiking"])
        self.network.add_user("bob", "Bob Jones", ["coding", "music"])
        self.network.add_user("carol", "Carol White", ["hiking", "music"])
        self.network.add_user("dave", "Dave Brown", ["coding"])
        self.network.add_user("eve", "Eve Davis", ["music", "reading"])
        
        # Create connections - a connected graph
        #   alice -- bob -- carol
        #     |              |
        #   dave            eve
        self.network.add_connection("alice", "bob")
        self.network.add_connection("alice", "dave")
        self.network.add_connection("bob", "carol")
        self.network.add_connection("carol", "eve")
    
    def test_01_add_user_and_retrieve(self):
        """Test 1: Adding users and retrieving user information (1 mark)"""
        user = self.network.get_user("alice")
        
        self.assertIsNotNone(user, "Should retrieve existing user")
        self.assertEqual(user.username, "alice", "Username should match")
        self.assertEqual(user.name, "Alice Smith", "Name should match")
        self.assertIn("coding", user.interests, "Should have coding interest")
        self.assertIn("hiking", user.interests, "Should have hiking interest")
        
        # Non-existent user
        non_user = self.network.get_user("nobody")
        self.assertIsNone(non_user, "Should return None for non-existent user")
    
    def test_02_bidirectional_connections(self):
        """Test 2: Connections are bidirectional (1 mark)"""
        alice_connections = self.network.get_connections("alice")
        bob_connections = self.network.get_connections("bob")
        
        self.assertIn("bob", alice_connections, "Alice should be connected to Bob")
        self.assertIn("alice", bob_connections, "Bob should be connected to Alice")
        self.assertEqual(self.network.get_connection_count("alice"), 2,
                        "Alice should have 2 connections")
    
    def test_03_find_direct_path(self):
        """Test 3: Finding path between directly connected users (1 mark)"""
        path = self.network.find_path("alice", "bob")
        
        self.assertIsNotNone(path, "Should find path between connected users")
        self.assertEqual(len(path), 2, "Direct connection should have 2 nodes")
        self.assertEqual(path[0], "alice", "Path should start with alice")
        self.assertEqual(path[-1], "bob", "Path should end with bob")
    
    def test_04_find_shortest_path_multiple_hops(self):
        """Test 4: Finding shortest path requiring multiple hops (1 mark)"""
        # Path from alice to eve: alice → bob → carol → eve
        path = self.network.find_path("alice", "eve")
        
        self.assertIsNotNone(path, "Should find path")
        self.assertEqual(path[0], "alice", "Path should start with alice")
        self.assertEqual(path[-1], "eve", "Path should end with eve")
        self.assertEqual(len(path), 4, "Shortest path should have 4 nodes")
        
        # Verify it's a valid path (each consecutive pair is connected)
        for i in range(len(path) - 1):
            connections = self.network.get_connections(path[i])
            self.assertIn(path[i+1], connections,
                         f"{path[i]} should be connected to {path[i+1]}")
    
    def test_05_no_path_exists(self):
        """Test 5: Returns None when no path exists between users (1 mark)"""
        # Add isolated user
        self.network.add_user("isolated", "Isolated User", ["none"])
        
        path = self.network.find_path("alice", "isolated")
        self.assertIsNone(path, "Should return None for disconnected users")
        
        # Also test non-existent user
        path2 = self.network.find_path("alice", "nobody")
        self.assertIsNone(path2, "Should return None for non-existent user")
    
    def test_06_degrees_of_separation(self):
        """Test 6: Calculating degrees of separation correctly (1 mark)"""
        # Direct connection: 1 degree
        degrees = self.network.get_degrees_of_separation("alice", "bob")
        self.assertEqual(degrees, 1, "Direct connection should be 1 degree")
        
        # Two hops: alice → bob → carol
        degrees = self.network.get_degrees_of_separation("alice", "carol")
        self.assertEqual(degrees, 2, "Two-hop path should be 2 degrees")
        
        # Three hops: alice → bob → carol → eve
        degrees = self.network.get_degrees_of_separation("alice", "eve")
        self.assertEqual(degrees, 3, "Three-hop path should be 3 degrees")
        
        # Same user: 0 degrees
        degrees = self.network.get_degrees_of_separation("alice", "alice")
        self.assertEqual(degrees, 0, "Same user should be 0 degrees")
        
        # No path: -1
        self.network.add_user("isolated", "Isolated User", [])
        degrees = self.network.get_degrees_of_separation("alice", "isolated")
        self.assertEqual(degrees, -1, "No path should return -1")
    
    def test_07_find_common_connections(self):
        """Test 7: Finding mutual connections between users (1 mark)"""
        # Alice and Carol both connected to Bob
        common = self.network.find_common_connections("alice", "carol")
        
        self.assertIsInstance(common, list, "Should return a list")
        self.assertIn("bob", common, "Bob should be common connection")
        self.assertEqual(len(common), 1, "Should have exactly 1 common connection")
        
        # Bob and Eve both connected to Carol
        common2 = self.network.find_common_connections("bob", "eve")
        self.assertIn("carol", common2, "Carol should be common connection")
        
        # No common connections
        common3 = self.network.find_common_connections("dave", "eve")
        self.assertEqual(len(common3), 0, "Dave and Eve should have no common connections")
    
    def test_08_users_by_interest(self):
        """Test 8: Finding users with specific interests (1 mark)"""
        # Find all users interested in coding
        coders = self.network.get_users_by_interest("coding")
        
        self.assertIsInstance(coders, list, "Should return a list")
        self.assertIn("alice", coders, "Alice likes coding")
        self.assertIn("bob", coders, "Bob likes coding")
        self.assertIn("dave", coders, "Dave likes coding")
        self.assertEqual(len(coders), 3, "Should find exactly 3 users")
        
        # Find users interested in music
        music_lovers = self.network.get_users_by_interest("music")
        self.assertEqual(len(music_lovers), 3, "Should find 3 music lovers")
        
        # Interest that no one has
        nobody = self.network.get_users_by_interest("knitting")
        self.assertEqual(len(nobody), 0, "Should return empty list for non-existent interest")
    
    def test_09_network_statistics(self):
        """Test 9: Calculating network statistics correctly (1 mark)"""
        stats = self.network.get_network_statistics()
        
        self.assertIsInstance(stats, dict, "Should return a dictionary")
        
        # Check total users
        self.assertEqual(stats['total_users'], 5, "Should have 5 users")
        
        # Check total connections (4 friendships)
        self.assertEqual(stats['total_connections'], 4,
                        "Should have 4 unique friendships")
        
        # Check average connections (8 total / 5 users = 1.6)
        self.assertAlmostEqual(stats['average_connections'], 1.6, places=1,
                              msg="Average should be 1.6 connections per user")
        
        # Check most connected user (bob and carol both have 2 connections)
        self.assertIn(stats['most_connected_user'], ['bob', 'carol'],
                     "Most connected user should be bob or carol")
    
    def test_10_complex_network_shortest_path(self):
        """Test 10: Shortest path in complex network (1 mark)"""
        # Create a more complex network with multiple possible paths
        complex_net = SocialNetwork()
        
        # Add users
        users = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        for u in users:
            complex_net.add_user(u, f"User {u}", [])
        
        # Create connections forming a graph:
        #     a --- b --- c
        #     |     |     |
        #     d --- e --- f
        #           |
        #           g
        complex_net.add_connection('a', 'b')
        complex_net.add_connection('b', 'c')
        complex_net.add_connection('a', 'd')
        complex_net.add_connection('d', 'e')
        complex_net.add_connection('b', 'e')
        complex_net.add_connection('e', 'f')
        complex_net.add_connection('c', 'f')
        complex_net.add_connection('e', 'g')
        
        # Test 1: Shortest path from 'a' to 'c'
        # Possible paths: a→b→c (2 hops), a→d→e→b→c (4 hops), a→d→e→f→c (4 hops)
        # Shortest should be: a→b→c
        path_ac = complex_net.find_path('a', 'c')
        self.assertEqual(len(path_ac), 3, "Shortest path a→c should have 3 nodes")
        self.assertEqual(complex_net.get_degrees_of_separation('a', 'c'), 2,
                        "a to c should be 2 degrees")
        
        # Test 2: Shortest path from 'a' to 'g'
        # Possible paths: a→b→e→g (3 hops), a→d→e→g (3 hops)
        # Both are shortest, length should be 4 nodes
        path_ag = complex_net.find_path('a', 'g')
        self.assertEqual(len(path_ag), 4, "Shortest path a→g should have 4 nodes")
        self.assertEqual(complex_net.get_degrees_of_separation('a', 'g'), 3,
                        "a to g should be 3 degrees")
        
        # Test 3: Verify BFS found an actual valid shortest path
        # Check that each consecutive pair in the path is connected
        for i in range(len(path_ag) - 1):
            connections = complex_net.get_connections(path_ag[i])
            self.assertIn(path_ag[i+1], connections,
                         f"Path should be valid: {path_ag[i]} connected to {path_ag[i+1]}")


def run_tests():
    """Run all tests and return results"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSocialNetwork)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Calculate score
    total_tests = result.testsRun
    failed_tests = len(result.failures) + len(result.errors)
    passed_tests = total_tests - failed_tests
    
    print(f"\n{'='*70}")
    print(f"RESULTS: {passed_tests}/{total_tests} tests passed")
    print(f"SCORE: {passed_tests}/10 marks")
    print(f"{'='*70}")
    
    return passed_tests


if __name__ == "__main__":
    run_tests()
