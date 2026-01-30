"""
Customer Service Call Center

This module implements a call center queue system with priority handling.
Students need to manage multiple priority queues and track call statistics.

@Author: Alok More
"""

import time


class Call:
    """Represents a customer service call"""
    
    def __init__(self, caller_id: str, issue: str, priority: int, timestamp: float):
        """
        Initialize a call with caller information and priority
        
        Args:
            caller_id (str): Customer phone number
            issue (str): Description of the problem
            priority (int): 1 (urgent), 2 (normal), 3 (low)
            timestamp (float): Time when call was received (from time.time())
        """
        self.caller_id = caller_id
        self.issue = issue
        self.priority = priority
        self.timestamp = timestamp
        self.answer_timestamp = None  # Set when call is answered
    
    def __repr__(self):
        return f"Call(caller_id='{self.caller_id}', issue='{self.issue}', priority={self.priority})"
    
    def get_wait_time(self) -> float:
        """
        Calculate how long this call has been/was waiting
        
        Returns:
            float: Wait time in seconds (from received to answered)
        """
        if self.answer_timestamp is None:
            # Call not answered yet - return current wait time
            return time.time() - self.timestamp
        else:
            # Call was answered - return total wait time
            return self.answer_timestamp - self.timestamp


class CallCenter:
    """Call center with priority queue management"""
    
    def __init__(self):
        """
        Initialize an empty call center
        
        You need to track:
        - Three separate queues for different priority levels (1, 2, 3)
        - Statistics about received and answered calls
        - Wait times for answered calls
        """
        self.urgent = []
        self.normal = []
        self.low = []
        self.received = 0
        self.answered = 0
        self.answered_calls = []  
    
    def receive_call(self, caller_id: str, issue: str, priority: int):
        """
        Receive a new call and add it to the appropriate priority queue
        
        Args:
            caller_id (str): Customer phone number
            issue (str): Description of the problem
            priority (int): 1 (urgent), 2 (normal), 3 (low)
        
        The call should be added to the end of the appropriate priority queue
        and marked with the current timestamp.
        """
        call = Call(caller_id, issue, priority, time.time())
        if call.priority == 1:
            self.urgent.append(call)
            self.received += 1

        elif call.priority == 2:
            self.normal.append(call)
            self.received += 1

        else:
            self.low.append(call)
            self.received += 1
    
    def answer_next_call(self):
        """
        Answer the next call based on priority
        
        Returns:
            Call: The next call to be answered, or None if no calls waiting
        
        Priority order:
        1. First, check priority 1 queue (urgent)
        2. Then, check priority 2 queue (normal)
        3. Finally, check priority 3 queue (low)
        
        Within each priority level, calls are answered FIFO (first in, first out).
        """
        if len(self.urgent) != 0:
            call = self.urgent.pop(0)
            call.answer_timestamp = time.time()
            self.answered += 1
            self.answered_calls.append(call)
            return call
        
        elif len(self.normal) != 0:
            call = self.normal.pop(0)
            call.answer_timestamp = time.time()
            self.answered += 1
            self.answered_calls.append(call)
            return call
        
        elif len(self.low) != 0:
            call = self.low.pop(0)
            call.answer_timestamp = time.time()
            self.answered += 1
            self.answered_calls.append(call)
            return call
        
        else: return None
    
    def get_queue_length(self, priority: int) -> int:
        """
        Get the number of calls waiting at a specific priority level
        
        Args:
            priority (int): Priority level (1, 2, or 3)
        
        Returns:
            int: Number of calls in that priority queue
        """
        if priority == 1:
            return len(self.urgent)
    
        elif priority == 2:
            return len(self.normal)
        
        else:
            return len(self.low)
    
    def get_average_wait_time(self) -> float:
        """
        Calculate the average wait time for all answered calls
        
        Returns:
            float: Average wait time in seconds, or 0.0 if no calls answered
        
        Wait time = time between when call was received and when it was answered
        """
        # TODO: Calculate average of wait times for all answered calls
        # Hint: Use call.get_wait_time() for each answered call
        # Return 0.0 if no calls have been answered ye
        if self.answered == 0:
            return 0.0

        total = 0
        for call in self.answered_calls:
            total += call.get_wait_time()

        avg = total/self.answered
        return avg
    
    def get_longest_waiting_call(self):
        """
        Find the call that has been waiting the longest (across all priorities)
        
        Returns:
            Call: The call with the longest current wait time, or None if no calls waiting
        """
        if len(self.urgent) != 0:
            call1 = self.urgent[0]
            if len(self.normal) != 0:
                call2 = self.normal[0]
                if len(self.low) != 0:
                    call3 = self.low[0]

                    if call1.timestamp < call2.timestamp:
                        if call1.timestamp < call3.timestamp:
                            return call1
                        else: return call3

                    else:
                        if call2.timestamp < call3.timestamp:
                            return call2
                        else: return call3
                else:
                    if call1.timestamp < call2.timestamp:
                        return call1
                    else: return call2 

            else:
                if len(self.low) != 0:
                    call3 = self.low[0]
                    if call1.timestamp < call3.timestamp:
                        return call1
                    else: return call3

                else: return call1

        elif len(self.normal) != 0:
            call2 = self.normal[0]
            if len(self.low) != 0:
                call3 = self.low[0]

                if call2.timestamp < call3.timestamp:
                    return call2
                else: return call3

            else:
                return call2
                
        else:
            if len(self.low) != 0:
                call3 = self.low[0]
                return call3
            else: return None
    
    def get_total_calls_received(self) -> int:
        """
        Get the total number of calls received since call center started
        
        Returns:
            int: Total calls received
        """
        return self.received
    
    def get_total_calls_answered(self) -> int:
        """
        Get the total number of calls answered since call center started
        
        Returns:
            int: Total calls answered
        """
        return self.answered
    
    def get_total_calls_waiting(self) -> int:
        """
        Get the total number of calls currently waiting (across all priorities)
        
        Returns:
            int: Total calls waiting in all queues
        """
        u = len(self.urgent)
        n = len(self.normal)
        l = len(self.low)
        return u+n+l
