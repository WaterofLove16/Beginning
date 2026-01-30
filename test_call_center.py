"""
Unit Tests: Customer Service Call Center

Tests priority queue management and call statistics tracking.

@Author: Alok More
"""

import unittest
import time
from call_center import CallCenter, Call


class TestCallCenter(unittest.TestCase):
    """Test cases for Call Center System"""
    
    def setUp(self):
        """Set up a new call center for each test"""
        self.center = CallCenter()
    
    def test_01_receive_calls_increments_counter(self):
        """Test 1: Receiving calls increments the total received counter (1 mark)"""
        self.center.receive_call("555-0100", "Login issue", 2)
        self.center.receive_call("555-0101", "System down", 1)
        self.center.receive_call("555-0102", "Question", 3)
        
        self.assertEqual(self.center.get_total_calls_received(), 3,
                        "Should have received 3 calls")
        self.assertEqual(self.center.get_total_calls_answered(), 0,
                        "Should not have answered any calls yet")
    
    def test_02_queue_length_tracking(self):
        """Test 2: Queue lengths are tracked correctly for each priority (1 mark)"""
        self.center.receive_call("555-0100", "Login issue", 2)
        self.center.receive_call("555-0101", "System down", 1)
        self.center.receive_call("555-0102", "Another urgent", 1)
        self.center.receive_call("555-0103", "Question", 3)
        
        self.assertEqual(self.center.get_queue_length(1), 2,
                        "Priority 1 queue should have 2 calls")
        self.assertEqual(self.center.get_queue_length(2), 1,
                        "Priority 2 queue should have 1 call")
        self.assertEqual(self.center.get_queue_length(3), 1,
                        "Priority 3 queue should have 1 call")
    
    def test_03_urgent_calls_answered_first(self):
        """Test 3: Urgent calls (priority 1) are answered before others (1 mark)"""
        self.center.receive_call("555-0100", "Login issue", 2)
        time.sleep(0.01)
        self.center.receive_call("555-0101", "System down!", 1)
        time.sleep(0.01)
        self.center.receive_call("555-0102", "Question", 3)
        
        # First call answered should be the urgent one (priority 1)
        call = self.center.answer_next_call()
        self.assertIsNotNone(call, "Should return a call")
        self.assertEqual(call.priority, 1, "First call should be priority 1")
        self.assertEqual(call.caller_id, "555-0101", "Should be the urgent call")
    
    def test_04_fifo_within_same_priority(self):
        """Test 4: Within same priority, calls answered FIFO (1 mark)"""
        # Add three normal priority calls
        self.center.receive_call("555-0100", "Issue A", 2)
        time.sleep(0.01)
        self.center.receive_call("555-0101", "Issue B", 2)
        time.sleep(0.01)
        self.center.receive_call("555-0102", "Issue C", 2)
        
        # Answer them - should be in FIFO order
        call1 = self.center.answer_next_call()
        call2 = self.center.answer_next_call()
        call3 = self.center.answer_next_call()
        
        self.assertEqual(call1.caller_id, "555-0100", "First call should be answered first")
        self.assertEqual(call2.caller_id, "555-0101", "Second call should be answered second")
        self.assertEqual(call3.caller_id, "555-0102", "Third call should be answered third")
    
    def test_05_priority_order_across_all_levels(self):
        """Test 5: Correct priority ordering (1→2→3) is maintained (1 mark)"""
        # Add calls in mixed priority order
        self.center.receive_call("555-0103", "Low priority", 3)
        time.sleep(0.01)
        self.center.receive_call("555-0102", "Normal priority", 2)
        time.sleep(0.01)
        self.center.receive_call("555-0101", "Urgent!", 1)
        
        # Answer all three
        call1 = self.center.answer_next_call()
        call2 = self.center.answer_next_call()
        call3 = self.center.answer_next_call()
        
        self.assertEqual(call1.priority, 1, "Priority 1 should be answered first")
        self.assertEqual(call2.priority, 2, "Priority 2 should be answered second")
        self.assertEqual(call3.priority, 3, "Priority 3 should be answered last")
    
    def test_06_empty_queue_returns_none(self):
        """Test 6: Answering call from empty queue returns None (1 mark)"""
        call = self.center.answer_next_call()
        self.assertIsNone(call, "Should return None when no calls waiting")
        
        # Add and answer a call, then try again
        self.center.receive_call("555-0100", "Test", 2)
        self.center.answer_next_call()
        
        call2 = self.center.answer_next_call()
        self.assertIsNone(call2, "Should return None after all calls answered")
    
    def test_07_answered_calls_counter(self):
        """Test 7: Answered calls counter increments correctly (1 mark)"""
        self.center.receive_call("555-0100", "Test 1", 2)
        self.center.receive_call("555-0101", "Test 2", 1)
        self.center.receive_call("555-0102", "Test 3", 3)
        
        self.assertEqual(self.center.get_total_calls_answered(), 0,
                        "Should start with 0 answered")
        
        self.center.answer_next_call()
        self.assertEqual(self.center.get_total_calls_answered(), 1,
                        "Should have 1 answered")
        
        self.center.answer_next_call()
        self.center.answer_next_call()
        self.assertEqual(self.center.get_total_calls_answered(), 3,
                        "Should have 3 answered")
        self.assertEqual(self.center.get_total_calls_received(), 3,
                        "Should still have 3 received")
    
    def test_08_average_wait_time_calculation(self):
        """Test 8: Average wait time is calculated correctly (1 mark)"""
        # Add calls with small delays between them
        self.center.receive_call("555-0100", "Test 1", 2)
        time.sleep(0.05)  # 50ms wait
        self.center.receive_call("555-0101", "Test 2", 2)
        time.sleep(0.05)  # 50ms wait
        
        # Answer first call (should have waited ~100ms)
        self.center.answer_next_call()
        
        # Answer second call (should have waited ~50ms)
        self.center.answer_next_call()
        
        avg_wait = self.center.get_average_wait_time()
        
        # Average should be around 75ms (0.075 seconds)
        self.assertGreater(avg_wait, 0, "Average wait time should be positive")
        self.assertGreater(avg_wait, 0.04, "Average should reflect actual wait time")
        self.assertLess(avg_wait, 0.15, "Average should be reasonable")
    
    def test_09_longest_waiting_call(self):
        """Test 9: Identifying longest waiting call across priorities (1 mark)"""
        # Add calls to different priority queues with delays
        self.center.receive_call("555-0100", "First call", 3)
        time.sleep(0.02)
        self.center.receive_call("555-0101", "Second call", 1)
        time.sleep(0.02)
        self.center.receive_call("555-0102", "Third call", 2)
        
        # Longest waiting should be the first call (priority 3)
        longest = self.center.get_longest_waiting_call()
        
        self.assertIsNotNone(longest, "Should find longest waiting call")
        self.assertEqual(longest.caller_id, "555-0100",
                        "First call should be waiting longest")
        
        # Answer the urgent call (priority 1) - should not affect longest waiting
        self.center.answer_next_call()
        
        longest_after = self.center.get_longest_waiting_call()
        self.assertEqual(longest_after.caller_id, "555-0100",
                        "First call should still be waiting longest")
    
    def test_10_complex_scenario_multiple_priorities(self):
        """Test 10: Complex scenario with multiple priorities and operations (1 mark)"""
        # Add 10 calls with mixed priorities
        calls_data = [
            ("555-0100", "Issue 1", 2),
            ("555-0101", "Emergency 1", 1),
            ("555-0102", "Question 1", 3),
            ("555-0103", "Issue 2", 2),
            ("555-0104", "Emergency 2", 1),
            ("555-0105", "Question 2", 3),
            ("555-0106", "Issue 3", 2),
            ("555-0107", "Emergency 3", 1),
            ("555-0108", "Question 3", 3),
            ("555-0109", "Issue 4", 2),
        ]
        
        for caller_id, issue, priority in calls_data:
            self.center.receive_call(caller_id, issue, priority)
            time.sleep(0.01)
        
        # Verify queue lengths
        self.assertEqual(self.center.get_queue_length(1), 3, "Should have 3 urgent calls")
        self.assertEqual(self.center.get_queue_length(2), 4, "Should have 4 normal calls")
        self.assertEqual(self.center.get_queue_length(3), 3, "Should have 3 low priority calls")
        
        # Answer first 5 calls - should get all 3 urgent, then 2 normal
        answered_priorities = []
        for _ in range(5):
            call = self.center.answer_next_call()
            answered_priorities.append(call.priority)
        
        # First 3 should be urgent
        self.assertEqual(answered_priorities[:3], [1, 1, 1],
                        "First 3 answered should be urgent")
        # Next 2 should be normal
        self.assertEqual(answered_priorities[3:], [2, 2],
                        "Next 2 answered should be normal priority")
        
        # Check remaining queues
        self.assertEqual(self.center.get_queue_length(1), 0, "All urgent calls answered")
        self.assertEqual(self.center.get_queue_length(2), 2, "2 normal calls remaining")
        self.assertEqual(self.center.get_queue_length(3), 3, "All low priority calls still waiting")
        
        # Verify total statistics
        self.assertEqual(self.center.get_total_calls_received(), 10, "Received 10 calls")
        self.assertEqual(self.center.get_total_calls_answered(), 5, "Answered 5 calls")
        self.assertEqual(self.center.get_total_calls_waiting(), 5, "5 calls still waiting")


def run_tests():
    """Run all tests and return results"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCallCenter)
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
